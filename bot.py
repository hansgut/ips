from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from os import environ

stub_text = """
Improve communication and reduce tension with the coworker.
Create a more positive and cooperative work environment.
Manage stress related to the conflict.

Schedule a meeting with the coworker to discuss the issues in a calm and constructive way.
Seek mediation through HR or a manager to facilitate better communication.
Practice active listening and empathy to better understand the coworker’s perspective.
Set boundaries and agree on clear roles and responsibilities to avoid future conflict.
Practice stress-relief techniques outside of work to manage the emotional impact.
"""


def get_data(question: str):
    print(question)
    # TODO Get data from LLM model
    return stub_text


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=get_data(update.message.text))


if __name__ == '__main__':
    token = environ.get('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(token).build()
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(echo_handler)

    application.run_polling()
