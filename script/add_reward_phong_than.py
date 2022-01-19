from resources.models import PhongThanHistory, PhongThanRewardConfig, Session
from resources.ultils import Creator, Getter
from resources.logger import *
from returns.pipeline import is_successful
from sqlalchemy import func, desc

logger = logging.getLogger('ALive')
from_time = "2021-12-27 00:00:00"
to_time = "2022-01-03 00:00:00"
task = f"Phong Than {from_time.replace(' 00:00:00','')} - {to_time.replace(' 00:00:00','')} "
logger.warning(F"---------- {f'SESSION {task.upper()}':^30} ----------")

session = Session()

results = session.query(
    PhongThanHistory.to_uid.label("u_id"),
    func.sum(PhongThanHistory.amount).label("point")
).filter(
    PhongThanHistory.created_at >= from_time,
    PhongThanHistory.created_at < to_time
).group_by(
    PhongThanHistory.to_uid
).order_by(
    desc("point")
).limit(7).all()

if results:
    logger.info(f"Get ranking success")
else:
    logger.error(f"Get ranking fail")
    exit()

rewards_config = PhongThanRewardConfig.query.all()
for rank in range(0, 7):
    user_id = results[rank][0]
    reward_id = rewards_config[rank].reward_id
    source_id = 2

    reward_info = Getter.reward_info(id=reward_id)
    if not is_successful(reward_info):
        logger.error(F"--- {user_id:>7}: Reward id {reward_id} invalid")
    reward_info = reward_info.unwrap()

    source = Getter.source_info(id=source_id)
    if not is_successful(source):
        logger.error(F"--- {user_id:>7}: Source id {source_id} invalid")
    source = source.unwrap()

    add_reward_result = Creator.add_reward(user_id=user_id, reward_id=reward_id, source_id=source_id)
    if not is_successful(add_reward_result):
        logger.error(F"--- {user_id:>7}: {add_reward_result.failure()}")
    else:
        logger.info(F"--- {user_id:>7}: {source.name:^10} | {reward_info.name}")

logger.warning(F"---------- {f'END SESSION':^30} ----------")
logger.warning(" ")
