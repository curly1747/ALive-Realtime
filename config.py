class DatabaseConfig:
    HOST = "119.82.141.211"
    PORT = 3306
    USERNAME = "master"
    PASSWORD = "QGxpdmVtQHN0ZXI="
    URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}'


class ALiveConfig:
    AUTHORIZATION = 'a11b33fb1edd9a82fd09773e1d3966869d15420f7662bf6d2865fb848c889155_1053_J8kur7k4ZZ_1649912964055'
    TOOL_URL = 'https://tools.alive.vn/cms/v1/'
    API_URL = 'https://api.alive.vn/v2/'
