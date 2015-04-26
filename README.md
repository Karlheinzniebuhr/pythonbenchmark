# timecomplexity

Python provides us with the possibility to measure the execution time of code snippets with 
https://docs.python.org/2/library/timeit.html 
But in most cases it’s difficult if not impossible to guess how long it should take
to execute certain code. It would be much more useful to just see how the execution time is changed by changing the code.
Enters  Timecomplexity! Timecomplexity allows you to compare two functions which take the same input and compares which one
of them executes faster and how many times faster compared to the second function. 

How to use:
Put the timecomplexity.py file in your working order
Import it

The typical use case would be that you have a functionX, and your modified functionX. 

```python
import timecomplexity
times_average = 1000     # this is used to produce an average --> (function_calls / number_of_calls)
loops = 10               # number of times the whole function will run and print to the console
myinput = "some input"   # the input of your functions
def myFunction(input):
	# something
def myOptimizedFunction(input):
	# something
timecomplexity.compare(myfunction, myUpdatedfunction, myinput, times_average, loops)
```
Measuring time of a single function
```python
import timecomplexity
times_average = 1000    # this is used to produce an average --> (function_calls / number_of_calls)
loops = 10              # number of times the whole function will run and print to the console
myinput = "blabla"	# the input of your function
def myFunction(input)
	# something
timecomplexity.measure(myFunction, myinput, times_average, loops)
```

