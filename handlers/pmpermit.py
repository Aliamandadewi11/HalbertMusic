
from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Halo, Saya adalah layanan asisten musik.\n\n ❗️ Rules:\n   - Ganteng dulu kek @mrismanaziz\n   - Jangan spam Lagu biar ga error \n\n 👉 **KIRIM LINK UNDANGAN GRUP ATAU NAMA PENGGUNA JIKA USERBOT TIDAK DAPAT BERGABUNG DENGAN GRUP ANDA.**\n\n ⚠️ Disclamer: Jika Anda mengirim pesan di sini berarti admin akan melihat pesan Anda dan bergabung dengan obrolan.\n    - Jangan menambahkan userbot ini ke grup private.\n\n")
  return                        
