import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, InputMedia, KeyboardButton, \
    ReplyKeyboardMarkup, InputMediaPhoto, Message
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes
from VK import get_description

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "5818761953:AAEVwWY4agQmQyVHCUYra8S5MN4crl7chGQ"
message_id_to_delete = None
application = None
chat_id = 0


class Sections:
    def __init__(self, text, button_text, media, callback_data):
        self.text = text
        self.button = InlineKeyboardButton(text=button_text, callback_data=callback_data)
        self.media = media
        self.callback_data = callback_data


image = "https://sun9-12.userapi.com/impg/YHPxT6bJAK7Eke2Q183w1C1PibrSqyL-Vdfw4w/-MlmYzuhHjg.jpg?size=1684x1190&quality=95&sign=d05299b454b12cdfe10281e412e3ccb6&type=album"
rules = Sections("", "Rules", image, "rules")

text = 'Привет, мы компьютерный клуб Level Up в Новосибирске.\nМы транслируем ценности, которые пришли к нам за годы ' \
       'работы — мы создаем уют и комфорт для твоей игры, мы — это дружелюбное комьюнити с одной целью.\n\nТвой ' \
       'комфорт мы продумали до мелочей: \n✅ Качественная техника. Профессиональная периферия от наших хороших друзей ' \
       'Logitech. \n✅ Дружелюбный компетентный персонал.\n✅ Помещение. Большая квадратура (250м²), высокие потолки и ' \
       'самобытный дизайн.\n✅ Хорошая вентиляция. Циркуляции большого объема воздуха в помещении и благоприятная ' \
       'температура.\n✅ Зона отдыха, включающая в себя кальяны и приставки.\n✅ Бар с большим выбором энергетиков и ' \
       'снеков. '
image = "https://sun9-5.userapi.com/impg/PqMZCV3oLCC02jmNHnxA7UTeq8rMRF4vD2i4fQ/amJsE6aqZKk.jpg?size=2400x2400&quality=95&sign=950d8b5062183aa852c34e843a33bab7&type=album"
welcome = Sections(text, "Main", image, "main")

image1 = "https://sun9-59.userapi.com/impg/8d6m9L_FpJryVvRdvApRnrxgh317XAFLiPCGAw/ujulo0XD8-g.jpg?size=1080x1920&quality=96&sign=002c29bc6b75be6792b133383c4abf27&type=album"
image2 = "https://sun9-41.userapi.com/impg/phNOUEvIg_fLB_3EY-GNRbPenAFjCb8DJvb1vA/TfyOS71-Tt0.jpg?size=1081x1920&quality=96&sign=1dd85bbbf0dbcdfc60cb8be473c42470&type=album"
components = Sections("Control Menu IS HERE!", "Components", [image1, image2], "components")

image1 = 'https://sun9-3.userapi.com/impg/PDQfTxKGhqFC07qsLEbKl6nES6g1u-aHA37ArA/kUPWAyeyle4.jpg?size=1080x1920&quality=96&sign=e29c4c7fbdb8705d8b03b9a48b58ace5&type=album'
image2 = 'https://sun9-33.userapi.com/impg/r2cnGVJuz4S2H5jU7k6lvl0NfwVgdChMA6tiEw/YgXPOa033Wk.jpg?size=1080x1920&quality=96&sign=8c3aa67db9ddfd2de7665781f3827656&type=album'
image3 = 'https://sun9-56.userapi.com/impg/PQyTuLZHBaGtalGn1ZS8co2Q9ZEjiuuehr9VEA/A8L-GRAPDaE.jpg?size=1080x1920&quality=96&sign=7ccf91c696395c94eb31d107582d4d50&type=album'
games = Sections("Control Menu IS HERE!", "Games", [image1, image2, image3], "games")

image1 = 'https://sun9-63.userapi.com/impg/vJXdIk8X_GEMFkDbaVFKAAB9bkQ6w7iFvlbMDA/1nC_WTEz8v0.jpg?size=1080x1920&quality=96&sign=fa776607a02ee6c409db230486d04d2b&type=album'
image2 = 'https://sun9-39.userapi.com/impg/xX-rL-hVrJA1dYExLPnqPI659X-VlQaulDo4jg/WBQvU8UKVAE.jpg?size=1080x1920&quality=96&sign=c2e7af0366d2a5207a0607b52b4f1ef5&type=album'
image3 = 'https://sun9-66.userapi.com/impg/iPERMjOfTP6musEuUgRTOvr4GLTPXD8tfR61MQ/WrmOjKrHdbA.jpg?size=1079x1920&quality=96&sign=5830185b3f232f39da5c0e79d3b8b63d&type=album'
image4 = 'https://sun9-64.userapi.com/impg/6YAEzkOCEAaaco472ZpqRrlpKxqX9ieJ_u6jcw/-RvdGGXbibE.jpg?size=1240x1754&quality=95&sign=53a385aaa9a764b71b2eba70d959fca7&type=album'
image5 = 'https://sun9-75.userapi.com/impg/yZhKkh_Ij5TwxAFvT9_hhaSf_IXDxG1njJLGRg/r63Icb3-TdU.jpg?size=1240x1754&quality=95&sign=76e790debf4db231d5cf594feaf02e9f&type=album'
image6 = 'https://sun9-67.userapi.com/impg/QwnM4SSQAkLv2rPx34CRfmrrM-iX21I4C9BDgw/m9wy3qSL5PM.jpg?size=1240x1754&quality=95&sign=970aba1ab3d485027a31f1cc57cd2806&type=album'
prices = Sections('Control menu IS HERE!', 'Prices', [image1, image2, image3, image4, image5, image6], 'prices')

