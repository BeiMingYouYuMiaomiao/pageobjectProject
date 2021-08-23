# -*- coding: UTF-8 -*-
import requests



class BaseApi:




    def send_api(self,data:dict,params):
        self.session = requests.session()
        self.session.params = params
        return self.session.request(**data).json()