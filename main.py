import logging


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "5818761953:AAEVwWY4agQmQyVHCUYra8S5MN4crl7chGQ"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Афиша", callback_data="poster"),
            InlineKeyboardButton("О нас", callback_data="about_us"),
        ],
        [
            InlineKeyboardButton("Купить билеты", callback_data="buy_ticket")
        ],
        [
            InlineKeyboardButton("ДА?", callback_data="other_funcs")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("Привет! \n blabla\t\tblabla\t\tblabla\t\tblabla\t\tblablablablablabla.\n :)", reply_markup=reply_markup)


async def main_page(query) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Афиша", callback_data="poster"),
            InlineKeyboardButton("О нас", callback_data="about_us"),
        ],
        [
            InlineKeyboardButton("Купить Билет", callback_data="buy_ticket")
        ],
        [
            InlineKeyboardButton("ДА?", callback_data="other_funcs")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("Привет! \n blabla\t\tblabla\t\tblabla\t\tblabla\t\tblablablabla\n :)", reply_markup=reply_markup)


async def about_us(query) -> None:
    keyboard = [
        [
            InlineKeyboardButton("На Главную", callback_data="main")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("***Информация про КБрд***", reply_markup=reply_markup)


async def poster(query) -> None:
    keyboard = [
        [
            InlineKeyboardButton("На Главную", callback_data="main")
        ],
        [
            InlineKeyboardButton("Купить Билет", callback_data="buy_ticket")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("***Афиша КБрд***", reply_markup=reply_markup)


async def buy_ticket(query) -> None:
    keyboard = [
        [
            InlineKeyboardButton("На Главную", callback_data="main")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("***Операция покупки билета***", reply_markup=reply_markup)


async def other_funcs(query) -> None:
    keyboard = [
        [
            InlineKeyboardButton("На Главную", callback_data="main")
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("ПИЗДА", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    if query.data == "about_us":
        await about_us(query)
    if query.data == "main":
        await main_page(query)
    if query.data == "poster":
        await poster(query)
    if query.data == "buy_ticket":
        await buy_ticket(query)
    if query.data == "other_funcs":
        await other_funcs(query)
    # await query.edit_message_text(text=f"Selected option: {query.data}")


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
