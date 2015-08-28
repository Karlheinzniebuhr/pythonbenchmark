from pythonbenchmark import compare, measure
import time

a,b,c,d,e = 10,10,10,10,10
something = [a,b,c,d,e]

#@measure
def myFunction(something):
	time.sleep(0.4)

#@measure
def myOptimizedFunction(something):
	time.sleep(0.2)

# decorator test
#myFunction(input)
#myOptimizedFunction(input)

# comparing test
compare(myFunction, myOptimizedFunction, 10, input)
