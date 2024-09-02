import os
from pprint import pprint

from telethon import TelegramClient
from telethon.tl.types import User


async def test_hello(client):
    await client.send_message('me', 'Hello, myself!')


async def where_admin(client):
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        if not isinstance(dialog.entity, User):
            if dialog.entity.admin_rights is not None:
                 d = dialog.entity.to_dict()
                 print(f"- {d['title']} ({d['id']})")
                 pprint(dialog.entity.admin_rights.to_dict())
                 print()

    
async def main(client):
    await test_hello(client)
    await where_admin(client)


if __name__ == "__main__":
    api_id   = os.getenv("TG_API_ID")
    api_hash = os.getenv("TG_API_HASH")
    with TelegramClient('anon', api_id, api_hash) as client:
        client.loop.run_until_complete(main(client))
