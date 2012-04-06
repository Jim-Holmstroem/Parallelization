#! /usr/bin/env python
from multiprocessing import Pool
import numpy


def f(x):
    print "f(",x,")"
    return numpy.sum(x+numpy.array(range(10**7)))


if __name__=='__main__':
    pool = Pool(processes=4)
    print pool.map(f,range(32))

