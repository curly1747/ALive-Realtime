from resources.ultils import Creator, Formatter, Getter
from resources.logger import *
from returns.pipeline import is_successful
from schedule import every, repeat, run_pending
import time
import datetime

logger = logging.getLogger('ALive')


# @repeat(every().hour.at(":00"))
# def idol_star_1d_update_badge():
#     reward_id = [482, 483, 484]
#     source_id = 2
#
#     idol_daily_rank = Getter.idol_star_ranking_1d(limit=3)
#
#     if not is_successful(idol_daily_rank):
#         logger.error(F"{idol_daily_rank.failure()}")
#     idol_daily_rank = idol_daily_rank.unwrap()
#
#     source = Getter.source_info(id=source_id)
#     if not is_successful(source):
#         logger.error(F"--- Source id {source_id} invalid")
#     source = source.unwrap()
#
#     for rank in range(0, 3):
#         if rank < len(idol_daily_rank):
#
#             reward_info = Getter.reward_info(id=reward_id[rank])
#             if not is_successful(reward_info):
#                 logger.error(F"--- Reward id {reward_id[rank]} invalid")
#             reward_info = reward_info.unwrap()
#
#             user_id = idol_daily_rank[rank].idol_id
#             result = Creator.add_reward(user_id=user_id, reward_id=reward_id[rank], source_id=source_id)
#             if not is_successful(result):
#                 logger.error(F"--- {user_id:>7}: {result.failure()}")
#             else:
#                 logger.info(F"--- {user_id:>7}: {source.name:^10} | {reward_info.name}")

@repeat(every().hour.at(":00"))
def top_star_idol_daily_hourly_update_badge():
    rewards = [482, 483, 484]
    source_id = 2

    from_time = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    to_time = from_time.replace(hour=23, minute=59, second=59)
    epoch = datetime.datetime.fromtimestamp(0)
    from_time = int((from_time - epoch).total_seconds())
    to_time = int((to_time - epoch).total_seconds())

    top_idol = Getter.rank_by_material(
        material_id=2,
        from_time=from_time,
        to_time=to_time,
        scheme_id=2
    )

    if not is_successful(top_idol):
        logger.error(F"{top_idol.failure()}")
    top_idol = top_idol.unwrap()

    source = Getter.source_info(id=source_id)
    if not is_successful(source):
        logger.error(F"--- Source id {source_id} invalid")
    source = source.unwrap()

    for rank in range(0, 3):
        if rank < len(top_idol):
            reward_id = rewards[rank]
            reward_info = Getter.reward_info(id=reward_id)
            if not is_successful(reward_info):
                logger.error(F"--- Reward id {reward_id} invalid")
            reward_info = reward_info.unwrap()

            user_id = top_idol[rank]['profile']['uid']
            result = Creator.add_reward(user_id=user_id, reward_id=reward_id, source_id=source_id)
            if not is_successful(result):
                logger.error(F"--- {user_id:>7}: {result.failure()}")
            else:
                logger.info(F"--- {user_id:>7}: {source.name:^10} | {reward_info.name}")


@repeat(every().hour.at(":00"))
def main_event_hourly_update_badge():
    reward_id = 481
    source_id = 13

    top_idol = Getter.rank_by_material(
        material_id=15,
        from_time=1647277200,
        to_time=1648313999,
        scheme_id=7
    )
    if not is_successful(top_idol):
        logger.error(F"{top_idol.failure()}")
    top_idol = top_idol.unwrap()

    source = Getter.source_info(id=source_id)
    if not is_successful(source):
        logger.error(F"--- Source id {source_id} invalid")
    source = source.unwrap()

    reward_info = Getter.reward_info(id=reward_id)
    if not is_successful(reward_info):
        logger.error(F"--- Reward id {reward_id} invalid")
    reward_info = reward_info.unwrap()

    for rank in range(0, 3):
        user_id = top_idol[rank]['profile']['uid']
        result = Creator.add_reward(user_id=user_id, reward_id=reward_id, source_id=source_id)
        if not is_successful(result):
            logger.error(F"--- {user_id:>7}: {result.failure()}")
        else:
            logger.info(F"--- {user_id:>7}: {source.name:^10} | {reward_info.name}")


@repeat(every().hour.at(":00"))
def game_center_hourly_update_badge():
    reward_id = 485
    source_id = 6

    top = Getter.rank_tra_sua(
        limit=3
    )
    if not is_successful(top):
        logger.error(F"{top.failure()}")
    top = top.unwrap()

    source = Getter.source_info(id=source_id)
    if not is_successful(source):
        logger.error(F"--- Source id {source_id} invalid")
    source = source.unwrap()

    reward_info = Getter.reward_info(id=reward_id)
    if not is_successful(reward_info):
        logger.error(F"--- Reward id {reward_id} invalid")
    reward_info = reward_info.unwrap()

    for rank in range(0, 3):
        if rank < len(top):
            user_id = top[rank]['user_id']
            result = Creator.add_reward(user_id=user_id, reward_id=reward_id, source_id=source_id)
            if not is_successful(result):
                logger.error(F"--- {user_id:>7}: {result.failure()}")
            else:
                logger.info(F"--- {user_id:>7}: {source.name:^10} | {reward_info.name}")


while True:
    run_pending()
    time.sleep(1)
