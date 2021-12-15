import requests
telegram_token = ''


def send_message(message, user):
    parameters = {
        "chat_id": user,
        "text": {message},
        "parse_mode": "Markdown"
    }
    response = requests.get(url=f"https://api.telegram.org/bot{telegram_token}/sendMessage?",
                            params=parameters)
    response.raise_for_status()
