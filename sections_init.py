from telegram import InlineKeyboardButton


class Sections:
    def __init__(self, text, button_text, media, callback_data):
        self.text = text
        self.button = InlineKeyboardButton(text=button_text, callback_data=callback_data)
        self.media = media
        self.callback_data = callback_data


image = "https://sun9-12.userapi.com/impg/YHPxT6bJAK7Eke2Q183w1C1PibrSqyL-Vdfw4w/-MlmYzuhHjg.jpg?size=1684x1190&quality=95&sign=d05299b454b12cdfe10281e412e3ccb6&type=album"
rules = Sections("", "Rules", [image], "rules")

text_ = 'Привет, мы компьютерный клуб Level Up в Новосибирске.\nМы транслируем ценности, которые пришли к нам за годы ' \
       'работы — мы создаем уют и комфорт для твоей игры, мы — это дружелюбное комьюнити с одной целью.\n\nТвой ' \
       'комфорт мы продумали до мелочей: \n✅ Качественная техника. Профессиональная периферия от наших хороших друзей ' \
       'Logitech. \n✅ Дружелюбный компетентный персонал.\n✅ Помещение. Большая квадратура (250м²), высокие потолки и ' \
       'самобытный дизайн.\n✅ Хорошая вентиляция. Циркуляции большого объема воздуха в помещении и благоприятная ' \
       'температура.\n✅ Зона отдыха, включающая в себя кальяны и приставки.\n✅ Бар с большим выбором энергетиков и ' \
       'снеков. '
image = "https://sun9-5.userapi.com/impg/PqMZCV3oLCC02jmNHnxA7UTeq8rMRF4vD2i4fQ/amJsE6aqZKk.jpg?size=2400x2400&quality=95&sign=950d8b5062183aa852c34e843a33bab7&type=album"
welcome = Sections(text_, "Main", image, "main")

image1 = "https://sun9-59.userapi.com/impg/8d6m9L_FpJryVvRdvApRnrxgh317XAFLiPCGAw/ujulo0XD8-g.jpg?size=1080x1920&quality=96&sign=002c29bc6b75be6792b133383c4abf27&type=album"
image2 = "https://sun9-41.userapi.com/impg/phNOUEvIg_fLB_3EY-GNRbPenAFjCb8DJvb1vA/TfyOS71-Tt0.jpg?size=1081x1920&quality=96&sign=1dd85bbbf0dbcdfc60cb8be473c42470&type=album"
components = Sections("Control Menu IS HERE!", "Components", [image1, image2], "components")

image1 = 'https://sun9-3.userapi.com/impg/PDQfTxKGhqFC07qsLEbKl6nES6g1u-aHA37ArA/kUPWAyeyle4.jpg?size=1080x1920&quality=96&sign=e29c4c7fbdb8705d8b03b9a48b58ace5&type=album'
image2 = 'https://sun9-33.userapi.com/impg/r2cnGVJuz4S2H5jU7k6lvl0NfwVgdChMA6tiEw/YgXPOa033Wk.jpg?size=1080x1920&quality=96&sign=8c3aa67db9ddfd2de7665781f3827656&type=album'
image3 = 'https://sun9-56.userapi.com/impg/PQyTuLZHBaGtalGn1ZS8co2Q9ZEjiuuehr9VEA/A8L-GRAPDaE.jpg?size=1080x1920&quality=96&sign=7ccf91c696395c94eb31d107582d4d50&type=album'
games = Sections("Control Menu IS HERE!!", "Games", [image1, image2, image3], "games")

image1 = 'https://sun9-63.userapi.com/impg/vJXdIk8X_GEMFkDbaVFKAAB9bkQ6w7iFvlbMDA/1nC_WTEz8v0.jpg?size=1080x1920&quality=96&sign=fa776607a02ee6c409db230486d04d2b&type=album'
image2 = 'https://sun9-39.userapi.com/impg/xX-rL-hVrJA1dYExLPnqPI659X-VlQaulDo4jg/WBQvU8UKVAE.jpg?size=1080x1920&quality=96&sign=c2e7af0366d2a5207a0607b52b4f1ef5&type=album'
image3 = 'https://sun9-66.userapi.com/impg/iPERMjOfTP6musEuUgRTOvr4GLTPXD8tfR61MQ/WrmOjKrHdbA.jpg?size=1079x1920&quality=96&sign=5830185b3f232f39da5c0e79d3b8b63d&type=album'
image4 = 'https://sun9-64.userapi.com/impg/6YAEzkOCEAaaco472ZpqRrlpKxqX9ieJ_u6jcw/-RvdGGXbibE.jpg?size=1240x1754&quality=95&sign=53a385aaa9a764b71b2eba70d959fca7&type=album'
image5 = 'https://sun9-75.userapi.com/impg/yZhKkh_Ij5TwxAFvT9_hhaSf_IXDxG1njJLGRg/r63Icb3-TdU.jpg?size=1240x1754&quality=95&sign=76e790debf4db231d5cf594feaf02e9f&type=album'
image6 = 'https://sun9-67.userapi.com/impg/QwnM4SSQAkLv2rPx34CRfmrrM-iX21I4C9BDgw/m9wy3qSL5PM.jpg?size=1240x1754&quality=95&sign=970aba1ab3d485027a31f1cc57cd2806&type=album'
prices = Sections('Control menu IS HERE!!!', 'Prices', [image1, image2, image3, image4, image5, image6], 'prices')

