# -*- coding: UTF-8 -*-
def dog(name):
    print('开始。。。%s ' %name)
    while True:
        x = yield
        print('结束。。。'+ x)

f=dog('哈哈哈')
f.send(None)
f.send('略略略')


l=['dss','qws','wer','wer','llo','qwdds']
new_l=[name for name in l if name.endswith('s')]
print(new_l)

new_l2=[name.upper() for name in l]
print(new_l2)