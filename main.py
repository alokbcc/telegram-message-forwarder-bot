from os import environ
from pyrogram import Client, filters

api_id = int(environ["API_ID"])
api_hash = environ["API_HASH"]
bot_token =None # environ["BOT_TOKEN"]
tg_session = environ.get("TELEGRAM_SESSION", None)
from_chats =None # list(set(int(x) for x in environ.get("FROM_CHATS").split()))
to_chats =None # list(set(int(x) for x in environ.get("TO_CHATS").split()))
#advance_config = [-1001412417782,-1001422216928,-1001497555467,-1001468474555,-1001415731712,-1001423340146]#environ.get("ADVANCE_CONFIG", None)

if tg_session:
  app = Client(tg_session, api_id, api_hash)
else:
  app = Client(":memory:", api_id, api_hash, bot_token=bot_token)

if True:
  from_chats = [-1001412417782, -1001497555467, -1001415731712]
  chats_data = {-1001412417782 : -1001422216928 , -1001497555467 : -1001468474555 , -1001415731712 : -1001423340146}


@app.on_message(filters.chat(from_chats) & filters.incoming)
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
