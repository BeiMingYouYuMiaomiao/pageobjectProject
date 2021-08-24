# -*- coding: UTF-8 -*-
# class Foo:
#     def __f1(self):
#         print('Foo.f1')
#
#     def f2(self):
#         print('Foo.f2')
#         self.__f1()
#
#
# class Bar(Foo):
#     def __f1(self):
#         print('Bar.f1')
#
#
# obj=Bar()
# obj.f2()

# ============================fenge============================
# class A:
#     def test(self):
#         print('from A')
#         super().test1()
#
# class B:
#     def test1(self):
#         print('from B')
#
#
# class C(A,B):
#     def test1(self):
#         print('from c')
#
# obj=C()
# obj.test()

# ============================fenge============================
# X = type('X', (), dict(a=1))
# print(X.a)


class A(object):
    pass
