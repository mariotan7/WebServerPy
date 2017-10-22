import abc


class HttpServletRequest(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_method(self):
        raise NotImplemented

    @abc.abstractmethod
    def get_parameter(self, name):
        raise NotImplemented

    @abc.abstractmethod
    def get_parameter_values(self, env):
        raise NotImplemented