image1 = 'https://sun9-25.userapi.com/impg/_NhVHO-C2vh6VIBR4vJ0w31rnL-cca1fsrRAag/nMTMGCWLra4.jpg?size=1920x1280&quality=96&sign=e7104592c2c67f3afad2bc24ec601412&type=album'
image2 = 'https://sun9-42.userapi.com/impg/hTeoEHc75485Mp1CXqBHmrznwRDRbQtdPRqfIw/j4FopzgKOPs.jpg?size=1920x1280&quality=96&sign=0fc255f41ac10774f26a5e921e81c864&type=album'
image3 = 'https://sun9-65.userapi.com/impg/oaXy3-I2JzLf95u30SfqYf-qfXzW2ROKpPLfKg/8Ww9rsa9zm8.jpg?size=1920x1280&quality=95&sign=b6236b18ba7435d06959672a005a6f7d&type=album'
image4 = 'https://sun9-5.userapi.com/impg/vg9tlFfPXwIDpIQZ54_38cNF4l9fFEpbD5F6gQ/evZmdJLB2qg.jpg?size=1920x1280&quality=96&sign=043201ebbc9ba7d2ae265b14d190b310&type=album'
image5 = 'https://sun9-50.userapi.com/impg/DCmzhX9p-p84dvWYr9hnwV_lj-hr23H0grsM6g/DSx-TxxJxZc.jpg?size=2560x1707&quality=95&sign=a48106fe03552ba58fa5d14d63faf1bd&type=album'
image6 = 'https://sun9-78.userapi.com/impg/eJIuQGq7ca1sdVAtD-5D3T5FZhetmqVHkBx1Ww/rGtsq2GOE1E.jpg?size=2560x1707&quality=95&sign=7b84adc47585397414446c5fa96796e7&type=album'
image7 = 'https://sun9-66.userapi.com/impg/O5b9GQZCbC9QhxkewLBbce--MYvx_W6Pi_g8sQ/fYobXEICG7M.jpg?size=2560x1707&quality=95&sign=ab70bd986aeb642cf9613007656176bb&type=album'
image8 = 'https://sun9-6.userapi.com/impg/gNxp2g8fGV3-zazNq5xvahOudjiPdO0bIvq4PQ/rGHSMu2HI2k.jpg?size=2560x1707&quality=95&sign=da61ad408c12de89f4f1965d9b84cc22&type=album'
image9 = 'https://sun9-74.userapi.com/impg/S_u0xll6tl9zTFEtMgvtL4Ok3UCzrHUdOnPPGg/Mk1kp4mdGg0.jpg?size=2560x1707&quality=95&sign=263db3b4909c326c19fd9ef613387c87&type=album'
image10 = 'https://sun9-21.userapi.com/impg/AgILiDIZ-nElV_XYreqnObwpmACCHphPhOoAEQ/CPVKBBQGWcI.jpg?size=1920x1280&quality=96&sign=55aa3b2718c1133273daf4ba2bf05773&type=album'
interior = Sections('Control menu Is HERE!!', 'Interior', [image1, image2, image3, image4, image5, image6, image7,
                                                           image8, image9, image10], 'interior')

text_ = 'В нашей арене мы предлагаем тебе альтернативный выбор зон в зависимости от твоих предпочтений: \n2 этажа ' \
       'посадочных мест. Нижний более темный и тихий. Верхний светлый с быстрым доступом к стойке администратора и ' \
       'лаундж зоны, где в основном происходит движ.\nЗона Подиум. Идеально для игры командой.\nВИП-комната. С ' \
       'улучшенным железом и обособленностью от других игроков. \nВИП-буткемп. Новейшие ВИП-комнаты, с самым мощным ' \
       'железом, удобными столами/креслами и новыми премиальными девайсами.\n\nВ Level Up есть только ТЫ и ТВОЯ ' \
       'КАТКА!\n\n👉🏼 полное погружение в игру;\n👉🏼 приобретение игрового опыта с единомышленниками;\n👉🏼 выход ' \
       'эмоций.\n\nСконцентрируйся на игре, об остальном позаботимся мы. '
video1 = 'https://vk.com/video_ext.php?oid=-187335255&id=456239137&hash=27ae861c91c5c291&__ref=vk.api&api_hash=1680261917074a0a7317b63be3e7_GIZDMMZTHA4DCNQ'
info = Sections(text_, 'Info', [video1], 'info')


image = "https://sun9-5.userapi.com/impg/PqMZCV3oLCC02jmNHnxA7UTeq8rMRF4vD2i4fQ/amJsE6aqZKk.jpg?size=2400x2400&quality=95&sign=950d8b5062183aa852c34e843a33bab7&type=album"
support = Sections('Support Text', 'Support', [image], 'support')

book = Sections('Book Text', 'Book', [image], 'book')