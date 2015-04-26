# Copyright Karlheinz Niebuhr
import time                         #  This part of code is to calculate how long a 
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
    a = 0
    b = 0                      
    while i < loops:
        first = avgof(times, functionA, parameter)
        second = avgof(times, functionB, parameter)
        if first < second:
            print 'functionA is ' + str(second/first) + ' times faster'
            a+=1
        else:
            print 'functionB is ' + str(first/second) + ' times faster'
            b+=1
        i += 1
    print "Average is: a="+str(a)+' b='+str(b)

