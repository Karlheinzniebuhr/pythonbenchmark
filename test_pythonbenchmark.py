from pythonbenchmark import compare, measure
import time



a,b,c,d,e = 10,10,10,10,10

# @measure
def myFunction(a,b,c,d,e):
	time.sleep(0.4)

# @measure
def myOptimizedFunction(a,b,c,d,e):
	time.sleep(0.2)

# decorator test
#loop(input)
#square2(input)

# comparing test
compare(myFunction, myOptimizedFunction, 2,a,b,c,d,e)