from resources.ultils import Getter
from resources.models import Package, UserPackage
import time
from threading import Thread

packages = Package.query.all()


def find_package(id):
    global packages
    for p in packages:
        if p.id == id:
            return p


class UpdateStreamList(Thread):
    def __init__(self, interval):
        Thread.__init__(self)
        self.interval = interval
        self.current = list()

    def run(self):
        while True:
            self.current = Getter.stream_list()
            for stream in self.current:
                download_thumbnail_thread = Thread(target=Getter.thumbnail, args=(stream['streamId'], 360,))
                download_thumbnail_thread.start()
                stream['packages'] = list()
                user_packages = UserPackage.query.filter(
                    UserPackage.u_id == stream['streamId'],
                    UserPackage.p_id != 0,
                    UserPackage.status == "ONGOING"
                )
                for up in user_packages:
                    pkg = find_package(id=up.p_id)
                    stream['packages'].append({
                        'id': up.p_id,
                        'name': pkg.title,
                        'thumbnail': pkg.thumbnail,
                        'icon': pkg.icon
                    })
            time.sleep(self.interval)
