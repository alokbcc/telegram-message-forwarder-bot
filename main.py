from os import environ
from pyrogram import Client, filters


tg_session = "AQBoRuUvo0f8yhwuaVVvP-5APG7fwmUV5leFXBlJWc1e0eNUk1bmzZzrk0BcvluAvcBN7Qaz0B1X2qBkKr74nZ3iF2gOvc2KOfRwSCNxGobnLRbNLZPyyA7OP8y1eYkiCUypEUidT2D_4aNXw8ca3U_LgeQjwVfpmwqg4MiBslcbel0NaJCZx2L060BOxVje5TmBXdE1WBUZt-rd8zO_etcFMFZPqawL-sqmbY8UeUrwO4RwHb4Kvv9nFqcEKBevX_1vNeekcUE1Kmzu9DkM6P_e80MaYSrIwCn2H__bwgnuQsxAYBmTb_hIy_NDZVscAxGSV-f8xpKXwf77bzleQuO8VMiVmgA"
api_id = "2634132"   # Get it from my.telegram.org
api_hash = "677e079dcc7e6a14dbeecfd2bf7bae11"   # Get it from my.telegram.org
api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
#bot_token = environ["BOT_TOKEN"]
tg_session = environ.get("TELEGRAM_SESSION", None)
from_chats = list(set(int(x) for x in environ.get("FROM_CHATS").split()))
to_chats = list(set(int(x) for x in environ.get("TO_CHATS").split()))
advance_config = environ.get("ADVANCE_CONFIG", None)

if tg_session:
    app = Client(tg_session, api_id, api_hash)
#else:
 #   app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

if advance_config:
    
    print("Advance Configures detected...")
    from_chats = []
    chats_data = {}
    for chats in advance_config.split(","):
        chat = chats.strip().split()
        chats_data[int(chat[0])] = int(chat[1])
    if not int(chat[0]) in from_chats:
        from_chats.append(int(chat[0]))
    print(from_chats)
    print(chats_data)
    

@app.on_message(filters.chat(from_chats) & filters.video)
def work(client, message):
    
    if advance_config:
        try:
            message.copy(chats_data[int(message.chat.id)])
        except Exception as e:
            print(e)
    else:
        try:
            for chat in to_chats:
                message.copy(chat)
        except Exception as e:
            print(e)

app.run()
