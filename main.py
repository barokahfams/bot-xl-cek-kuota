import os
import time
import subprocess
from telegram.ext import ApplicationBuilder, CommandHandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

MODE = os.getenv("MODE", "selenium")
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text(f"Bot aktif.\nMode: {MODE}\nGunakan /cek untuk cek kuota.")

async def cek(update, context):
    await update.message.reply_text("Memproses...")

    if MODE == "selenium":
        result = cek_selenium()
    else:
        result = cek_gammu()

    await update.message.reply_text(result)

def cek_selenium():
    phone = os.getenv("XL_PHONE")
    password = os.getenv("XL_PASSWORD")

    if not phone or not password:
        return "XL_PHONE dan XL_PASSWORD belum diisi di file .env"

    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=chrome_options)
