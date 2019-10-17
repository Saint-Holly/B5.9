#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-
"""
Элемент класса Stopwatch может быть использован как декоратор для функции.
Выводит на консоль среднее время выполнения функции, принимает в качестве аргумента
количесто запусков функции для определения среднего времени.

Элемент класса Stopwatch может быть использован как контекстный менеджер, выводящий 
среднее вменя выполнения функции. В качестве параметров принимает имя функции, параметр
функции, колиечество запусков функции для определения среднего времени.
"""

import time

class Stopwatch():
    def __init__(self, num_runs, func=None, param=None):
        self.num_runs = num_runs
        self.func = func
        self.param = param

    def __enter__(self):
        return self

    def __exit__(self, *args):
        avg_time = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.func(self.param)
            t1 = time.time()
            avg_time += (t1-t0)
        avg_time /= self.num_runs
        print("Количество запусков функции {}({}): {}".format(self.func.__name__, self.param, self.num_runs))
        print("Среднее время выполнения (сек): %.5f" % avg_time)

    def __call__(self, *args):
        def decorator(func):
            def wrap(param):
                avg_time = 0
                for i in range(self.num_runs):
                    t0 = time.time()
                    result = func(param)
                    t1 = time.time()
                    avg_time += (t1-t0)
                avg_time /= self.num_runs
                print("Количество запусков функции {}({}): {}".format(func.__name__, param, self.num_runs))
                print("Среднее время выполнения (сек): %.5f" % avg_time)
                return result
            return wrap
        return decorator

#sw = Stopwatch(num_runs=10)
#@sw()
def fib(n):
    fib =[0]
    for i in range(1, n+1):
        if i < 3:
            fib.append(i)
        else:
            fib.append(fib[i-1]+fib[i-2])
    return fib[n] 

with Stopwatch(num_runs=10, func=fib, param=1000) as sw:      
    sw.func(sw.param)
    
