import core.TelegramCloudConfig as config
from telethon.tl import functions
import json

# change login define
def change_login(api_id: str, api_hash: str) -> None:
    """This function changing login data"""
    with open(config.PATH_TO_LOGIN, "w") as JSON:
        json.dump({'TelegramCloudLogin': {'api_id': api_id, 'api_hash': api_hash}}, JSON)

# dave channel name
def save_channel_name(channel_name: str) -> None:
    """This is function save user custom channel name"""
    with open(config.PATH_TO_CHANNEL, "w") as JSON:
        json.dump({"ChannelName": channel_name}, JSON)
# save channel id
def save_channel_id(channel_id: str) -> None:
    """This is function append channel id"""
    channel = json.load(open(config.PATH_TO_CHANNEL, "r"))
    channel["ChannelId"] = channel_id
    with open(config.PATH_TO_CHANNEL, "w") as JSON:
        json.dump(channel, JSON)  
# main function
def _telegramcloud__init__(client):
    # check channel.json
    try: channel = json.load(open(config.PATH_TO_CHANNEL, "r"))
    except:
        save_channel_name(input("TelegramCloud channel_name(your custom name): "))
        channel = json.load(open(config.PATH_TO_CHANNEL, "r"))

    _dialogs = []
    for i in client.iter_dialogs():
        _dialogs.append(i.title)
        if i.title == channel["ChannelName"]:
            save_channel_id(str(i.id))
    if channel["ChannelName"] not in _dialogs:
        # create channel
        client(functions.channels.CreateChannelRequest(
            title=channel["ChannelName"],
            about=config.CHANNEL_DESCRIPTION
        ))
        for i in client.iter_dialogs():
            if i.title == channel["ChannelName"]:
                save_channel_id(str(i.id))