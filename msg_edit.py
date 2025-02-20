import requests
import time
import random

min_msg = 0
max_msg = 15000000
personal_id = 1

vk_token = ""

def read_words_from_file(file_path):
    with open(file_path, 'r', encoding="windows-1251") as file:
        return [line.strip() for line in file.readlines()]

def generate_random_string(words, min_length=1, max_length=2048):
    random_string = ""
    while len(random_string) < min_length or len(random_string) > max_length:

        random.shuffle(words)
        random_string = ' '.join(words)

        if len(random_string) > max_length:
            random_string = random_string[:max_length]
        elif len(random_string) < min_length:
            random_string = "I like hamburgers with cheese and ketchup"
    return random_string

words = read_words_from_file("src/english.txt")

for i in range(min_msg, max_msg, 100):
    msgs = ",".join(map(str, range(i, min(i + 100, max_msg))))
    print(msgs)

    messages = requests.get(f"https://api.vk.com/method/messages.getById",
                    params={"message_ids": msgs,
                          "v": "5.199",
                          "access_token": vk_token}).json()
    time.sleep(0.34)
    for message in messages["response"]["items"]:
        if message["from_id"] == personal_id:
            message_request = requests.get(f"https://api.vk.com/method/messages.edit",
                                           params={"peer_id": message["from_id"],
                                                   "message_id": message["id"],
                                                   "message": str(generate_random_string(words)),
                                                   "v": "5.199",
                                                   "access_token": vk_token}).json()
            print(message_request)
            time.sleep(15)
    print(messages.json())
    time.sleep(0.34)
