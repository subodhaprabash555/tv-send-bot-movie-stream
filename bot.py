from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# BOT TOKEN
TOKEN = "8675108417:AAFIrkLl-fit8GGMXmjrOrfGkhaQHRwEXts"

# CHANNEL USERNAME
CHANNEL_ID = "@moviestream_PS"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:

        # check if start has parameter
        if context.args:

            msg_id = int(context.args[0])

            # copy message from channel to user
            await context.bot.copy_message(
                chat_id=update.effective_chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=msg_id
            )

        else:

            await update.message.reply_text(
                "🎬 Welcome to Movie Stream Bot\n\nSend movie link to watch."
            )

    except Exception as e:

        await update.message.reply_text("❌ Movie not found.")


# Create bot
app = ApplicationBuilder().token(TOKEN).build()

# Start command handler
app.add_handler(CommandHandler("start", start))

print("🤖 Bot Running...")

# Run bot
app.run_polling()