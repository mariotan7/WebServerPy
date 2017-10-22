import os
import os.path


class WebApplication():

    def __init__(self, webapps_dir):
        self.__WEBAPPS_DIR = webapps_dir

        self.web_app_collection = {}
        self.directory = ""
        self.servlet_collection = {}

    @property
    def webapps_dir(self):
        return self.__WEAPPS_DIR

    def web_application(self, directory):

        self.directory = directory
        path_obj = self.__WEBAPPS_DIR + os.sep + directory
