from pathlib import Path 
from telethon.sync import TelegramClient
api_id = API_ID
api_hash =  API_HASH 
phone_number = PHONE_NUMBER
client = TelegramClient(SESSION_NAME, api_id, api_hash)

async def main():
    # send yourself a massge to check if it's work
    await client.send_message('me', 'Hello, myself!')
    groupid = -1 # Group ID to check


   
    group_name = input("enter the group name to search: ").lower()
    async for dialog in client.iter_dialogs():
        if(dialog.name.lower() ==  group_name):
            groupid = dialog.id
            break




    if groupid == -1:
        print("Didn't find any group with that name")
        return
    #number of messages you want to download 
    i = 0
    path =Path(input("what path do download the files to:"))
    if not path.is_dir():
       path.mkdir(exist_ok=True)
       print(f"Didn't find any directory named {path}. Creating one and downloading")
    async for message in client.iter_messages(groupid):
        print(message.id, message.text)

        if message.video:
            path_to_download = await message.download_media(path)
            print('File saved to', path_to_download)  # printed after download is don
        if i == 10:
             break
        i +=1 
with client:
      client.loop.run_until_complete(main())
