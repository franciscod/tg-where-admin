# tg-where-admin

a tool to get a list of telegram groups/channels that you have admin rights in

uses [Telethon](https://docs.telethon.dev/en/stable/index.html)

inspired by [a SO answer from its author](https://stackoverflow.com/a/76094988)


## authentication

get `API_ID` and `API_HASH` from https://my.telegram.org

from [Telethon doc](https://docs.telethon.dev/en/stable/basic/signing-in.html):

    > Signing In

    > 1. Login to your Telegram account with the phone number of the developer 
         account to use.
    > 2. Click under API Development tools.
    > 3. A Create new application window will appear. Fill in your application 
         details. There is no need to enter any URL, and only the first two 
         fields (App title and Short name) can currently be changed later.
    > 4. Click on Create application at the end. Remember that your API hash 
         is secret and Telegram won’t let you revoke it. Don’t post it anywhere!

## tip

when done, you can revoke your session from the "Devices" menu in telegram
