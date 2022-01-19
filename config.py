class DatabaseConfig:
    HOST = "119.82.141.211"
    PORT = 3306
    USERNAME = "master"
    PASSWORD = "QGxpdmVtQHN0ZXI="
    URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'


class ALiveConfig:
    AUTHORIZATION = 'e710918a155fa940ad44a8609f16cdd224c702d383538b64361520d3db6b9b4e_1053_pKKDS2MZqy_1642756428301'
    TOOL_URL = 'https://tools.alive.vn/cms/v1/'
    API_URL = 'https://api.alive.vn/'
