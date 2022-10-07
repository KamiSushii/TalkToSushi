import discord
from discord.ext import pages

class Embeds():
    def __init__(self):
        pass

    @property
    def help(self):
        self._help = [
            pages.PageGroup(
                pages=[discord.Embed(
                    title="SushiTTS Help Page",
                    description="Just type `;<text>`, then im going to join your voice channel and speak it for you <3\n"
                                "Use slash command to control the bot.\n\n"

                                "Slash Commands:\n"
                                "```"
                                "disconnect \n"
                                "stop       \n"
                                "help       \n"
                                "```",
                    colour=discord.Colour.blue()
                    )],
                label="SushiTTS Help Page",
                use_default_buttons=False,
            ),
            pages.PageGroup(
                pages=[discord.Embed(
                    title="Supported Languages",
                    description="Usage example: `;japanese Konnichiwa!` \n\n"
                    
                                "Supported languages:\n"
                                "```"
                                "af: Afrikaans      ar: Arabic          bg: Bulgarian       \n"
                                "bn: Bengali        bs: Bosnian         ca: Catalan         \n"
                                "cs: Czech          cy: Welsh           da: Danish          \n"
                                "de: German         el: Greek           en: English         \n"
                                "eo: Esperanto      es: Spanish         et: Estonian        \n"
                                "fi: Finnish        fr: French          gu: Gujarati        \n"
                                "hi: Hindi          hr: Croatian        hu: Hungarian       \n"
                                "hy: Armenian       id: Indonesian      is: Icelandic       \n"
                                "it: Italian        iw: Hebrew          ja: Japanese        \n"
                                "jw: Javanese       km: Khmer           kn: Kannada         \n"
                                "ko: Korean         la: Latin           lv: Latvian         \n"
                                "mk: Macedonian     ml: Malayalam       mr: Marathi         \n"
                                "ms: Malay          my: Myanmar         ne: Nepali          \n"
                                "nl: Dutch          no: Norwegian       pl: Polish          \n"
                                "pt: Portuguese     ro: Romanian        ru: Russian         \n"
                                "si: Sinhala        sk: Slovak          sq: Albanian        \n"
                                "sr: Serbian        su: Sundanese       sv: Swedish         \n"
                                "sw: Swahili        ta: Tamil           te: Telugu          \n"
                                "th: Thai           tl: Filipino        tr: Turkish         \n"
                                "uk: Ukrainian      vi: Vietnamese      zh: Chinese         \n"
                                "```",
                    colour=discord.Colour.blue()
                    )],
                label="Supported Languages",
                use_default_buttons=False,
            ),
            pages.PageGroup(
                pages=[discord.Embed(
                    title="Supported Male/Female Voice",
                    description="Usage example: `;jp_male Konnichiwa!`/`;jp_female Konnichiwa!`"
                                "\n\nSupported languages:\n"
                                "```"
                                "ar: Arabic         bn: Bengali         da: Danish          \n"
                                "nl: Dutch          en-AU: English(AU)  en-IN: English(IN)  \n"
                                "uk: English(UK)    us: English(US)     ph: Filipino        \n"
                                "fr: French         de: Germany         gu: Gujarati        \n"
                                "hi: Hindi          id: Indonesian      it: Italy           \n"
                                "jp: Japanese       kn: Kannada         ko: Korean          \n"
                                "ms: Malay          ml: Malayalam       cmn-CN: Chinese     \n"
                                "cmn-TW: Taiwanese  no: Norway          pl: Polish          \n"
                                "pt: Portuguese     pa:Punjabi          ru: Russia          \n"
                                "es: Spanish        sv: Swedish         ta: Tamil           \n"
                                "tr: Turksih        vi: Vietnamese                          \n"
                                "```",
                    colour=discord.Colour.blue()
                    )],
                label="Supported Male/Female Voice",
                use_default_buttons=False,
            ),
        ]
        return self._help
