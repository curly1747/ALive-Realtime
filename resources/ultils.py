import os
from config import ALiveConfig
import requests
from returns.result import Success, Failure
from sqlalchemy import desc

request_session = requests.Session()
request_session.cookies['authorization'] = ALiveConfig.AUTHORIZATION
request_session.headers['authorization'] = ALiveConfig.AUTHORIZATION


class Getter:

    @staticmethod
    def stream_list(page=1, count=1000, stream_type="mobilecam", platform=11, app_version="1.0.0"):
        import requests
        url = f"https://api.alive.vn/api_stream/get_stream_list?page={page}&count={count}&type={stream_type}&platform={platform}&appversion={app_version}"
        response = requests.post(url)
        try:
            return response.json()['data']
        except Exception as e:
            return list()

    @staticmethod
    def thumbnail(user_id, width=360):
        import ffmpeg

        input_file = f"https://stream.alive.vn/hls/{user_id}/index.m3u8"
        output_file = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'static', 'screenshot', f"{user_id}.jpg"))
        try:
            (
                ffmpeg
                    .input(input_file)
                    .filter('scale', width, -1)
                    .output(output_file, vframes=1)
                    .overwrite_output()
                    .run(quiet=True)
            )
            return True
        except ffmpeg.Error as e:
            return False

    @staticmethod
    def current_timestamp():
        from datetime import timezone, datetime
        return int(datetime.now().replace(tzinfo=timezone.utc).timestamp())

    @staticmethod
    def reward_info(id):
        from resources.models import RewardInfo
        result = RewardInfo.query.filter_by(id=id).first()
        if not result:
            return Failure(result)
        return Success(result)

    @staticmethod
    def source_info(id):
        from resources.models import SourceInfo
        result = SourceInfo.query.filter_by(id=id).first()
        if not result:
            return Failure(result)
        return Success(result)

    @staticmethod
    def rank_by_material(material_id, from_time, to_time, scheme_id, limit=10):
        r = request_session.get(
            f'{ALiveConfig.API_URL}gami/ranking/material?materialId={material_id}&fromTime={from_time}&toTime={to_time}&limit={limit}&schemeId={scheme_id}')
        try:
            response = r.json()
            return Success(response['data']) if response['status']['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})

    @staticmethod
    def rank_tra_sua(limit=3):
        r = request_session.get(f'https://trasua.alive.vn/v1/ranking?limit={limit}')
        try:
            response = r.json()
            return Success(response['data']['users']) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})

    @staticmethod
    def idol_star_ranking_1d(limit=10):
        from resources.models import IdolStarRanking1D
        result = IdolStarRanking1D.query.order_by(desc(IdolStarRanking1D.total)).limit(limit).all()
        if not result:
            return Failure(result)
        return Success(result)


class Formatter:
    @staticmethod
    def datetime_to_unix(dt):
        from datetime import timezone
        return int(dt.replace(tzinfo=timezone.utc).timestamp())

    @staticmethod
    def split_config(data, param_count=None, require=False):
        data = data.split("\n")
        result = list()
        if not data:
            return Failure('Wrong format or empty')
        for d in data:
            if d:
                d_list = d.split("\t")
                if param_count:
                    if len(d_list) is not param_count:
                        print(d_list)
                        return Failure(f'"{d}" missing param')
                    if require:
                        for p in d_list:
                            if p == "":
                                return Failure(f'"{d}" {param_count} params is required')
                result.append(d_list)
        return Success(result)


class Creator:

    @staticmethod
    def add_reward(user_id, reward_id, source_id):
        data = {
            'user_id': int(user_id),
            'reward_id': str(reward_id),
            'source': int(source_id)
        }
        r = request_session.post(f'{ALiveConfig.TOOL_URL}/add-user-item/reward', json=data)
        try:
            response = r.json()
            return Success(response) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})

    @staticmethod
    def add_item(user_id, item_id, amount):
        data = {
            'user_id': int(user_id),
            'item_id': str(item_id),
            'amount': int(amount)
        }
        r = request_session.put(f'{ALiveConfig.TOOL_URL}/user_inventory/add', json=data)
        try:
            response = r.json()
            return Success(response) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})

    @staticmethod
    def set_package(user_id, new_package):
        data = {
            'user_id': user_id,
            'new_package': new_package,
            'old_package': 0
        }
        r = request_session.put(f'{ALiveConfig.TOOL_URL}/user_package', json=data)
        try:
            response = r.json()
            return Success(response) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})


class Actor:

    @staticmethod
    def ban_user(user_id, reason):
        r = request_session.put(f'https://tools.alive.vn/cms/v1/user/ban', json={'user_id': user_id, 'message': reason})
        try:
            response = r.json()
            return Success(response) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})

    @staticmethod
    def delete_stream(room_id):
        r = request_session.delete(f'https://tools.alive.vn/cms/v1/room', json={'room_id': int(room_id)})
        try:
            response = r.json()
            return Success(response) if response['code'] == 0 else Failure(response)
        except:
            return Failure({'message': 'Unknown error'})
