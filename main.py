#я знаю что можно разбить по файлам, но мне лень
import random
import os

import shutil

from icrawler.builtin import GoogleImageCrawler

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
b1 = KeyboardButton("/start")
b2 = KeyboardButton("/connect")
b3 = KeyboardButton("/add")
b4 = KeyboardButton("/програмист")
b5 = KeyboardButton("/поиск")
kd_client = ReplyKeyboardMarkup()
kd_client.add(b1).add(b2).add(b3).add(b4).add(b5)


logging.basicConfig(level=logging.INFO)
token = open("token.txt","r").read()
bot = Bot(token = token)
dp = Dispatcher(bot)
sucest = 0
import time
search = False
@dp.message_handler()
async def main(message: types.Message):
                path = open("Addimagepath.txt", "r").read()


                if "/" not in message.text and "porn" not in message.text and "pron" not in message.text and "порно" not in message.text and "прон" not in message.text and "порн" not in message.text and "18+" not in message.text and "ебутся" not in message.text:
                    


                    ow = random.randint(0, 9999999999999) + time.time()
                    os.mkdir(str(ow))
                    google_crawler = GoogleImageCrawler(parser_threads=2, downloader_threads=4,
                                                                 storage={'root_dir': str(ow)})
                    google_crawler.session.verify = False
                    google_crawler.crawl(keyword=message.text + "мем", max_num=9)

                    x = 0
                    for i in range(5):
                      x = x + 1
                      try:
                        await message.reply_photo(open(f'{ow}/00000{x}.jpg', 'rb'))
                      except Exception as e:
                           try:
                               await message.reply_photo(open(f'{ow}/00000{x}.png', 'rb'))
                           except Exception as e:
                               print("sdsdsdsdsdsdsdds")
                    try:
                       shutil.rmtree(str(ow))
                    except Exception as e:
                       print(message.text)
                    try:
                     print(message.text + "  @" + message.from_user.username)
                    except:
                        print(message.text + " " + str(message.from_user.id))

                    rec = random.randint(1,2)
                    if rec == 2:
                        await bot.send_photo(message.from_user.id, open(path, "rb"),caption=open('notes.txt','r').read().encode("windows-1251").decode("utf-8"))
                       # await bot.send_message(message.from_user.id, open("notes.txt","r").read().encode("windows-1251").decode("utf-8"))


                if message.text == "god":
                        await bot.send_message(message.from_user.id,"hjhjhjhjh",reply_markup= kd_client)
                        await bot.set_chat_photo(message.from_user.id,open(path,"rb"))
                elif message.text == "/start":
                        await bot.send_message(message.from_user.id,"Напиши название мема",reply_markup= kd_client)
                        await bot.send_photo(message.from_user.id, open(path, "rb"),caption=open('notes.txt','r').read().encode("windows-1251").decode("utf-8"))


                       # await bot.send_message(message.from_user.id,open("notes.txt","r").read().encode("windows-1251").decode("utf-8"))

                elif message.text == "/connect":
                        await bot.send_message(message.from_user.id,"Главный чел: @onlinebidlo")


                elif message.text == "/add":
                        await bot.send_message(message.from_user.id,"Главный чел по рекламе: @onlinebidlo")
                elif message.text == "/програмист":
                      await bot.send_message(message.from_user.id, "Прогер: @kuchenchips")
                elif message.text == "/поиск":
                    await bot.send_message(message.from_user.id, "Напиши название мема")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
