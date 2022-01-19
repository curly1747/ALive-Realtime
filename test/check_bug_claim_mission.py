from resources.models import RewardHistory, Transactions, LootboxReward, FCMToken, Diamond, LootboxHistory, session
from sqlalchemy import func, desc
import json

rewards = RewardHistory.query.filter(
    RewardHistory.status == "END",
    func.date(RewardHistory.modified_at) == '2021-10-17',
    RewardHistory.source == 20
).all()

unique_id = dict()

for reward in rewards:
    reward_data = reward.data['info'][0]
    if "pieceId" in reward_data:
        if reward_data['pieceId'] == 40:
            unique_id[reward.to_uid] = 0

cheat = 0

for uid in unique_id.keys():
    trans = Transactions.query.filter(
        Transactions.uid == uid,
        Transactions.status == "SUCCESS",
        func.date(Transactions.update_at) == '2021-10-17',
    ).all()
    payment = 0
    diamond_reward = 0
    opened_boxes = []
    received_boxes = []
    total_received_boxes = 0
    current_diamond = 0
    opened_duration = 0
    for tran in trans:
        payment += tran.diamond
    if payment == 0:
        cheat += 1
        opened_boxes = LootboxReward.query.filter(
            func.date(LootboxReward.modified_time) == '2021-10-17',
            LootboxReward.u_id == uid,
            LootboxReward.box_id == 17
        ).order_by(desc(LootboxReward.modified_time)).all()
        if len(opened_boxes) >= 2:
            opened_duration = int((opened_boxes[0].modified_time - opened_boxes[-1].modified_time).total_seconds())
        received_boxes = LootboxHistory.query.filter(
            func.date(LootboxHistory.created_at) == '2021-10-17',
            LootboxHistory.to_uid == uid,
            LootboxHistory.box_id == 17
        ).all()
        for received_box in received_boxes:
            total_received_boxes += received_box.amount
        for box in opened_boxes:
            result = json.loads(box.result)
            if result[0]['pieceId'] == 26:
                diamond_reward += result[0]['pieceAmount']
    current_diamond = Diamond.query.filter_by(uid=uid).first()
    try:
        current_diamond = current_diamond.total
    except Exception as e:
        current_diamond = 0
    token = FCMToken.query.filter_by(u_id=uid).first()
    try:
        fcm_token = token.token
        device_id = token.device_id
    except:
        fcm_token = ""
        device_id = ""
    print(f"{uid}\t{payment}\t{total_received_boxes}\t{len(opened_boxes)}\t{diamond_reward}\t{current_diamond}\t{opened_duration}\t{fcm_token}\t{device_id}")

print(cheat)