image1 = ''
image2 = ''
image3 = ''
image4 = ''
image5 = ''
image6 = ''
image7 = ''
image8 = ''
image9 = ''
image10 = ''
interior = Sections('Control menu IS HERE!!', 'Interior', [image1, image2, image3, image4, image5, image6, image7,
                                                           image8, image9, image10], 'interior')

text = 'В нашей арене мы предлагаем тебе альтернативный выбор зон в зависимости от твоих предпочтений: \n2 этажа ' \
       'посадочных мест. Нижний более темный и тихий. Верхний светлый с быстрым доступом к стойке администратора и ' \
       'лаундж зоны, где в основном происходит движ.\nЗона Подиум. Идеально для игры командой.\nВИП-комната. С ' \
       'улучшенным железом и обособленностью от других игроков. \nВИП-буткемп. Новейшие ВИП-комнаты, с самым мощным ' \
       'железом, удобными столами/креслами и новыми премиальными девайсами.\n\nВ Level Up есть только ТЫ и ТВОЯ ' \
       'КАТКА!\n\n👉🏼 полное погружение в игру;\n👉🏼 приобретение игрового опыта с единомышленниками;\n👉🏼 выход ' \
       'эмоций.\n\nСконцентрируйся на игре, об остальном позаботимся мы. '
video1 = 'https://vk.com/video-187335255_456239137'
info = Sections(text, 'Info', video1, 'info')

support = Sections('Support Text', 'Support', [], 'support')

book = Sections('Book Text', 'Book', [], 'book')

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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await update.message.reply_photo(
        photo=welcome.media,
        caption=welcome.text,
        reply_markup=reply_markup
    )


async def send_welcome(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=welcome.text
        ),
        reply_markup=reply_markup
    )


async def send_rules(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=rules.media,
            media_type="photo",
            caption=rules.text
        ),
        reply_markup=reply_markup
    )


async def send_components(query) -> None:
    global message_id_to_delete
    message_id_to_delete = 1
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=components.text
        ),
        reply_markup=reply_markup
    )
    await query.message.reply_media_group(
        media=[
            InputMedia(
                media=components.media[0],
                media_type="photo",
            ),
            InputMedia(
                media=components.media[1],
                media_type="photo",
            )
        ]
    )


async def send_games(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=games.text
        ),
        reply_markup=reply_markup
    )
    await query.message.reply_media_group(
        media=[
            InputMedia(
                media=games.media[0],
                media_type="photo",
            ),
            InputMedia(
                media=games.media[1],
                media_type="photo",
            ),
            InputMedia(
                media=games.media[2],
                media_type="photo",
            )
        ]
    )


async def send_prices(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=prices.text
        ),
        reply_markup=reply_markup
    )
    await query.message.reply_media_group(
        media=[
            InputMedia(
                media=prices.media[0],
                media_type="photo",
            ),
            InputMedia(
                media=prices.media[1],
                media_type="photo",
            ),
            InputMedia(
                media=prices.media[2],
                media_type="photo",
            ),
            InputMedia(
                media=prices.media[3],
                media_type="photo",
            ),
            InputMedia(
                media=prices.media[4],
                media_type="photo",
            ),
            InputMedia(
                media=prices.media[5],
                media_type="photo",
            )
        ]
    )


async def send_interior(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=interior.text
        ),
        reply_markup=reply_markup
    )
    await query.message.reply_media_group(
        media=[
            InputMedia(
                media=interior.media[0],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[1],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[2],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[3],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[4],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[5],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[6],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[7],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[8],
                media_type="photo",
            ),
            InputMedia(
                media=interior.media[9],
                media_type="photo",
            )
        ]
    )


async def send_info(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=info.media,
            media_type="video",
            caption=info.text
        ),
        reply_markup=reply_markup
    )


async def send_support(query) -> None:
    reply_markup = InlineKeyboardMarkup(default_keyboard)
    await query.message.edit_media(
        media=InputMedia(
            media=welcome.media,
            media_type="photo",
            caption=support.text
        ),
        reply_markup=reply_markup
    )


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


async def callback_query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global message_id_to_delete
    query = update.callback_query
    # if message_id_to_delete:
    #     application.bot.delete_message(chat_id=, message_id=message_id_to_delete)
    #     message_id_to_delete = None
    await query.answer()

    if query.data == welcome.callback_data:
        await send_welcome(query)

    if query.data == rules.callback_data:
        await send_rules(query)

    if query.data == components.callback_data:
        await send_components(query)

    if query.data == games.callback_data:
        await send_games(query)

    if query.data == prices.callback_data:
        await send_prices(query)

    if query.data == interior.callback_data:
        await send_interior(query)

    if query.data == info.callback_data:
        await send_info(query)

    if query.data == support.callback_data:
        await send_support(query)

    if query.data == book.callback_data:
        await send_booking(query)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bombastick")


def main() -> None:
    global application
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(callback_query))
    application.add_handler(CommandHandler("help", help_command))

    application.run_polling()


if __name__ == "__main__":
    main()
