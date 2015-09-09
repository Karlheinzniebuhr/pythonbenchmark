### Learn to write faster code by experimenting with this library 

#pip install pythonbenchmark  
- The timeit module that comes with python is only useful for small bits of Python code not for functions.

- This library solves that. It provides an intuitive way to measure the execution time of functions and compare the relative speed of two functions.

- Optimizing your code? Curious how much speed you gained? No problem

- Pythonbenchmark allows this by letting you compare two functions which take the same input and measure which one gets the job done faster.
```python
compare(myFunction, myOptimizedFunction, 10)
```
- Additionally you can just put a decorator on the functions, pythonbenchmark will measure them and print out the execution time in the console.
```python
@measure
def myFunction(something):
    [x*x for x in range(1000000)]
```

###How-To:
A typical use case is: I have functionX, and optimized functionX. Now I want to know if my modified version is faster and how much.

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
# without input
compare(myFunction, myOptimizedFunction, 100)
```

<h4>Output</h4>
![alt tag](https://github.com/Karlheinzniebuhr/pythonbenchmark/blob/master/images/test_compare.PNG)


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
![alt tag](https://github.com/Karlheinzniebuhr/pythonbenchmark/blob/master/images/test_decorator.PNG)

<hr>

Do experiments, have fun!  
Make incremental changes to your high performance code and see how much speed improvement you gain with each modification. This will give you an enormous intuition about how to write fast code :)  

A spanish article about how I came up with this library is on my  [Blog.](http://karlheinzniebuhr.github.io/es/2015/05/10/de-CS101-a-una-libreria-python.html)
