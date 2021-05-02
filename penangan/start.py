from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn

@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hai {message.from_user.first_name}!</b>

Aku adalah Lestari Musik, bot sumber terbuka yang memungkinkan Anda memutar musik di Grup Telegram Anda.
Tidak mengetahui cara memakainya? Baca panduan pemakaian agar langsung memahami tanpa bertanya!
━━━━━━━━━━━━━━━━━━━━━━
Bot : @Lestarimusik - Asisten : @LestariBotAssistant
Dikelola oleh ✨ [Manda](t.me/aamdys). Thanks! 
        """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📌 Panduan", url="https://t.me/Lestarimusik")
                  ],[
                    InlineKeyboardButton(
                        "Owner 🎶", url="https://t.me/aamdys"
                    ),
                    InlineKeyboardButton(
                        "🔉 Channel", url="https://t.me/noteshati") 
                  ],[
                    InlineKeyboardButton(
                        "📈 Official Group", url="https://t.me/familybrden"
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
                        "Official Group", url="https://t.me/familybrden"
                    ),
                    InlineKeyboardButton(
                        "Owner Bot", url="https://t.me/aamdys"
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
                        "⚡ Lestari music⚡", url="https://t.me/aamdys") 
                ],[
                    InlineKeyboardButton(
                        "Official Group", url="https://t.me/familybrden"
                    )
                ]
            ]
        )
   )
