#%%
%reload_ext autoreload
%autoreload 2
#%%
from requests.api import get
from helpers import get_keys_dict, read_database, query_database, create_page_in_database, get_page
import json

#%%
key_dict = get_keys_dict()


#%%
res = read_database(
    database_id=key_dict["expenses_test_id"],
    token=key_dict["internal_integration_token"],
)

# %%
res = query_database(
    database_id=key_dict["expenses_test_id"],
    token=key_dict["internal_integration_token"],
)
# %%
res = create_page_in_database(
    database_id=key_dict["expenses_test_id"],
    token=key_dict["internal_integration_token"],
)

# %%
res = get_page(
    page_id=key_dict['test_expense_id'], 
    token=key_dict["internal_integration_token"],
)

# %%
