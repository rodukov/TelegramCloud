import json
from telethon import TelegramClient
from telethon import sync, events
import core.TelegramCloudConfig as config
import core.TelegramCloudCore as core
import argparse

parser = argparse.ArgumentParser(description='Telegram Cloud --help')
parser.add_argument("-f", "--file", help='accept file path to file')
args = parser.parse_args()

# check login.json
try: login = json.load(open(config.PATH_TO_LOGIN, "r"))
except:
    core.change_login(input("TelegramCloud api_id: "), input("TelegramCloud api_hash: "))
    login = json.load(open(config.PATH_TO_LOGIN, "r"))

client = TelegramClient(config.PATH_TO_SAVE, login["TelegramCloudLogin"]["api_id"], login["TelegramCloudLogin"]["api_hash"])
client.start()
def main():
    core._telegramcloud__init__(client)
    channel = json.load(open(config.PATH_TO_CHANNEL, "r"))
    client.send_file(channel["ChannelName"], args.file)

# run TelegramCloud
main()