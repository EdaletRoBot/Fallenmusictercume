from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✖️ Bağla", callback_data="close")]]
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
            text="➕ Qrupa Əlavə Et ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="📚 Bot Əmrləri", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="📢 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💬 Söhbət Qrupu", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="✅ Rəsmi Kanal", url="https://t.me/Rahid_44"
        ),
        InlineKeyboardButton(text="👨🏻‍💻 Bot Sahibi", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="➕ Qrupa Əlavə Et ➕",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="📢 Kanal", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💬 Söhbət Qrupu", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="✅ Rəsmi Kanal", url="hhttps://t.me/Rahid_44"
        ),
        InlineKeyboardButton(text="👨🏻‍💻 Bot Sahibi", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="👥 Hərkəs Üçün Əmrlər",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="📑 Sudo Əmrləri", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="👨🏻‍💻 Sahib Əmrləri", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="🔙 Geri", callback_data="fallen_home"),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="💬 Söhbət Qrupu", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="🔙 Geri", callback_data="fallen_help"),
        InlineKeyboardButton(text="✖️ Bağla", callback_data="close"),
    ],
]
