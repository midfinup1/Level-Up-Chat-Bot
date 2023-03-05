import logging


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "5818761953:AAEVwWY4agQmQyVHCUYra8S5MN4crl7chGQ"

buttons = {
    "poster": InlineKeyboardButton("Афиша", callback_data="poster"),
    "support": InlineKeyboardButton("Поддержка", callback_data="support"),
    "about_us": InlineKeyboardButton("О нас", callback_data="about_us"),
    "other_funcs": InlineKeyboardButton("Другое", callback_data="other_funcs"),
    "main": InlineKeyboardButton("🏠На Главную", callback_data="main"),
    "buy_ticket": InlineKeyboardButton("Купить Билет", callback_data="buy_ticket"),
    "about_event": InlineKeyboardButton("О мероприятии", callback_data="about_event"),
    "back_to_poster": InlineKeyboardButton("↩Назад", callback_data="back_to_poster")
}

texts = {
    "main": "Привет! \n blabla\t\tblabla\t\tblabla\t\tblabla\t\tblablablablablabla.\n :)",
    "support": "***Поддержим еблана👍***",
    "about_us": "***Информация про КБрд***",
    "poster": "***Афиша КБрд***",
    "buy_ticket": "***Операция покупки билета***",
    "about_event": "***О мероприятии***",
    "other_funcs": "ТУТ ПУСТО ЁПТА"
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            buttons["poster"]
        ],
        [
            buttons["support"],
            buttons["about_us"]
        ],
        [
            buttons["back_to_poster"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(texts["main"], reply_markup=reply_markup)


async def main_page(query) -> None:
    keyboard = [
        [
            buttons["poster"]
        ],
        [
            buttons["support"],
            buttons["about_us"]
        ],
        [
            buttons["back_to_poster"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["main"], reply_markup=reply_markup)


async def support(query) -> None:
    keyboard = [
        [
            buttons["main"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["support"], reply_markup=reply_markup)


async def about_us(query) -> None:
    keyboard = [
        [
            buttons["main"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["about_us"], reply_markup=reply_markup)


async def poster(query) -> None:
    keyboard = [
        [
            buttons["buy_ticket"]
        ],
        [
            buttons["about_event"]
        ],
        [
            buttons["main"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["poster"], reply_markup=reply_markup)


async def buy_ticket(query) -> None:
    keyboard = [
        [
            buttons["back_to_poster"]
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["buy_ticket"], reply_markup=reply_markup)


async def event_info(query) -> None:
    keyboard = [
        [
            buttons["back_to_poster"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["about_event"], reply_markup=reply_markup)


async def other_funcs(query) -> None:
    keyboard = [
        [
            buttons["main"]
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text(texts["other_funcs"], reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "about_us":
        await about_us(query)
    if query.data == "main":
        await main_page(query)
    if query.data == "poster":
        await poster(query)
    if query.data == "support":
        await support(query)
    if query.data == "buy_ticket":
        await buy_ticket(query)
    if query.data == "about_event":
        await event_info(query)
    if query.data == "back_to_poster":
        await poster(query)
    if query.data == "other_funcs":
        await other_funcs(query)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bombastick")


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()


if __name__ == "__main__":
    main()
