import requests
import time
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the bot token from an environment variable
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if TOKEN is None:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable is not set.")

URL = f'https://api.telegram.org/bot{TOKEN}'

# Function to send messages
def send_message(chat_id, text):
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(f"{URL}/sendMessage", data=payload)
    if response.status_code != 200:
        logging.error("Error sending message: %s", response.text)
    return response

# Function to send photos
def send_photo(chat_id, photo):
    try:
        with open(photo, 'rb') as file:
            files = {'photo': file}
            response = requests.post(f"{URL}/sendPhoto", data={'chat_id': chat_id}, files=files)
            if response.status_code != 200:
                logging.error("Error sending photo: %s", response.text)
    except FileNotFoundError:
        logging.error("File not found: %s", photo)

# Function to handle incoming updates
def handle_updates():
    offset = None
    processed_updates = set()

    while True:
        url = f"{URL}/getUpdates"
        if offset:
            url += f"?offset={offset}"

        response = requests.get(url)
        if response.status_code != 200:
            logging.error("Error fetching updates: %s", response.text)
            time.sleep(5)
            continue

        updates = response.json().get('result', [])
        
        for update in updates:
            update_id = update['update_id']
            if update_id not in processed_updates:
                processed_updates.add(update_id)

                if 'message' in update:  # Check if the update contains a message
                    chat_id = update['message']['chat']['id']
                    
                    # Check if 'text' is present in the message
                    if 'text' in update['message']:
                        command = update['message']['text']
                        handle_command(command, chat_id)
                    else:
                        logging.warning("No text found in message: %s", update['message'])

                offset = update_id + 1  

        time.sleep(1)  # Avoid hitting API rate limits

def handle_command(command, chat_id):
    command_handlers = {
        '/start': lambda: send_message(chat_id, "សូមស្វាគមន៍មកកាន់ Robot របស់យើង! 🎉") or send_photo(chat_id, 'welcome.jpg'),
        '/DemoVideo': lambda: send_message(chat_id, 'LinkVideo: https://t.me/+vAiZcNfW9elhNDdl'),
        '/BuyTool': lambda: send_message(chat_id, 'ទំនាក់ទំនងទិញ: https://t.me/KSHD168'),
        '/Issue': lambda: send_message(chat_id, 'ដើម្បីរាយការណ៍បញ្ហា: https://t.me/+2OfccpF-8wgyMDg9'),
        '/TestingTool': lambda: send_message(chat_id, 'សុំសាកល្បងប្រើTools: https://t.me/+5ID_frxCxjk5OWU9'),
        '/Support': lambda: send_message(chat_id, 'ទាក់ទងផ្នែក support: https://t.me/KSHD168'),
        '/Tiktok': lambda: send_message(chat_id, 'Our TikTok: https://www.tiktok.com/@socialeasytools168?_t=8qIS9OuNBWX&_r=1'),
        '/About_Us': lambda: send_message(chat_id, 'Social Easy Tools គឺជាឧបករណ៍ MMO ដែលជួយអ្នកឱ្យក្លាយជាអ្នកមានក្នុងពេលឆាប់ៗនេះ.😎👌🔥'),
        '/Help': lambda: send_message(chat_id, (
            "/DemoVideo - របៀបប្រើTools 💻\n"
            "/BuyTool - ទិញ Social Easy Tools 💲💰\n"
            "/Issue - រាយការណ៍បញ្ហា Tools 🛠\n"
            "/TestingTool - សុំសាកល្បងប្រើTools 🤳\n"
            "/Support - ទាក់ទងផ្នែក support 🔧\n"
            "/Tiktok - Link to our TikTok 🎬\n"
            "/About_Us - ស្វែងយល់បន្ថែមអំពីយើង 👁‍🗨 \n"
            "/Help - រាយបញ្ជីសេវាកម្មដែលមាន 👨‍🔧"
        )),
    }

    handler = command_handlers.get(command)
    if handler:
        handler()
    else:
        send_message(chat_id, "Unknown command. Type /Help for assistance.")

if __name__ == '__main__':
    logging.info("Bot is running...")
    handle_updates()
