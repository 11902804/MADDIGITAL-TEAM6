class Client:
    def __init__(self, sid):
        self.__sid = sid
        self.__wid = None

    def get_sid(self):
        return self.__sid

    def get_wid(self):
        return self.__wid

    def set_wid(self, wid):
        self.__wid = wid
