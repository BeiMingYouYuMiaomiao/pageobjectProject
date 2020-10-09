# -*- coding: UTF-8 -*-
import yaml
from appium.webdriver import webdriver
from appium.webdriver.webdriver import WebDriver



class BasePage:
    _black_list=[]
    _error_count = 0
    _error_max = 10
    _parameter = {}

    def __init__(self,driver:WebDriver =None):
        self._driver = driver


    def find(self,by,locator = None):
        #循环查找
        try:
            element = self._driver.find_elements(*by,locator) if isinstance(by,tuple) else self._driver.find_element(by,locator)
            self._error_count = 0
            return element
        except Exception as e:
            self._error_count +=1
            if self._error_count>=self._error_max:
                raise e
            for black in self._black_list:
                elements=self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by,locator)
            raise e
    def send(self,value,by,locator=None):
        try:
            self.find(by,locator).send_keys(value)
            self._error_count = 0
        except Exception as e:
            self._error_count +=1
            if self._error_count>=self._error_max:
                raise e
            for black in self._black_list:
                elements=self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value,by,locator)
            raise e




    def steps(self,path):
        # global el
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)

            for step in steps:
                if "by" in step.keys():
                    el = self.find(step['by'],step['locator'])
                if "action" in step.keys():
                    if "click" == step['action']:
                        el.click()
                    if "send" == step['action']:
                        # {value_key}
                        content: str = step['value']
                        # 循环字典里的keys，将字典中的value值，全部替换成对应的字典中的value值
                        for param in self._parameter.keys():
                            # 字符串的格式化，
                            """
                            string="hello" 
                            %s打印时结果是hello  
                            print "string=%s" % string   # output: string=hello  

                            """
                            # content = content.replace("{param}",self._parameter[param])
                            # {value_key} 这个字符串，替换字典中的key如果等于value_key，那么进行替换，将字典中value_key的value值替换
                            # 例如 value_key：aass   那么替换后 类似于这个意思  step['value']=aass
                            content = content.replace("{%s}" % param, self._parameter[param])
                        self.send(content, step['by'], step['locator'])




















