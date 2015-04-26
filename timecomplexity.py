# Copyright Karlheinz Niebuhr
import time

import sys

        
#  This part of code is to calculate how long a code will take to run
def time_execution(function, arg):         
    if sys.platform == 'win32':
        # time.clock() resolution is very good on Windows, but very bad on Unix.

        # ***** For now this doesn't seem to work well so we will just use time.clock() *****

        # check if python is >= V 3.3 
        if False: #(sys.version_info[0] == 3 and sys.version_info[1] == 3):
            run_time = time.process_time()
            function( arg )
            #run_time = time.process_time()
        else:
            start = time.clock()
            function( arg )
            run_time = time.clock() - start
    else:
        # On most other platforms the best timer is time.time
        start = time.time()
        function( arg )
        run_time = time.time() - start
    #print(run_time)
    return run_time


def avgof(function, parameter, times_average):
    count = 0
    track = 0

    while count < times_average:
        track += time_execution(function, parameter)
        count += 1
    return track/times_average


def compare(functionA, functionB, parameter, times_average, loops=10):
    # loop n times
    i = 0
    totalA = 0.0
    totalB = 0.0                      
    while i < loops:
        first = avgof(functionA, parameter, times_average)
        second = avgof(functionB, parameter, times_average)
        if first < second:
            print('functionA is ' + str(second/first) + ' times faster')
            
        else:
            print('functionB is ' + str(first/second) + ' times faster')
            

        totalA+=first
        totalB+=second
        i += 1
    if first < second:
        print("On average function A is "+str( "{0:0f}%".format(totalB/totalA * 10) )+' faster than function B')
    elif second < first:
        print("On average function B is "+str( "{0:0f}%".format(totalA/totalB * 10) )+' faster than function A')

def measure(function, parameter, times_average=1, loops=10):
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