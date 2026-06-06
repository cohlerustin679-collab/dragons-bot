from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = "8733850331:AAG1ZIEUUhuc2t1TnPOtsJOkO6-YGFI-UgE"

IMAGE_URL = "https://i.ibb.co/9HQDRLVT/file-00000000d5b47206bc20556356c90186.png"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["JAR 🟠", "ACP 🔵"],
        ["Labs Chat 🔴"]
    ]

    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_photo(
        photo=IMAGE_URL,
        caption=(
            "Three Dragon Heads of Telegram\n\n"
            "Choose your destination and use the buttons below to levitate."
        ),
        reply_markup=reply_markup
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "JAR 🟠":
        await update.message.reply_text(
            "JAR\n\nhttps://t.me/+jQQHJsHr54oxYzcy"
        )

    elif text == "ACP 🔵":
        await update.message.reply_text(
            "ACP\n\nhttps://t.me/AntiChessPropaganda"
        )

    elif text == "Labs Chat 🔴":
        await update.message.reply_text(
            "Labs Chat\n\nhttps://t.me/parmar_Labs"
        )


app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons)
)

print("Bot is running...")
app.run_polling()