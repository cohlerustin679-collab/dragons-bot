from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8733850331:AAG1ZIEUUhuc2t1TnPOtsJOkO6-YGFI-UgE"

JAR_IMAGE = "AgACAgEAAxkBAAFLsKBqJIPKJsguq5_yBQOOHxBtXr8RrQACTwxrGzGYKUUOPAOSyrZJ4wEAAwIAA3MAAzsE"

ACP_IMAGE = "AgACAgEAAxkBAAFLsKJqJIQMl6pLWht9CxbhyaGwbJEuqAACUAxrGzGYKUU7Egd9GJl3eQEAAwIAA3gAAzsE"

LABS_IMAGE = "AgACAgEAAxkBAAFLsKhqJIR7u8fOAyV_ITzG8pGILjeREgACUQxrGzGYKUU57Wg1BX5q0AEAAwIAA3cAAzsE"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["JAR 🟠", "ACP 🔵"],
        ["Labs Chat 🔴"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "Three Dragon Heads of Telegram\n\nChoose your destination and use the buttons below to levitate.",
        reply_markup=reply_markup
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "JAR 🟠":
    await update.message.reply_text(
        "JAR\n\nhttps://t.me/+jQQHJsHr54oxYzcy"
    )
            caption="JAR\n\nhttps://t.me/+jQQHJsHr54oxYzcy"
        )

    elif text == "ACP 🔵":
        await update.message.reply_photo(
            photo=ACP_IMAGE,
            caption="ACP\n\nhttps://t.me/AntiChessPropaganda"
        )

    elif text == "Labs Chat 🔴":
        await update.message.reply_photo(
            photo=LABS_IMAGE,
            caption="Labs Chat\n\nhttps://t.me/parmar_Labs"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons)
)

print("Bot is running...")
app.run_polling()