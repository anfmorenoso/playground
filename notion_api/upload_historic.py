import json
from typing import Dict
import pandas as pd
from helpers import read_json, create_page_in_database


def save_expenses(key_dict: Dict[str, str], expenses: pd.DataFrame):
    my_dict = read_json("cache/month_year_id_dict.json")
    ok_count = 0
    for _, expense in expenses.iterrows():
        data = {
            "title": expense["Task Name"],
            "amount": expense["Money"],
            "date": expense["pay_date"],
            "relation_id": my_dict[expense["month_year"]],
        }
        res = create_page_in_database(
            database_id=key_dict["all_expenses_id"],
            token=key_dict["internal_integration_token"],
            data=data,
            save_file=False,
            expense=True,
        )
        ok_count = ok_count + 1 if res.status_code == 200 else 0
    print(f"ok expenses = {ok_count}")


def save_income(key_dict: Dict[str, str], incomes: pd.DataFrame):
    my_dict = read_json("cache/month_year_id_dict.json")
    ok_count = 0
    for _, income in incomes.iterrows():
        data = {
            "title": income["Task Name"],
            "tag": "Main",
            "amount": income["Money"],
            "date": income["pay_date"],
            "relation_id": my_dict[income["month_year"]],
        }
        res = create_page_in_database(
            database_id=key_dict["all_income_id"],
            token=key_dict["internal_integration_token"],
            data=data,
            save_file=False,
            expense=False,
        )
        ok_count = ok_count + 1 if res.status_code == 200 else 0
    print(f"ok incomes = {ok_count}")


if __name__ == "__main__":
    key_dict = read_json("cache/notion.json")

    expenses = pd.read_csv("cache/final_expenses.csv")
    income = pd.read_csv("cache/final_income.csv")

    save_income(key_dict, income)
    save_expenses(key_dict, expenses)
