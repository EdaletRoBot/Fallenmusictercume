import time
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from FallenMusic import BOT_NAME, StartTime, app
from FallenMusic.Helpers import get_readable_time


@app.on_message(filters.command("ping"))
async def ping_fallen(_, message: Message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG, caption=f"{BOT_NAME} ping edir..."
    )
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    start = datetime.now()
    resp = (datetime.now() - start).microseconds / 1000
    uptime = get_readable_time((upt))

    await hmm.edit_text(
        f"""👨🏻‍💻 Rahid: `{resp}ᴍs`

<b><u>{BOT_NAME} Sistem Statistikası:</u></b>

๏ **İş vaxtı:** {uptime}
๏ **Ram:** {mem}
๏ **CPU:** {cpu}
๏ **Disk:** {disk}""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("💬 Söhbət Qrupu", url=config.SUPPORT_CHAT),
                    InlineKeyboardButton(
                        "👨🏻‍💻 Bot Sahibi",
                        url="https://t.me/Rahid_7",
                    ),
                ],
            ]
        ),
    )
