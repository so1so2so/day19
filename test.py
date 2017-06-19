#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def log(func):
    def wrapper(*args, **kwargs):
        print 'call %s():' % func.__name__
        return func(*args, **kwargs)
    return wrapper

@log
def now():
    print '2013-12-25'
now()