# Copyright Karlheinz Niebuhr
import time

import sys

#  This part of code is to calculate how long a code will take to run
def measure(method):
    def run(*args, **kwargs): 
        if sys.platform == 'win32':
            # time.clock() resolution is very good on Windows, but very bad on Unix.
            # ***** For now this doesn't seem to work well so we will just use time.clock() *****

            '''
            check if python is >= V 3.3 
            if False: #(sys.version_info[0] == 3 and sys.version_info[1] == 3):
                run_time = time.process_time()
                function( arg )
                #run_time = time.process_time()
            '''
            start = time.clock()
            #run the function and save the result
            result = method(*args, **kwargs)
            run_time = time.clock() - start
            print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
            
        else:
            # On most other platforms the best timer is time.time
            start = time.time()
            #run the function and save the result
            result = method(*args, **kwargs)
            run_time = time.time() - start
            print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
            
        return run_time
    return run


def run_time(method,*args, **kwargs): 
    if sys.platform == 'win32':
        # time.clock() resolution is very good on Windows, but very bad on Unix.
        # ***** For now this doesn't seem to work well so we will just use time.clock() *****

        '''
        check if python is >= V 3.3 
        if False: #(sys.version_info[0] == 3 and sys.version_info[1] == 3):
            run_time = time.process_time()
            function( arg )
            #run_time = time.process_time()
        '''
        start = time.clock()
        #run the function and save the result
        result = method(*args, **kwargs)
        run_time = time.clock() - start
        #print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
        
    else:
        # On most other platforms the best timer is time.time
        start = time.time()
        #run the function and save the result
        result = method(*args, **kwargs)
        run_time = time.time() - start
        #print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
        
    return run_time


def avgof(function, times_average, *args, **kwargs):
    count = 0
    track = 0

    while count < times_average:
        time = run_time(function,*args, **kwargs)
        print time
        track += time
        count += 1
    return track/times_average


def compare(functionA, functionB, times_average, loops=10, *args, **kwargs):
    # loop n times
    i = 0
    totalA = 0.0
    totalB = 0.0                      
    while i < loops:
        first = avgof(functionA, times_average, *args, **kwargs)
        second = avgof(functionB, times_average, *args, **kwargs)
        if first < second:
            print(functionA.__name__+' is ' + str(second/first) + ' times faster')
            
        else:
            print(functionB.__name__+' is ' + str(first/second) + ' times faster')
            

        totalA+=first
        totalB+=second
        i += 1
    if first < second:
        print("On average "+ functionA.__name__+ " is "+str( "{0:0f} %".format(totalB/totalA * 10) )+' faster than '+functionB.__name__)
    elif second < first:
        print("On average "+ functionB.__name__+ " is "+str( "{0:0f} %".format(totalA/totalB * 10) )+' faster than '+functionA.__name__)

def measureold(function, parameter, times_average=1, loops=10):
    # loop n times
    i = 0
    temp = 0.0
    totaltime = 0.0
    while i < loops:
        temp = avgof(function, parameter, times_average)
        print("Average in loop "+str(i)+": "+str(temp))
        totaltime += temp
        i += 1

    print("Total time: "+ str(totaltime))