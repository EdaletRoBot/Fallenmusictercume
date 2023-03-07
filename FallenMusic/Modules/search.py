from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtube_search import YoutubeSearch

from FallenMusic import app


@app.on_message(filters.command(["search"]))
async def ytsearch(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    try:
        if len(message.command) < 2:
            return await message.reply_text("Axtarış etmək üçün nəsə yazın")
        query = message.text.split(None, 1)[1]
        m = await message.reply_text("**🔍 Göndərirəm...**")
        results = YoutubeSearch(query, max_results=4).to_dict()
        i = 0
        text = ""
        while i < 4:
            text += f"🏷️ Başlıq: {results[i]['title']}\n"
            text += f"⏳ Müddət: `{results[i]['duration']}`\n"
            text += f"👀 Baxış: `{results[i]['views']}`\n"
            text += f"📢 Kanal: {results[i]['channel']}\n"
            text += f"🔗 Link: https://youtube.com{results[i]['url_suffix']}\n\n"
            i += 1
        key = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="✖️ Bağla",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await m.edit_text(
            text=text,
            reply_markup=key,
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply_text(str(e))
