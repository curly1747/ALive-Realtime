from resources.ultils import Getter

stream_list = Getter.stream_list()
for stream in stream_list:
    print(stream)
    print(stream['streamId'], Getter.thumbnail(user_id=stream['streamId'], width=360))
