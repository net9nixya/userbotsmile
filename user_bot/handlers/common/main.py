from asyncio import sleep
from random import choice
import sqlite3

from pyrogram import Client
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.types import Message

from misc.html_tags import b
from user_bot.filters import get_filter
from user_bot.handlers.common.games import _get_game_handlers
from user_bot.utils import cmd, play_anim
from user_bot.handlers.common.stickers import _get_sticker_handlers
from user_bot.handlers.common.texts import _get_text_handlers


@cmd()
async def __night(app, msg: Message):
    sleep_words = (
        'зайка 💚', 'солнышко 💛', 'котёнок ❤', 'цветочек 💙', 'ангелочек 💜', 'принцесса 💓',
        'красотка 💕', 'милашка 💖', 'симпатяжка 💗', 'бусинка 💘',
    )
    love_words = (
        '❤ я ❤', '💚 тебя 💚', '💙 очень 💙', '💛 сильно 💛', '💜 люблю 💜',
    )
    for word in sleep_words:
        await msg.edit(b(f'Cпокойной ночи {word}'))
        await sleep(0.5)
    for word in love_words:
        await msg.edit(b(word))
        await sleep(0.5)


@cmd(True)
async def __bombs(app: Client, msg: Message):
    row = '▪️▪️▪️▪️\n'
    bombs = '💣 💣 💣 💣\n'
    fire = '💥 💥 💥 💥\n'
    smile = '😵 😵 😵 😵\n'
    words = (
        f"{row}{row}{row}{row}{row}",
        f"{bombs}{row}{row}{row}{row}",
        f"{row}{bombs}{row}{row}{row}",
        f"{row}{row}{bombs}{row}{row}",
        f"{row}{row}{row}{bombs}{row}",
        f"{row}{row}{row}{row}{bombs}",
        f"{row}{row}{row}{row}{fire}",
        f"{row}{row}{row}{fire}{fire}",
        f"{row}{row}{row}{row}{smile}"
    )
    await play_anim(msg, words)


@cmd(True)
async def __stupid(app: Client, msg: Message):
    first_str = 'ТВОЙ МОЗГ ➡️ 🧠\n\n🧠'
    second_str = 'ТВОЙ МОЗГ ➡️ 🧠\n\n'
    words = (
        f'{first_str}         (^_^)🗑',
        f'{first_str}       (^_^)  🗑',
        f'{first_str}     (^_^)    🗑',
        f'{first_str}   (^_^)      🗑',
        f'{first_str} (^_^)        🗑',
        f'{first_str} <(^_^ <)     🗑',
        f'{second_str}(> ^_^)>🧠   🗑',
        f'{second_str} (> ^_^)>🧠  🗑',
        f'{second_str}  (> ^_^)>🧠 🗑',
        f'{second_str}   (> ^_^)>🧠🗑',
        f'{second_str}       (^_^) 🗑',
        f'{second_str}        (3_3)🗑'
    )
    await play_anim(msg, words)
    
    
@cmd()
async def __pidor(app: Client, msg: Message):
    words = (
        'ебанутый', 'конченый', 'говнистый', 'тупой', 'гей', 'далбаеб', 'уебок', 'пидорас',
        'пиздючеловский', 'хуевый', 'даунский', 'шалавинский', 'жирный', 'пиздосный', 'пидорский',
    )
    await msg.edit('<b>Крошечные напоминания того, что ты далбаеб...</b>')
    await sleep(1)

    for word in words:
        await msg.edit(b(f'Cамый {word}😵‍💫'))
        await sleep(0.5)
    await msg.edit(b(f'Cамый {choice(words)}💀'))


@cmd()
async def __compli(app: Client, msg: Message):
    words = (
        'удивительная', 'внимательная', 'красивая', 'лучшая', 'успешная', 'заботливая', 'милая', 'прекрасная',
        'умная', 'шикарная', 'обалденная', 'очаровашка', 'любимая', 'весёлая', 'нежная', 'яркая', 'прелестная',
        'приятная', 'сладкая', 'дивная', 'ангельская', 'добрая', 'бесподобная', 'волшебная', 'крутышка', 'смелая',
        'ласковая', 'романтичная', 'великолепная', 'внимательная', 'страстная', 'игривая', 'единственная',
        'стройная', 'безумная', 'симпатичная', 'изящная', 'талантливая', 'элегантная', 'чуткая', 'уникальная',
    )
    await msg.edit('<b>Крошечные напоминания того, что ты...</b>')
    await sleep(1)

    for word in words:
        await msg.edit(b(f'Cамая {word}✨'))
        await sleep(0.5)
    await msg.edit(b(f'Cамая {choice(words)}✨'))
    
    
