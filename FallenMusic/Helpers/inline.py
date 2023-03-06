from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="𝄞 Bağlayır 𝄞", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="✙ Qrupa Əlavə Et ✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="📚 Kömək və Əmrlər 📚", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="🗣 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🚀 Dəstək", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 Mənbə", url="https://github.com/RaviVeyi"
        ),
        InlineKeyboardButton(text=" İnkişaf etdirici ", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="✙ Qrupa Əlavə Et ✙",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="🗣 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="🚀 Dəstək", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💡 Mənbə", url="https://github.com/RaviVeyi"
        ),
        InlineKeyboardButton(text="☠ İnkişaf etdirici", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="👥 Hər kəs",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="📑 Sudo", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="🗃 Sahibi", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="◅ Geri", callback_data="fallen_home"),
        InlineKeyboardButton(text="✘ Bağlayır", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="🚀 Dəstək", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="◅ Geri", callback_data="fallen_help"),
        InlineKeyboardButton(text="✘ Bağlayır", callback_data="close"),
    ],
]
