from pyrogram import filters
from pyrogram.types import Message

from FallenMusic import app, pytgcalls
from FallenMusic.Helpers import admin_check, close_key, is_streaming, stream_on


@app.on_message(filters.command(["resume"]) & filters.group)
@admin_check
async def res_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if await is_streaming(message.chat.id):
        return await message.reply_text("Saxlanıldı")
    await stream_on(message.chat.id)
    await pytgcalls.resume_stream(message.chat.id)
    return await message.reply_text(
        text=f"{message.from_user.mention} **tərəfindən davam edildi",
        reply_markup=close_key,
    )
