#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A(object):

    def foo(self):
        print('foo of A')


class B(A):
    pass


class C(A):

    def foo(self):
        print('foo fo C')


class D(B, C):
    pass


class E(D):

    def foo(self):
        # print('foo in E')
        # super().foo()
        super(B, self).foo()
        # super(C, self).foo()


if __name__ == '__main__':
    # d = D()
    # d.foo()
    e = E()
    e.foo()
