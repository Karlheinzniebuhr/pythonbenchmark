# Copyright Karlheinz Niebuhr
import time
import platform        
                                             #  This part of code is to calculate how long a 
def time_execution(function, arg):           #  code will take to run (learned in class). 
    start = time.clock()
    function( arg )
    run_time = time.clock() - start
    return run_time


def avgof(times,function, parameter):
    count = 0
    track = 0

    while count < times:
        track += time_execution(function, parameter)
        count += 1
    return track/times


def compare(functionA, functionB, parameter, times, loops=10,):
    # loop n times
    i = 0
    totalA = 0.0
    totalB = 0.0                      
    while i < loops:
        first = avgof(times, functionA, parameter)
        second = avgof(times, functionB, parameter)
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
