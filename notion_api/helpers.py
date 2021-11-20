import json
import requests
from requests.api import request


def get_keys_dict():
    with open("../cache/notion.json", "r") as file:
        return json.loads(file.read())


def read_database(database_id: str, token: str, save_file=True):
    read_url = f"https://api.notion.com/v1/databases/{database_id}"
    headersAuth = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2021-08-16",
    }
    res = requests.request("GET", read_url, headers=headersAuth)
    print(res.status_code)

    if save_file:
        with open("../cache/response_read.json", "w", encoding="utf8") as file:
            json.dump(res.json(), file, ensure_ascii=False)
    return res


def query_database(database_id: str, token: str, save_file=True):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"
    headersAuth = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2021-08-16",
    }
    res = requests.request("POST", read_url, headers=headersAuth)
    print(res.status_code)

    if save_file:
        with open("../cache/response_query.json", "w", encoding="utf8") as file:
            json.dump(res.json(), file, ensure_ascii=False)
    return res


def get_page(page_id: str, token: str, save_file=True):
    read_url = f"https://api.notion.com/v1/pages/{page_id}"
    headersAuth = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2021-08-16",
    }
    res = requests.request("GET", read_url, headers=headersAuth)
    print(res.status_code)

    if save_file:
        with open("../cache/page_read.json", "w", encoding="utf8") as file:
            json.dump(res.json(), file, ensure_ascii=False)
    return res


def create_page_in_database(database_id: str, token: str, save_file=True):
    read_url = f"https://api.notion.com/v1/pages"
    headersAuth = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16",
    }
    new_page_data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": "With relation",
                        },
                    }
                ]
            },
            "Amount": {
                "number": 420.69,
            },
            "Tags": {
                "multi_select": [
                    {
                        "name": "test_tag",
                    }
                ]
            },
            "Paid Date": {
                "date": {
                    "start": "2021-11-22",
                }
            },
            "Balance ID": {
                "relation": [
                    {
                        "id": "c41b43e3-914d-47ee-b545-68b53119e542",
                    }
                ]
            },
        },
    }

    res = requests.request(
        "POST", read_url, headers=headersAuth, data=json.dumps(new_page_data)
    )
    print(res.status_code)

    if save_file:
        with open("../cache/response_new_page.json", "w", encoding="utf8") as file:
            json.dump(res.json(), file, ensure_ascii=False)
    return res
