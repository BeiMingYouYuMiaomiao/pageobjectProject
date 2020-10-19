# -*- coding: UTF-8 -*-
import yaml


class Utils:
    def data_from_yaml(path):
        with open(path) as f:
            # 读取出文件是一个dict
            yaml_datas=yaml.safe_load(f)
            # 定义一个list，存放文件中的读取的dict中的yaml_datas['params']对应的value
            params=yaml_datas['params']
            # 定义一个set集合 ，存放所有keywords，并且去重，就是参数与使用时的变量名称
            keys =set()
            # 定义一个列表，存放所有value 为了参数使用时，作为参数使用
            values = []

        """
        文件内格式
        params:
             - keywords: alibaba
             - keywords: jd
             - keywords: baidu
        """
        if isinstance(params, list):
            for row in params:
                if isinstance(row, dict):
                    for key in row.keys():
                        keys.add(key)
                        print('row.values()的属性：',type(row.values()))
                        """
                        radiansdict.keys() 返回一个迭代器，可以使用 list() 来转换为列表
                        """
                        values.append(list(row.values())[0])
        var_names = ','.join(keys)
        return {'keys':var_names,'values':values}
