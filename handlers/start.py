from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hai {message.from_user.first_name}!</b>

Aku adalah Star Music Bot, bot sumber terbuka yang memungkinkan Anda memutar musik di Grup Telegram Anda.
Tidak mengetahui cara memakainya? Baca panduan pemakaian agar langsung memahami tanpa bertanya!
━━━━━━━━━━━━━━━━━━━━━━
Bot : @StarMusicPlay_bot - Asisten : @StarzMusicAssistant
Dikelola oleh ✨ [Rezy](t.me/ItsmeAlsya). Thanks! 
        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Channel Support", url="https://t.me/StarMusicTelegram")
                  ],[
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/ItsmeAlsya"
                    ),
                    InlineKeyboardButton(
                        "🔉 Channel", url="https://t.me/gabutannyaumat") 
                  ],[
                    InlineKeyboardButton(
                        "📈 Official Group", url="https://t.me/Republicfriend"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/Republicfriend"
                    ),
                    InlineKeyboardButton(
                        "Owner Bot", url="https://t.me/ItsmeAlsya"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🎧 Pemutar Musik Sedang Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ Star Music⚡", url="https://t.me/ItsmeAlsya") 
                ],[
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/Republicfriend"
                    )
                ]
            ]
        )
   )
