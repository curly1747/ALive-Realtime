from resources.models import Idol, Session
import pandas as pd

data = pd.read_csv('update_idol_info.csv')
session = Session()
idol_list = []

for index, data in data.iterrows():
    idol = session.query(Idol).filter_by(u_id=data["u_id"]).first()
    print(data["u_id"])
    if pd.notna(data["name"]):
        idol.name = data["name"]
    if pd.notna(data["identify"]):
        idol.identify = data["identify"]
    if pd.notna(data["facebook"]):
        idol.facebook = data["facebook"]
    if pd.notna(data["email"]):
        idol.email = data["email"]
    if pd.notna(data["phone"]):
        idol.phone = data["phone"]
    if pd.notna(data["bank_number"]):
        idol.bank_number = data["bank_number"]
    if pd.notna(data["bank_name"]):
        idol.bank_name = data["bank_name"]
    if pd.notna(data["bank_branch"]):
        idol.bank_branch = data["bank_branch"]

session.commit()
