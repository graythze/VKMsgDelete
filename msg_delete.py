import requests
import time

min_msg = 1
max_msg = 15000000

vk_token = ""

for i in range(min_msg, max_msg, 100):
    msgs = ",".join(map(str, range(i, min(i + 100, max_msg))))
    print(msgs)

    messages = requests.get(f"https://api.vk.com/method/messages.delete",
                    params={"message_ids": msgs,
                          "delete_for_all": 1,
                          "v": "5.199",
                          "access_token": "vk_token"})
    print(messages.json())
    time.sleep(0.34)
