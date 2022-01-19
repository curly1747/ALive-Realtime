from resources.ultils import Creator, Formatter, Getter
from resources.logger import *
from returns.pipeline import is_successful

task = "Main Event 11/2021"

title = f"SESSION {task.upper()}"
logger = logging.getLogger('ALive')

# Source 15 -> Gift Hunter
# Source 13 -> Main Event

config = """
170058	237	13
57322	238	13
5888	239	13
3893	240	13
181611	240	13
29287	240	13
87503	240	13
150922	240	13
195555	240	13
115712	240	13
72178	237	13
126033	238	13
2701	239	13
150565	240	13
194705	240	13
196990	240	13
5698	240	13
2322	240	13
19124	240	13
192675	240	13
126033	241	13
2701	242	13
170058	243	13
150565	244	13
181611	244	13
57322	244	13
196990	244	13
3893	244	13
72178	244	13
195555	244	13
1152	245	13
206272	246	13
2233	247	13
98507	248	13
49527	248	13
200359	248	13
169061	248	13
57322	248	13
200361	248	13
195385	248	13
"""

logger.warning(F"---------- {f'SESSION {task.upper()}':^30} ----------")

configs = Formatter.split_config(data=config, param_count=3, require=True)

if not is_successful(configs):
    logger.error(configs.failure())
configs = configs.unwrap()
logger.info(f"Config: {configs}")

for config in configs:
    user_id = config[0]
    reward_id = config[1]
    source_id = config[2]

    reward_info = Getter.reward_info(id=reward_id)
    if not is_successful(reward_info):
        logger.error(F"--- {user_id:>7}: Reward id {reward_id} invalid")
    reward_info = reward_info.unwrap()

    source = Getter.source_info(id=source_id)
    if not is_successful(source):
        logger.error(F"--- {user_id:>7}: Source id {source_id} invalid")
    source = source.unwrap()

    result = Creator.add_reward(user_id=user_id, reward_id=reward_id, source_id=source_id)
    if not is_successful(result):
        logger.error(F"--- {config[0]:>7}: {result.failure()}")
    else:
        logger.info(F"--- {config[0]:>7}: {source.name:^10} | {reward_info.name}")

logger.warning(F"---------- {f'END SESSION':^30} ----------")
logger.warning(" ")
