import json
from typing import Dict
import requests
from requests.api import request


def get_keys_dict():
    with open("../cache/notion.json", "r") as file:
        return json.loads(file.read())


def read_json(file_path: str):
    with open(file_path, "r") as file:
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


def create_page_in_database(
    database_id: str, token: str, data: Dict[str, str], save_file=True, expense=True
):
    read_url = f"https://api.notion.com/v1/pages"
    headersAuth = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2021-08-16",
    }
    new_page_data = create_page_data_from_dict(data, database_id, expense)

    res = requests.request(
        "POST", read_url, headers=headersAuth, data=json.dumps(new_page_data)
    )
    # print(res.status_code)

    if save_file:
        with open("../cache/response_new_page.json", "w", encoding="utf8") as file:
            json.dump(res.json(), file, ensure_ascii=False)
    return res


def create_month_year_id_dict() -> Dict[str, str]:
    key_dict = get_keys_dict()
    res = query_database(
        database_id=key_dict["balance_database"],
        token=key_dict["internal_integration_token"],
    )

    my_id_dict = {}
    for page in res.json()["results"]:
        my_id_dict[page["properties"]["Month/Year"]["title"][0]["plain_text"]] = page[
            "id"
        ]

    with open("../cache/month_year_id_dict.json", "w", encoding="utf8") as file:
        json.dump(my_id_dict, file, ensure_ascii=False)
    return


def create_page_data_from_dict(data, database_id, expense=True):
    page_data = {"parent": {"database_id": database_id}}
    page_data["properties"] = {}

    if "title" in data.keys():
        page_data["properties"]["Name"] = {
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": data["title"],
                    },
                }
            ]
        }
    if "tag" in data.keys():
        page_data["properties"]["Tags" if expense else "Account"] = {
            "multi_select"
            if expense
            else "select": [
                {
                    "name": data["tag"],
                }
            ]
            if expense
            else {
                "name": data["tag"],
            }
        }
    if "amount" in data.keys():
        page_data["properties"]["Amount"] = {
            "number": data["amount"],
        }
    if "date" in data.keys():
        page_data["properties"]["Paid Date"] = {
            "date": {
                "start": data["date"],
            }
        }

    if "relation_id" in data.keys():
        page_data["properties"]["Balance ID"] = {
            "relation": [
                {
                    "id": data["relation_id"],
                }
            ]
        }

    return page_data
