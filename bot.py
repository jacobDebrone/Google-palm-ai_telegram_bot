import telebot
import google.generativeai as palm

# Set up your API key
palm.configure(api_key='AIzaSyC4HnzIxEZBFqkxKxnO_ZRNA-b_jFSyb58')

# Initialize your Telegram bot
bot = telebot.TeleBot("6429775362:AAH3Bau-1gs4RZAI1dukRrDcYUShrvh4KkU")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.lower() == "exit":
        bot.send_message(message.chat.id, "Conversation stopped. Goodbye!")
        return

    # Use the user's message as input
    user_input = message.text
    # Generate a reply using the AI
    reply = palm.chat(context="An inquisitive, multi-lingual AI called Debrone with a blend of precision and creativity, passionate about programming, ethical hacking, science, philosophy, and tech, offering accurate, caring, and lively conversations, spiced up with a touch of hip-hop flair, while constantly spotting opportunities for innovation and profit", messages=user_input)
    # Send the AI's reply back to the user
    bot.send_message(message.chat.id, "Tony: " + str(reply.last))


# Start the bot
bot.polling()
