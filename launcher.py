import os
from bot import TalkToSushi

TOKEN = "token here"
json = os.path.join(os.path.dirname(__file__), "key.json here")

def main():
    bot = TalkToSushi(TOKEN, json)
    bot.run()

if __name__ == '__main__':
    main()
