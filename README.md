# timecomplexity

<h3>Python library that makes benchmarking easy and fun</h3>
<h6>Contributors wanted. Please send me lots of pull requests or suggestions</h6>
The timeit module that comes with python is only useful for small bits of Python code not for functions.

This library solves that. It provides an intuitive way to measure the execution time of functions and compare the relative speed of two functions.
<h4>Why</h4> would you want to compare the relative speed of two functions? 
Because if you are optimizing your code you may want to know how much of a speed improvement you gained. 
<h4>How</h4>
Timecomplexity allows this by letting you compare two functions which take the same input and measure which one gets the job done faster. 
<h4>@measure</h4>
Additionally you can just put a decorator on the functions, timecomplexity will measure them and print out the execution time in the console.

How to use:
Import timecomplexity.py

The typical use case could be: You have functionX, and optimized functionX. Now you want to know if your modified version is faster.

```python
from timecomplexity import compare, measure
import time
times_average = 1000     # this is used to produce an average --> (function_calls / number_of_calls)
myinput = "some input"   # the input of your functions, It can be an arbitrary number of inputs, an array or dictionary 
def myFunction(input):
	time.sleep(0.4)
def myOptimizedFunction(input):
	time.sleep(0.2)
	
compare(myfunction, myUpdatedfunction, times_average, input)
```
Measuring execution time with the @measure decorator
```python
from timecomplexity import compare, measure
import time

arguments = "something" # the input of your functions, It can be an arbitrary number of inputs, an array or dictionary

@measure
def myFunction(arguments):
	time.sleep(0.4)
@measure
def myOptimizedFunction(arguments):
	time.sleep(0.2)
	
myFunction(arguments)
myOptimizedFunction(arguments)
```
<h3>TODO</h3>
Adding support to compare multiple functions maybe? 
Any ideas are welcome
