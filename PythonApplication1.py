import requests
import time
import os

# Load the bot token from an environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')  # Set this environment variable on Render
URL = f'https://api.telegram.org/bot{TOKEN}'

# Function to send messages
def send_message(chat_id, text):
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(f"{URL}/sendMessage", data=payload)
    return response

# Function to send photos
def send_photo(chat_id, photo):
    with open(photo, 'rb') as file:
        files = {'photo': file}
        response = requests.post(f"{URL}/sendPhoto", data={'chat_id': chat_id}, files=files)
    return response

# Function to handle incoming updates
def handle_updates():
    offset = 0
    while True:
        response = requests.get(f"{URL}/getUpdates?offset={offset}")
        if response.status_code != 200:
            print("Error fetching updates:", response.text)
            time.sleep(5)  # Wait before retrying
            continue

        updates = response.json().get('result', [])
        
        for update in updates:
            offset = update['update_id'] + 1
            chat_id = update['message']['chat']['id']
            command = update['message']['text']

            if command == '/start':
                welcome_text = "សូមស្វាគមន៍មកកាន់ Robot របស់យើង! យើងរីករាយដែលមានអ្នកជាសមាជិក។ 🎉"
                send_message(chat_id, welcome_text)
                send_photo(chat_id, 'welcome.jpg')

            elif command == '/DemoVideo':
                send_message(chat_id, 'LinkVideo: https://t.me/+vAiZcNfW9elhNDdl')

            elif command == '/BuyTool':
                send_message(chat_id, 'ទំនាក់ទំនងទិញ: https://t.me/KSHD168')

            elif command == '/Issue':
                send_message(chat_id, 'ដើម្បីរាយការណ៍បញ្ហា: https://t.me/+2OfccpF-8wgyMDg9')

            elif command == '/TestingTool':
                send_message(chat_id, 'សុំសាកល្បងប្រើTools: https://t.me/+5ID_frxCxjk5OWU9')

            elif command == '/Support':
                send_message(chat_id, 'ទាក់ទងផ្នែក support: https://t.me/KSHD168')

            elif command == '/Tiktok':
                send_message(chat_id, 'Our TikTok: https://www.tiktok.com/@socialeasytools168?_t=8qIS9OuNBWX&_r=1')

            elif command == '/About_Us':
                send_message(chat_id, 'Social Easy Tools គឺជាឧបករណ៍ MMO ដែលជួយអ្នកឱ្យក្លាយជាអ្នកមានក្នុងពេលឆាប់ៗនេះ.😎👌🔥')

            elif command == '/Help':
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
                send_message(chat_id, help_text)

        time.sleep(1)  # Sleep to avoid hitting the API rate limit

if __name__ == '__main__':
    print("Bot is running......")
    handle_updates()
