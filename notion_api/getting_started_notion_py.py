#%%
from notion.client import NotionClient

#%%
with open("../cache/secret.txt", "r") as secret:
    token_v2 = secret.read()
#%%
client = NotionClient(token_v2=token_v2)

# %%
page = client.get_block(
    "https://www.notion.so/Life-Wiki-f7556348341541fbbd1334ec68e96187"
)

# %%
