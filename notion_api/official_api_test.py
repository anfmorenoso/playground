#%%
%reload_ext autoreload
%autoreload 2
#%%
from requests.api import get
from helpers import get_keys_dict, read_database, query_database, create_page_in_database, get_page, create_month_year_id_dict,create_page_data_from_dict
import json

#%%
key_dict = get_keys_dict()


#%%
res = read_database(
    database_id=key_dict["balance_database"],
    token=key_dict["internal_integration_token"],
)

# %%
res = query_database(
    database_id=key_dict["balance_database"],
    token=key_dict["internal_integration_token"],
)
# %%

data = {
    "title": "From dict",
    "tag": "Going Out",
    "amount": 420.69,
    "date": "2021-12-10",
    "relation_id": "c41b43e3-914d-47ee-b545-68b53119e542",
}
res = create_page_in_database(
    database_id=key_dict["all_expenses_id"],
    token=key_dict["internal_integration_token"],
    data=data,
    expense=True
)

# %%
res = get_page(
    page_id=key_dict['test_expense_id'], 
    token=key_dict["internal_integration_token"],
)

# %%

month_year_id_dict = create_month_year_id_dict()
# %%
data = {
    "title": "From dict",
    "amount": 420.69,
    "date": "2021-11-22",
    "relation_id": "c41b43e3-914d-47ee-b545-68b53119e542",
}
create_page_data_from_dict(data, database_id=key_dict["balance_database"])
# %%
