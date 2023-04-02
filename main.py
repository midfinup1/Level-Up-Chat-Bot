import logging

from telegram import InlineKeyboardMarkup, Update, InputMedia
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from sections_init import *

# Enable logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "5818761953:AAEVwWY4agQmQyVHCUYra8S5MN4crl7chGQ"
message_to_delete = None


default_keyboard = [
    [
        rules.button,
        components.button
    ],
    [
        games.button,
        prices.button
    ],
    [
        interior.button,
        info.button
    ],
    [
        book.button,
        support.button
    ]
]


async def start(update: Update) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await update.message.reply_photo(
        photo=welcome.media,
        caption=welcome.text,
        reply_markup=reply_markup
    )


async def send_section(query, section) -> None:
    media = []
    for item in section.media:
        media.append(InputMedia(media=item, media_type='photo'))
    message = await query.message.reply_media_group(
        media=media,
        caption=section.text
    )
    return message


async def send_booking(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=book.text
        ),
        reply_markup=reply_markup
    )


async def callback_query(update: Update) -> None:
    global message_to_delete
    query = update.callback_query
    if message_to_delete:
        await delete_message(message_to_delete)
        message_to_delete = None
    await query.answer()

    match query.data:
        case rules.callback_data:
            section = rules
        case components.callback_data:
            section = components
        case games.callback_data:
            section = games
        case prices.callback_data:
            section = prices
        case interior.callback_data:
            section = interior
        case support.callback_data:
            section = support
        case info.callback_data:
            section = info
    message_to_delete = await send_section(query, section)

    if query.data == book.callback_data:
        await send_booking(query)


async def delete_message(message):
    for item in message:
        await item.delete()


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(callback_query))

    application.run_polling()


if __name__ == "__main__":
    main()
