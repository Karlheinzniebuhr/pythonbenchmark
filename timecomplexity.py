# copyright Karlheinz Niebuhr
import time                         #  This part of code is to calculate how long a 
def time_execution(code):           #  code will take to run (learned in class). 
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return run_time

def sillycaseCaffeine(string):
    return string[:int(round(len(string) / 2))].lower() + string[int(round(len(string) / 2)):].upper()

def sillycaseKarl(string):
    half = int(round(len(string) / 2))
    return string[:half].lower() + string[half:].upper()


def avgof(times,function, parameter):
    count = 0
    track = 0 
    track1 = 0
    track2 = 0
    track3 = 0
    to_execute1 = function + "('abcdefgh')"
    to_execute2 = function + "('abcdefghi')"
    to_execute3 = function + "('ghi')"
    while count < times:
        track1 += time_execution(to_execute1)
        track2 += time_execution(to_execute2)
        track3 += time_execution(to_execute3)
        count += 1
    return (track1+track2+track3)/times

# Finally we check which one is faster and print!
i = 0      
a = 0
b = 0                      
while i < 10:
    first = avgof(1000, "sillycaseKarl")
    second = avgof(1000, "sillycaseCaffeine")
    if first < second:
        print 'sillycaseKarl is ' + str(second/first) + ' times faster'
        a+=1
    else:
        print 'sillycaseCaffeine is ' + str(first/second) + ' times faster'
        b+=1
    i += 1
print "Average is: a="+str(a)+' b='+str(b) 
