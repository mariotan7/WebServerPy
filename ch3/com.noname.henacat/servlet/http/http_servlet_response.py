import abc


class HttpServletResponce(metaclass=abc.ABCMeta):

    def __init__(self):
        self.__SC_OK = 200
        self.__SC_FOUND = 302

    @property
    def SC_OK(self):
        return self.__SC_OK

    @property
    def SC_FOUND(self):
        return self.__SC_FOUND

    @abc.abstractmethod
    def set_content_type(self, content_type):
        raise NotImplemented

    @abc.abstractmethod
    def set_character_encoding(self, charset):
        raise NotImplemented

    @abc.abstractmethod
    def get_writer(self):
        raise NotImplemented

    @abc.abstractmethod
    def send_redirect(self, location):
        raise NotImplemented

    @abc.abstractmethod
    def set_status(self, sc):
        raise NotImplemented
