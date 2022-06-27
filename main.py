from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from news import LK
from config import ENVIRONMENT


bot = Client(
    "news",
    api_id=ENVIRONMENT.API_ID,
    api_hash=ENVIRONMENT.API_HASH, 
    bot_token=ENVIRONMENT.BOT_TOKEN
)

@bot.on_message(filters.command("start"))
async def start(_, m : Message):
    await m.reply_text("I'm Alive")

@bot.on_message(filters.command("news"))
async def news(_, m : Message):
    lol = await m.reply_text("processing...")
    nw = LK()
    await lol.delete()
    await m.reply_photo(nw[0]['img_url'], caption=f"**📰 {nw[0]['Title']}**\n\n✍️ {nw[0]['Description']}.__[See more...]({nw[0]['Link']})__\n\n📅 {nw[0]['Date']}\n\n🔰 Powered By 🔰 :- newswire.lk ", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("📰 View in site 📰", url=nw[0]['Link'])
            ]
        ]
    ))

print("Hemlo")
bot.run()
