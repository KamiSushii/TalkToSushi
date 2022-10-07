class MissingGuild(Exception):
    pass

class EmptyQueue(Exception):
    pass

class Queue():
    def __init__(self):
        self.queue = {}


    def is_guild_in_queue(self, guild_id):
        if guild_id in self.queue: return True
        else: return False


    def add_text(self, guild_id, text):
        if not self.is_guild_in_queue(guild_id):
            self.queue[guild_id] = []

        self.queue[guild_id].append(text)


    def get_next(self, guild_id):
        if self.queue_len(guild_id) is not None:
            return self.queue[guild_id].pop(0)
        else: raise EmptyQueue


    def queue_len(self, guild_id):
        try:
            return len(self.queue[guild_id])
        except: return None


    def destroy(self, guild_id):
        self.queue.pop(guild_id)