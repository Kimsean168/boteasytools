import telebot

# Replace 'YOUR_TOKEN' with your actual bot token
TOKEN = '7562016359:AAHkKTS_zZvcXpZy6jAHdEtdSX5FRR4XMrE'  # Use your actual token here
bot = telebot.TeleBot(TOKEN)

# Define command responses
@bot.message_handler(commands=['start'])
def start(message):
    # Send a welcome message
    welcome_text = "សូមស្វាគមន៍មកកាន់ Robot របស់យើង! យើងរីករាយដែលមានអ្នកជាសមាជិក។ 🎉"
    bot.reply_to(message, welcome_text)
    
    # Send a welcome image (update 'welcome_image.jpg' to your image filename)
    with open('welcome.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

@bot.message_handler(commands=['DemoVideo'])
def demo(message):
    bot.reply_to(message, 'LinkVideo: https://t.me/+vAiZcNfW9elhNDdl')

@bot.message_handler(commands=['BuyTool'])
def buy_tool(message):
    bot.reply_to(message, 'ទំនាក់ទំនងទិញ: https://t.me/KSHD168')

@bot.message_handler(commands=['Issue'])
def issue(message):
    bot.reply_to(message, 'ដើម្បីរាយការណ៍បញ្ហា: https://t.me/+2OfccpF-8wgyMDg9')

@bot.message_handler(commands=['TestingTool'])
def testing_tool(message):
    bot.reply_to(message, 'សុំសាកល្បងប្រើTools: https://t.me/+5ID_frxCxjk5OWU9')

@bot.message_handler(commands=['Support'])
def contact_support(message):
    bot.reply_to(message, 'ទាក់ទងផ្នែក support:https://t.me/KSHD168')

@bot.message_handler(commands=['Tiktok'])
def tiktok(message):
    bot.reply_to(message, 'Our TikTok: https://www.tiktok.com/@socialeasytools168?_t=8qIS9OuNBWX&_r=1')

@bot.message_handler(commands=['About_Us'])
def about(message):
    bot.reply_to(message, 'Social Easy Tools គឺជាឧបករណ៍ MMO ដែលជួយអ្នកឱ្យក្លាយជាអ្នកមានក្នុងពេលឆាប់ៗនេះ.😎👌🔥')

@bot.message_handler(commands=['Help'])
def help_command(message):
    help_text = (
        "/DemoVideo - របៀបប្រើTools 💻\n"
        "/BuyTool - ទិញ Social Easy Tools 💲💰\n"
        "/Issue - រាយការណ៍បញ្ហា Tools 🛠\n"
        "/TestingTool - សុំសាកល្បងប្រើTools 🤳\n"
        "/Support - ទាក់ទងផ្នែក support 🔧\n"
        "/Tiktok - Link to our TikTok 🎬\n"
        "/About_Us - ស្វែងយល់បន្ថែមអំពីយើង 👁‍🗨 \n"
        "/Help - រាយបញ្ជីសេវាកម្មដែលមាន 👨‍🔧"
    )
    bot.reply_to(message, help_text)

print("Bot is running......")
# Start polling for messages
bot.polling()