@cmd()
async def __naxyi(app, msg: Message):
    text = ''
    total = 'Пошёл нахуй чудак ебаный'
    for char in total:
        text += char
        if char == ' ':
            continue
        await msg.edit(b(text))
        await sleep(0.1)


@cmd()
async def __bagger_fast(app, msg: Message):
    text = ''
    total = 'Pythоn ИМБА, Pythоn ЕДИН. И Небесный непобедим!!!'
    for char in total:
        text += char
        if char == ' ':
            continue
        await msg.edit(b(text))
        await sleep(0.1)
        
        
import sqlite3

# Путь к базе данных
db_path = "user_prefixes.db"

# Создание таблицы для хранения префиксов, если она не существует
def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prefixes
                 (user_id INTEGER PRIMARY KEY, prefix TEXT)''')
    conn.commit()
    conn.close()

# Получение префикса пользователя из базы данных
def get_prefix(user_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT prefix FROM prefixes WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "-"

# Сохранение префикса в базе данных
def set_prefix(user_id, prefix):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('REPLACE INTO prefixes (user_id, prefix) VALUES (?, ?)', (user_id, prefix))
    conn.commit()
    conn.close()

# Создание таблицы при старте бота
create_table()

@cmd()
async def __prefix(app: Client, msg: Message):
    # Извлекаем текст после команды
    prefix = msg.text.split()[1:]  # Считываем текст после .префикс
    if prefix:
        prefix = prefix[0]

        # Проверяем, что длина сообщения не превышает 7 символов
        if len(prefix) > 7:
            await msg.reply("Ошибка! Префикс не должен превышать 7 символов.")
            return
        
        # Сохраняем префикс в базе данных
        set_prefix(msg.from_user.id, prefix)
        
        # Отправляем ответ о том, что префикс был изменен
        await msg.reply(f"Префикс успешно изменен на: {prefix}")
    else:
        await msg.reply("Ошибка! Вы не указали новый префикс.")

import sqlite3
from pyrogram.handlers import MessageHandler

import sqlite3

# Путь к базе данных
db_path = "user_prefixes.db"

# Создание таблицы для хранения префиксов, если она не существует
def create_table():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS prefixes
                 (user_id INTEGER PRIMARY KEY, prefix TEXT)''')
    conn.commit()
    conn.close()

