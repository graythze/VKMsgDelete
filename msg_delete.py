import requests
import time
import argparse

# Config values. Probably no need to tweak
bulk_message_size = 100
api_timeout = 0.34


def delete_messages(min_msg: int, max_msg: int, vk_token: str):
    for i in range(min_msg, max_msg, bulk_message_size):
        msgs = ",".join(map(str, range(i, min(i + bulk_message_size, max_msg))))
        print(f"Deleting messages: {msgs}")

        response = requests.get(
            "https://api.vk.ru/method/messages.delete",
            params={
                "message_ids": msgs,
                "delete_for_all": 1,
                "v": "5.199",
                "access_token": vk_token
            }
        )

        print(response.json())
        time.sleep(api_timeout)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VK Message Remover")
    parser.add_argument("--min_msg", type=int, required=True, help="Start message ID")
    parser.add_argument("--max_msg", type=int, required=True, help="End message ID")
    parser.add_argument("--vk_token", type=str, required=True, help="VK Token")

    args = parser.parse_args()

    delete_messages(args.min_msg, args.max_msg, args.vk_token)

