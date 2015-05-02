# Pythonbenchmark

<h3>The Python library that makes benchmarking easy and fun</h3>
<h6>Contributors wanted. Please send me lots of pull requests or suggestions</h6>
The timeit module that comes with python is only useful for small bits of Python code not for functions.
<hr>
This library solves that. It provides an intuitive way to measure the execution time of functions and compare the relative speed of two functions.
<hr>
<h4>Why</h4> would you want to compare the relative speed of two functions? 
Because if you are optimizing your code you may want to know how much of a speed improvement you gained. 
<hr>
<h4>How</h4>
Pythonbenchmark allows this by letting you compare two functions which take the same input and measure which one gets the job done faster.
<hr>
<h4>@measure</h4>
Additionally you can just put a decorator on the functions, pythonbenchmark will measure them and print out the execution time in the console.

<h3>Howto</h3>:
The typical use case could be: You have functionX, and optimized functionX. Now you want to know if your modified version is faster.

```python
from pythonbenchmark import compare, measure
import time

a,b,c,d,e = 10,10,10,10,10
something = [a,b,c,d,e]

def myFunction(something):
	time.sleep(0.4)

def myOptimizedFunction(something):
	time.sleep(0.2)

# comparing test
compare(myFunction, myOptimizedFunction, 10, input)
```

<h4>Output</h4>

![alt tag](https://github.com/Karlheinzniebuhr/pythonbenchmark/blob/master/test_files/test_compare.PNG)


Measuring execution time with the @measure decorator
```python
from pythonbenchmark import compare, measure
import time

a,b,c,d,e = 10,10,10,10,10
something = [a,b,c,d,e]

@measure
def myFunction(something):
	time.sleep(0.4)

@measure
def myOptimizedFunction(something):
	time.sleep(0.2)

myFunction(input)
myOptimizedFunction(input)

```
<h4>Output</h4>

![alt tag](https://github.com/Karlheinzniebuhr/pythonbenchmark/blob/master/test_files/test_decorator.PNG)

<hr>
<h3>TODO</h3>
Adding support to compare multiple functions maybe? 
Any ideas are welcome

