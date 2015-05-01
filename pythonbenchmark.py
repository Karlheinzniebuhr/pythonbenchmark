# Author: Karlheinz Niebuhr
# Copyright (c) 2015
# License: see License.txt

import time
import sys

#  This part of code is to calculate how long a code will take to run
def measure(method):
    def run(*args, **kwargs): 
        if sys.platform == 'win32':
            # time.clock() resolution is very good on Windows, but very bad on Unix.
            
            '''
            ***** For now process_time() doesn't seems to work well so we'll just use time.clock() *****

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
            # On non Windows platforms the best timer is time.time
            start = time.time()
            #run the function and save the result
            result = method(*args, **kwargs)
            run_time = time.time() - start
            print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
            
        return result
    return run


def run_time(method,*args, **kwargs): 
    if sys.platform == 'win32':
        # time.clock() resolution is very good on Windows, but very bad on Unix.

        start = time.clock()
        #run the function and save the result
        result = method(*args, **kwargs)
        run_time = time.clock() - start
        #print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
        
    else:
        # On non Windows platforms the best timer is time.time
        start = time.time()
        #run the function and save the result
        result = method(*args, **kwargs)
        run_time = time.time() - start
        #print('%r (%r, %r) %2.20f sec' % (method.__name__, args, kwargs, run_time))
        
    return run_time


def compare(functionA, functionB, times_average, *args, **kwargs):
    # loop n times
    i = 0
    totalA = 0.0
    totalB = 0.0
    
    '''
    Normalizer
    We intercalate the function calls because python tends to execute the second function faster if we first loop over functionA and then over functionB   

    '''
    for i in range(times_average):
        totalA += run_time(functionA,*args, **kwargs)
        totalB += run_time(functionB,*args, **kwargs)

    totalA = totalA/times_average
    totalB = totalB/times_average

    '''
    1.001 or 0.1% is the lowest granularity time.clock() can distinguish I've tested
    it calling compare and passing the same function twice. So we assume that if the difference 
    of speed is less than 0.1% the functions take the same time to execute  
    '''

    if totalA < totalB and (totalB/totalA > 1.001):
        print("Result: "+ functionA.__name__+ " is "+ str(totalB/totalA) +" times faster than "+functionB.__name__)
    elif totalB < totalA and (totalA/totalB > 1.001):
        print("Result: "+ functionB.__name__+ " is "+ str(totalA/totalB) +" times faster than "+functionA.__name__)
    else:
        print(functionA.__name__+" and "+functionB.__name__+" have the same speed!")