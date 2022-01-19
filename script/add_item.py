from resources.ultils import Creator
import pandas as pd

data = pd.read_csv('add_item.csv')

for index, data in data.iterrows():
    print(data['u_id'], data['amount'], Creator.add_item(user_id=data['u_id'], item_id=29, amount=data['amount']))