# Получение префикса пользователя из базы данных
def get_prefix(user_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT prefix FROM prefixes WHERE user_id = ?', (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else "-"

# Сохранение префикса в базе данных
def set_prefix(user_id, prefix):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('REPLACE INTO prefixes (user_id, prefix) VALUES (?, ?)', (user_id, prefix))
    conn.commit()
    conn.close()

# Создание таблицы при старте бота
create_table()

@cmd()
async def __prefix(app: Client, msg: Message):
    # Извлекаем текст после команды
    prefix = msg.text.split()[1:]  # Считываем текст после .префикс
    if prefix:
        prefix = prefix[0]

        # Проверяем, что длина сообщения не превышает 7 символов
        if len(prefix) > 7:
            await msg.reply("Ошибка! Префикс не должен превышать 7 символов.")
            return
        
        # Сохраняем префикс в базе данных
        set_prefix(msg.from_user.id, prefix)
        
        # Отправляем ответ о том, что префикс был изменен
        await msg.reply(f"Префикс успешно изменен на: {prefix}")
    else:
        await msg.reply("Ошибка! Вы не указали новый префикс.")
        
        
        
from pyrogram import Client
from pyrogram.types import Message

@cmd()
async def __help(app: Client, msg: Message):
    help_text = (
        '<a href="https://graph.org/Komandy-yuzer-bota-Lysyj-04-06">Все команды юзер бота</a> <i>(Кликабельно)</i>'
    )

    photo_path = "images/actions/journey/magic-forest/7.png"

    # Удаляем исходное сообщение (.help)
    await msg.delete()

    # Отправляем новое фото с подписью
    await app.send_photo(
        chat_id=msg.chat.id,
        photo=photo_path,
        caption=help_text
    )



@cmd()
async def __info(app: Client, msg: Message):
    # Получаем префикс пользователя из базы данных
    prefix = get_prefix(msg.from_user.id)
    
    # Формируем текст с информацией
    info_text = (
        "<b>Информация о юзер боте:</b>\n\n"
        f"Этот бот создан для развлекательных целей.\n"
        f"Он поддерживает множество команд и функций.\n"
        f"Чтобы узнать доступные команды, используйте /start в личке бота.\n\n"
        f"<b>Информация о пользователе:</b>\n"
        f"Авторизован: <b>да</b>\n"
        f"Префикс: <i>«{prefix}»</i>\n"
        f"Никнейм: <i>@{msg.from_user.username}</i>\n"
        f"Телеграм ID: <i>{msg.from_user.id}</i>\n\n"
        f"<a href='https://graph.org/Komandy-yuzer-bota-Lysyj-04-06'>Список команд</a> <i>(Кликабельно)</i>\n\n"
        f"Автор бота: <i>Небесный</i>\n"
        f"UUID: <i>В разработке</i>\n"
        f"Версия бота: <i>1.0</i>\n"
        f"Дата последнего обновления: <i>2025-04-06</i>"
    )
    
    # Путь до изображения
    photo_path = "images/actions/journey/magic-forest/4.png"
    
    # Отправляем изображение с текстом в одном сообщении
    await msg.reply_photo(photo=photo_path, caption=info_text)
    
@cmd()
async def __get(app: Client, msg: Message):
    # Проверяем, есть ли ответ на сообщение
    if msg.reply_to_message:
        replied_user = msg.reply_to_message.from_user  # Получаем пользователя, на чье сообщение ответили
        user_name = replied_user.username if replied_user.username else "Не указано"
        first_name = replied_user.first_name if replied_user.first_name else "Не указано"
        last_name = replied_user.last_name if replied_user.last_name else "Не указано"
        user_id = replied_user.id
        account_creation_date = "Неизвестно"  # Не можем получить точную дату, можно извлечь из базы данных или использовать другие подходы
        avatar = "Есть" if replied_user.photo else "Нет"
        premium = "Да" if replied_user.is_premium else "Нет"
        is_bot = "Да" if replied_user.is_bot else "Нет"
        
        # Чекаем, является ли аккаунт официальным
        official_account = "Да" if replied_user.username and replied_user.is_bot else "Нет"  # Примерная проверка для официального аккаунта

        info_text = (
            f"👁Информация о {first_name} {last_name} ({user_name})\n\n"
            f"✏️Имя: {first_name}\n"
            f"📝Фамилия: {last_name}\n"
            f"👤Юзернейм: @{user_name}\n"
            f"🪪ID: {user_id}\n"
            f"📆Дата аккаунта: {account_creation_date}\n"
            f"🖼Аватар: {avatar}\n"
            f"⭐Premium: {premium}\n"
            f"🤖Бот: {is_bot}\n"
            f"✅Официальный аккаунт: {official_account}"
        )

        # Путь до изображения (можно заменить на свой)
        photo_path = "images/actions/journey/magic-forest/4.png"  # Можешь изменить на путь к своему изображению

        # Отправляем изображение с текстом в одном сообщении
        await msg.reply_photo(photo=photo_path, caption=info_text)
    else:
        # Если сообщение не является ответом
        await msg.reply("Пожалуйста, ответьте на сообщение, чтобы получить информацию о пользователе.")



def get_common_handlers() -> tuple[MessageHandler, ...]:
    return (
        MessageHandler(__bombs, filters=get_filter('bombs')),
        MessageHandler(__night, filters=get_filter('night')),
        MessageHandler(__stupid, filters=get_filter('stupid')),
        MessageHandler(__compli, filters=get_filter('compli')),
        MessageHandler(__pidor, filters=get_filter('pidor')),
        MessageHandler(__prefix, filters=get_filter('prefix')),
        MessageHandler(__help, filters=get_filter('help')),
        MessageHandler(__info, filters=get_filter('инфо')),
        MessageHandler(__naxyi, filters=get_filter('послать')),
        MessageHandler(__get, filters=get_filter('get')),
        MessageHandler(__info, filters=get_filter('info')),
        MessageHandler(__bagger_fast, filters=get_filter('nb')),

        *_get_game_handlers(),
        *_get_text_handlers(),
        *_get_sticker_handlers(),
    )
