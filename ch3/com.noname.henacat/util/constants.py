class Constants():
    def __init__(self):
        self.__SERVER_NAME = "localhost:8001"

    @property
    def server_name(self):
        return self.__SERVER_NAME
