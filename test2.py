#! /usr/bin/env python
import random
import multiprocessing, Queue
import time

import numpy



"""
If the worker fails to allocate memory, add the job back to the queue again and retry later



"""



class Worker(multiprocessing.Process):
 
    def __init__(self, work_queue, result_queue):
 
        # base class initialization
        multiprocessing.Process.__init__(self)
 
        # job management stuff
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.kill_received = False
 
    def run(self):
        while not self.kill_received:
            try:
                job = self.work_queue.get_nowait()
            except Queue.Empty:
                break
 
            print("Starting " + str(job) + " ...")
            A=numpy.array(range(100000000)).reshape(10000,10000)
 
            # store the result
            self.result_queue.put(A[14][14])
            A=[] #clean



def parallal_map(map_function,input_list)
    """
    @param input_list list<A>
    @param map_function f:A->B
    @return list<B>
    """


    raise Exception("not implemented yet")


def parallel_do(do_functions):
    TODO is this easily possible tru lambda or such, does one really need to run functions that doesnt have neither output nor input?
    """
    run all the functions, they must not affect each other (no co-sideeffect) that is the order of execution shouldn't affect the result
    """
    raise Exception("not implemented yet")


if __name__ == "__main__":
 
    num_jobs =10
    num_processes=4
 
    # run
    # load up work queue
    work_queue = multiprocessing.Queue()


    for job in range(num_jobs):
        work_queue.put(job)
 
    # create a queue to pass to workers to store the results
    result_queue = multiprocessing.Queue()
 
    # spawn workers
    for i in range(num_processes):
        worker = Worker(work_queue, result_queue)
        worker.start()
 
    # collect the results off the queue
    results = []
    for i in range(num_jobs):
        print i,"=",result_queue.get()

    print "done"
