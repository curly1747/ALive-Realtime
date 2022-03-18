from resources.ultils import Creator, Formatter, Getter
from resources.logger import *
from returns.pipeline import is_successful

task = "Bu NV Main Event 03/2021"

title = f"SESSION {task.upper()}"
logger = logging.getLogger('ALive')

# Source 15 -> Gift Hunter
# Source 13 -> Main Event

config = """
219020	438	13
219020	439	13
219020	440	13
219020	441	13
219020	442	13
219020	443	13
219020	444	13
12398	438	13
12398	439	13
12398	440	13
12398	441	13
12398	442	13
213235	438	13
213235	439	13
213235	440	13
27744	438	13
27744	439	13
27744	440	13
13692	438	13
13692	439	13
13692	440	13
13692	441	13
13692	442	13
13692	443	13
13692	444	13
3553	438	13
16459	438	13
16459	439	13
16459	440	13
2493	438	13
2493	439	13
2493	440	13
2493	441	13
2493	442	13
39515	438	13
39515	439	13
39515	440	13
39515	441	13
39515	442	13
22919	438	13
22919	439	13
8306	438	13
8306	439	13
2466	438	13
2466	439	13
2466	440	13
2466	441	13
2466	442	13
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
