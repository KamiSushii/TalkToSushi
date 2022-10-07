import os, re, discord, asyncio
from discord.ext import commands, pages

from modules import Embeds, Queue, TalkToSpeech
from modules.tts import TalkToSpeech

class TalkToSushi(commands.Bot):
    def __init__(self, token, api_json):
        intents = discord.Intents.default()
        intents.members = True
        intents.presences = True
        intents.message_content = True
        
        debug_guilds = [998467063972626513, 
                        513511763334135809]
        super().__init__(command_prefix=self.prefix, 
                         intents=intents, 
                         debug_guilds=debug_guilds,
                         help_command=None)
        
        self.token = token
        self.__queue = Queue()
        self.__embeds = Embeds()
        self.__tts = TalkToSpeech(api_json)
        
        self.add_commands()


    async def prefix(self, bot, msg):
        return commands.when_mentioned_or(";")(bot, msg)

        
    def run(self):
        print("[*] Starting bot")
        super().run(self.token, reconnect=True)


    async def on_connect(self):
        print(f"[*] Connected to Discord (latency: {self.latency*1000:,.0f} ms).")


    async def on_message(self, msg):
        if not msg.author.bot:
            await self.process_commands(msg)


    async def on_ready(self):
        self.client_id = (await self.application_info()).id

        activity_name='with SushiMusic! :)'
        activity_type=discord.ActivityType.playing
        
        await self.change_presence(activity=discord.Activity(type=activity_type,name=activity_name))
        print(f"[*] {self.user.name} ready.")


    async def on_error(self, err, *args, **kwargs):
        raise 


    async def on_command_error(self, ctx, exc):
        raise getattr(exc, "original", exc)


    async def process_commands(self, msg):
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

        elif ctx.message.content.startswith(";"):
            await self.process_tts(ctx)


    def add_commands(self):
        @self.slash_command()
        async def help(ctx: discord.ApplicationContext):
            paginator = pages.Paginator(
                pages=self.__embeds.help,
                show_menu=True,
                show_disabled=False,
                use_default_buttons=False,
                show_indicator=False,
                menu_placeholder="Select help"
                )
            await paginator.respond(ctx.interaction)

        @self.slash_command()
        async def stop(ctx):
            guild_id = ctx.message.guild.id
            try:
                self.__queue.destroy(guild_id)
                await self.get_voice(guild_id).stop()
                await ctx.send("Stopped")
            except: await ctx.send('Error')

        @self.slash_command()
        async def disconnect(ctx):
            guild_id = ctx.message.guild.id
            try:
                self.__queue.destroy(guild_id)
                await self.get_voice(guild_id).disconnect()
                await ctx.send("Disconnected")
            except: await ctx.send('Error')




    # TTS Main engine
    async def process_tts(self, ctx):
        guild_id = ctx.message.guild.id
        text = ctx.message.content.strip(';').strip()

        if not ctx.message.author.voice:
            await ctx.send('User is not in accessible voice channel!')
            return
        self.__queue.add_text(guild_id, text)

        await self._connect(ctx)
        if self.get_voice(guild_id).is_playing() is False:
            self.play(ctx)


    async def _connect(self, ctx):
        guild_id = ctx.message.guild.id
        voice_channel = ctx.message.author.voice.channel
        
        if self.get_voice(guild_id) is None:
            await voice_channel.connect()


    async def _disconnect(self, guild_id):      
        try:
            self.__queue.destroy(guild_id)
            await self.get_voice(guild_id).disconnect()
        except: pass


    def get_voice(self, guild_id):
        return discord.utils.get(self.voice_clients, guild=self.get_guild(guild_id))


    def transform(self, ctx, message):
        guild_id = ctx.message.guild.id
        msg = re.sub(r'<.+?>', '', message)
        param = None
        
        if len(msg.split()) > 1:
            content = str(msg.split()[1:])
            foo = msg.split()[0]

            if foo in self.__tts.gtts_prefix or foo in self.__tts.wavenet_prefix:
                msg = content
                param = foo

        tts = self.__tts.text_to_speech(msg, param)
        file = f"{guild_id}.wav"
        with open(file, "wb") as out:
            out.write(tts)


    def play(self, ctx):
        guild_id = ctx.message.guild.id
        try:
            text = self.__queue.get_next(guild_id)
            self.transform(ctx, text)

            print(f"   Playing: {text}")
            audio_source = discord.FFmpegPCMAudio(f'{guild_id}.wav', options = "-loglevel panic")
            self.get_voice(guild_id).play(audio_source, after=lambda e: self.play(ctx))

        except:
            try: os.remove(f"{guild_id}.wav")
            except: pass

    
    async def on_voice_state_update(self, member, before, after):
        try:
            guild_id = before.channel.guild.id
            voice_channel = self.get_voice(guild_id)

            if before.channel == voice_channel.channel:
                await asyncio.sleep(10)
                if not member.bot and after.channel != voice_channel.channel:
                    if not [m for m in before.channel.members if not m.bot]:
                        await self._disconnect(guild_id)
        except: pass