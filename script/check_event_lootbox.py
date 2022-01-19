from resources.models import LootboxReward, ItemInfo, UserMaterial, SendGiftHistory, Transactions
from sqlalchemy import func
from datetime import datetime
import json


def find_item(items, id):
    for item in items:
        if item.id == id:
            return item


this_month_first_moment = datetime.now().replace(day=1)

opened_boxes = LootboxReward.query.filter(
    LootboxReward.box_id.in_((14, 18)),
    func.date(LootboxReward.modified_time) > this_month_first_moment
).all()

items = ItemInfo.query.all()

users = dict()

for box in opened_boxes:
    result = json.loads(box.result)[0]
    if box.u_id not in users.keys():
        super_fan = UserMaterial.query.filter_by(u_id=box.u_id, material_id=16).first()
        super_fan = 0 if not super_fan else super_fan.amount

        spend = 0
        gifts = SendGiftHistory.query.filter(
            SendGiftHistory.from_uid == box.u_id,
            SendGiftHistory.time > '2021-10-21'
        ).all()
        for gift in gifts:
            spend += gift.diamond

        topup = 0
        transactions = Transactions.query.filter(
            Transactions.uid == box.u_id,
            Transactions.status == "SUCCESS",
            Transactions.update_at > '2021-10-21'
        ).all()
        for transaction in transactions:
            topup += (transaction.diamond + transaction.bonus_diamond)

        users[box.u_id] = dict({
            'diamond_spend': spend,
            'diamond_topup': topup,
            'super_fan_point': super_fan,
            'rewards': list()
        })
    rewards = users[box.u_id]['rewards']
    match = False
    for reward in rewards:
        if reward['id'] == result['pieceId']:
            reward['amount'] += result['pieceAmount']
            match = True
            break
    if not match:
        rewards.append({
            'id': result['pieceId'],
            'item': find_item(items, result['pieceId']).name,
            'amount': result['pieceAmount'],
        })

print(json.dumps(users, indent=4))
