from osonbot import Bot, KeyboardButton
from deep_translator import GoogleTranslator

bot = Bot("8380176186:AAEwFZLcl_kGkQi8WLhQrCtFZD4EdxnMhms")

language = {'from': None, 'to': None}

languages_button = KeyboardButton(["🇺🇿 O'zbekcha", "🇷🇺 Ruscha", "🇬🇧 Ingilizcha"], ["🇪🇸 Ispancha", "🇹🇷 Turkcha", "🇩🇪 Nemischa"], ["🇫🇷 Fransuzcha", "🇮🇹 Italiyancha", "🇸🇦 Arabcha"], ["🇰🇷 Koreyscha", "🇨🇳 Xitoycha", "🇯🇵 Yaponcha"], ["🔄 Tilni O'zgartirish"])

def handle_uzbek(message):
    if language['from'] is None:
        language['from'] = 'uz'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'uz'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"

def handle_russian(message):
    if language['from'] is None:
        language['from'] = 'ru'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'ru'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"

def handle_english(message):
    if language['from'] is None:
        language['from'] = 'en'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'en'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_spanish(message):
    if language['from'] is None:
        language['from'] = 'es'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'es'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_turkish(message):
    if language['from'] is None:
        language['from'] = 'tr'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'tr'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"

def handle_german(message):
    if language['from'] is None:
        language['from'] = 'de'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'de'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"

def handle_french(message):
    if language['from'] is None:
        language['from'] = 'fr'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'fr'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_italian(message):
    if language['from'] is None:
        language['from'] = 'it'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'it'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_arabic(message):
    if language['from'] is None:
        language['from'] = 'ar'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'ar'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_korean(message):
    if language['from'] is None:
        language['from'] = 'ko'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'ko'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_chinese(message):
    if language['from'] is None:
        language['from'] = 'zh'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'zh'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    
def handle_japanese(message):
    if language['from'] is None:
        language['from'] = 'ja'
        return "Endi qaysi tilga tarjima qilmoqchi ekanligingizni tanlang"
    elif language['to'] is None:
        language['to'] = 'ja'
        return f"Bot matningizni tarjima qilishga tayyor. Matningizni kiriting"
    

def reset_languages(message):
    language['from'] = None
    language['to'] = None
    return "matningiz qaysi tildaligini tanlang"

def start(message):
    return f"Salom {message['from']['first_name']}!\nmen Tarjimon botman.\nmatningiz qaysi tildaligini tanlang"

bot.when("/start", start, reply_markup=languages_button)

bot.when("🔄 Tilni O'zgartirish", reset_languages, reply_markup=languages_button)

bot.when("🇺🇿 O'zbekcha", handle_uzbek, reply_markup=languages_button)
bot.when("🇷🇺 Ruscha", handle_russian, reply_markup=languages_button)
bot.when("🇬🇧 Ingilizcha", handle_english, reply_markup=languages_button)
bot.when("🇪🇸 Ispancha", handle_spanish, reply_markup=languages_button)
bot.when("🇹🇷 Turkcha", handle_turkish, reply_markup=languages_button)
bot.when("🇩🇪 Nemischa", handle_german, reply_markup=languages_button)
bot.when("🇫🇷 Fransuzcha", handle_french, reply_markup=languages_button)
bot.when("🇮🇹 Italiyancha", handle_italian, reply_markup=languages_button)
bot.when("🇸🇦 Arabcha", handle_arabic, reply_markup=languages_button)
bot.when("🇰🇷 Koreyscha", handle_korean, reply_markup=languages_button)
bot.when("🇨🇳 Xitoycha", handle_chinese, reply_markup=languages_button)
bot.when("🇯🇵 Yaponcha", handle_japanese, reply_markup=languages_button)

def translate(message):
    return GoogleTranslator(source=language['from'] or 'auto', target=language['to'] or 'en').translate(message['text'])

bot.when("*", translate)

bot.run()
