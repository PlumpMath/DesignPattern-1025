# encoding=utf8

import threading
import time


class Singleton(object):

    def __new__(cls, *args):
        if not hasattr(cls, '_instance'):
            origin = super(Singleton, cls)
            cls._instance = origin.__new__(cls, *args)
        return cls._instance


class Bus(Singleton):

    lock = threading.RLock()

    def send_data(self, data):
        self.lock.acquire()
        time.sleep(3)
        print "sending signal data...", data
        self.lock.release()


class VisitEntity(threading.Thread):

    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.send_data(self.name)


if __name__ == '__main__':
    for i in range(3):
        print "Entity %d begin to run..." % i
        my_entity = VisitEntity()
        my_entity.setName("Entity_"+str(i))
        my_entity.start()
