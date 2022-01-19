from resources.models import LootboxReward, RewardDiamondHistory
from sqlalchemy import func, desc
import json
import csv

with open('list.csv', newline='') as f:
    reader = csv.reader(f)
    users_id = [int(row[0]) for row in reader]

audit_logs = list()

opened_boxes = LootboxReward.query.filter(
    func.date(LootboxReward.modified_time) == '2021-10-17',
    LootboxReward.u_id.in_(users_id),
    LootboxReward.box_id == 17,
    LootboxReward.result.like('%"pieceId":5%')
).order_by(desc(LootboxReward.modified_time)).all()

for box in opened_boxes:
    audit_logs.append(box.audit_id)

transactions = RewardDiamondHistory.query.filter(
    RewardDiamondHistory.audit_id.in_(audit_logs)
).all()

for trans in transactions:
    print(f"{trans.id},{trans.to_uid},{trans.amount},{trans.diamond_trans_id},{trans.audit_id},{trans.created_at}")
