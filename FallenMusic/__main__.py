import asyncio
import importlib
import os

from pyrogram import idle

from FallenMusic import (
    ASS_ID,
    ASS_NAME,
    ASS_USERNAME,
    BOT_ID,
    BOT_NAME,
    BOT_USERNAME,
    LOGGER,
    SUNAME,
    app,
    app2,
    pytgcalls,
)
from FallenMusic.Modules import ALL_MODULES


async def fallen_startup():
    LOGGER.info("[•] Modulların yüklənməsi...")
    for module in ALL_MODULES:
        importlib.import_module("FallenMusic.Modules." + module)
    LOGGER.info(f"[•] Yükləndi {len(ALL_MODULES)} Modullar.")

    LOGGER.info("[•] Yenilənən Kataloqlar...")
    if "downloads" not in os.listdir():
        os.mkdir("downloads")
    if "cache" not in os.listdir():
        os.mkdir("cache")
    LOGGER.info("[•] Kataloqlar Yenilənib.")

    try:
        await app.send_message(
            SUNAME,
            f"Rahid Music ♫︎\n\n𖢵 ID: `{BOT_ID}`\n𖢵 Ad: {BOT_NAME}\n𖢵 istifadəçi adı: @{BOT_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{BOT_NAME} ünvanına mesaj göndərmək alınmadı @{SUNAME}, zəhmət olmasa gedin yoxlayın."
        )

    try:
        await app2.send_message(
            SUNAME,
            f"✯ Rahid Music Bot Assistent ✯\n\n𖢵 ID: `{ASS_ID}`\n𖢵 Ad: {ASS_NAME}\n𖢵 istifadəçi adı: @{ASS_USERNAME}",
        )
    except:
        LOGGER.error(
            f"{ASS_NAME} ünvanına mesaj göndərmək alınmadı @{SUNAME}, zəhmət olmasa gedin yoxlayın."
        )

    await app2.send_message(BOT_USERNAME, "/start")

    LOGGER.info(f"[•] Bot kimi başladı {BOT_NAME}.")
    LOGGER.info(f"[•] Assistent Başladı {ASS_NAME}.")

    LOGGER.info(
        "[•] \x53\x74\x61\x72\x74\x69\x6e\x67\x20\x50\x79\x54\x67\x43\x61\x6c\x6c\x73\x20\x43\x6c\x69\x65\x6e\x74\x2e\x2e\x2e"
    )
    await pytgcalls.start()
    await idle()


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fallen_startup())
    LOGGER.error("Rahis musiqi botu dayandı.")
