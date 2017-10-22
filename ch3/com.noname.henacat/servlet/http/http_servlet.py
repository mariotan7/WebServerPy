import abc


class HttpServlet(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def do_get(self, req, resp):
        raise NotImplemented

    @abc.abstractmethod
    def do_post(self, req, resp):
        raise NotImplemented

    def service(self, req, resp):

        if req.get_method().equals("GET"):
            self.do_get(req, resp)
        elif req.get_method().equals("POST"):
            self.do_post(req, resp)
