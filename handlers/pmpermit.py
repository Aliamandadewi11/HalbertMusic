from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Alooo Guys ✨ Saya adalah **Layanan Asisten Star Music Bot.**\n\n ❗️ Rules :\n   - Biasakan Salam, amanat dari [Owner](t.me/ItsmeAlsya) \n   - Jangan spam pemutaran lagu agar bot tidak error \n\n **Note :** Kirim link undangan Grup atau Username Grup jika Userbot/Asisten tidak dapat bergabung dengan Grup Anda atau yang lainnya.\n\n 🛠️ Ke [Official Group](t.me/Republicfriend) atau bisa PC ke owner [Rezy](t.me/ItsmeAlsya)\n\n")
  return                        
