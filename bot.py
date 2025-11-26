from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8399417849:AAGYtjC7FvFcsMZUsDiH3SzXTE933ywoTU0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я простий тестовий бот ")

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Список команд:\n/start – почати\n/help – допомога\n/test – тестова команда")

async def test_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Тестова команда працює!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text(f"Ти написав: {text}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_cmd))
app.add_handler(CommandHandler("test", test_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

print("Бот запущений...")
app.run_polling()
