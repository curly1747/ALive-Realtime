from resources.models import Idol, IdolRegistry, Session
from resources.ultils import Creator
import pandas as pd
import logging

data = pd.read_csv("insert_idol.csv")
session = Session()

for index, data in data.iterrows():
    info = {
        'is_verified': "001"
    }
    for col in data.index:
        info[col] = str(data[col])

    new_idol = Idol(
        u_id=info['u_id'],
        name=info['name'],
        facebook=info['facebook'],
        email=info['email'],
        phone=info['phone'],
        agency_id=info['agency_id'],
        is_verified=info['is_verified']
    )

    new_idol_register = IdolRegistry(
        idol_id=info['u_id'],
        agency_id=info['agency_id'],
        status="WAITING"
    )

    try:
        session.add(new_idol)
        session.add(new_idol_register)
        session.commit()
    except Exception as e:
        logging.exception(f"{new_idol.u_id}\t{e}")
        session.rollback()

    if info['package_id']:
        Creator.set_package(user_id=info['u_id'], new_package=info['package_id'])

    Creator.add_reward(user_id=info['u_id'], source_id=3, reward_id=311)
    print(new_idol.u_id, new_idol.name)
