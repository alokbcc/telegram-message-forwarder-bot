from os import environ
from pyrogram import Client, filters

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token = environ["BOT_TOKEN"]
tg_session =None #environ.get("TELEGRAM_SESSION", None)
from_chats =None # list(set(int(x) for x in environ.get("FROM_CHATS").split()))
to_chats =None # list(set(int(x) for x in environ.get("TO_CHATS").split()))
#advance_config = [-1001412417782,-1001422216928,-1001497555467,-1001468474555,-1001415731712,-1001423340146]#environ.get("ADVANCE_CONFIG", None)

  
#app = Client(session_name='fword',api_id=get_val("API_ID"), api_hash=get_val("API_HASH"), bot_token=get_val("BOT_TOKEN"))

app = Client(session_name='fword', api_id=api_id, api_hash=api_hash, bot_token=bot_token)

if True:
  from_chats = [-1001415731712,-1001412417782,-1001152269824,-1001315177838,-1001459395259]
  chats_data = {-1001415731712: -1001423340146,-1001412417782: -1001422216928,-1001152269824: -1001318982369,-1001315177838: -1001269480046,-1001459395259: -1001451236225}


@app.on_message(filters.chat(from_chats) & filters.video)
def work(client, message):
    if True:
      try:
        message.copy(chats_data[message.chat.id])
      except Exception as e:
        print(e)
    else:
      try:
        for chat in to_chats:
          message.copy(chat)
      except Exception as e:
        print(e)

app.run()
