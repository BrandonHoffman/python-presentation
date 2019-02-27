@title[Introduction]

# Python
## Demystifyied

---

### Functional or Object-oriented?

@title[Functional or Object-orientd?]

@ul

  - My Claim: Python is a pure object oriented language.
  - what do I mean by a "pure" object oriented programming language
    - must support the basic object oriented pricipals (inheritance, polymorphism, ...)
    - all user defined types are objects
    - all operations performed on an object must only be through methods exposed on the object

@ulend

---

@title[Does python meet these qualifications]

@ul
- python does support the basic object oriented principals
- all user defined types are classes
    - basic types: int, str, float...
    - containers: list, set, dict...
    - functions/methods
    - class/types
    - modules

@ulend

---

@title[Sample Classes]

```[python]
variable = 1
variable.__class__
# <type 'int'>
```

```[python]
def test():
    pass
test.__class__
# <class 'function'>
```

```[python]
class Test(object):
    pass
Test.__class__
# <class 'type'>
```

```[python]
import sys
sys.__class__
# <class 'module'>
```
---

@title[Python Data Model]

### Python Data Model

@ul

- python uses an internal data model to define all interactions with objects
- These data models define objects as:
    - iterable
    - callable
    - operable with mathmatical operators +, -, %, <, <=, ...
    - and a lot more (https://docs.python.org/3/reference/datamodel.html)
- these inteface methods are known as data model methods (dunder)
@ulend
---

@ul
- understanding these methods can:
    - allow you to create more powerful librarys
    - provide insight into the features of python which are often refered to as `magic`
    - answer questions about many of pythons language features
@ulend

---

@title[dynamic properties]

### Dynamic properties

```[python]
class Test(object):
    pass
obj = Test()
obj.x = 1
```

---
@title[\_\_dict\_\_]


```[python]
class Test(object):
    pass
obj = Test()
obj.__dict__
# {}
obj.x = 1
obj.__dict__
# {'x': 1}
```
@[1-4] most classes in python have `__dict__` property which is used to store its properties

---
### Functions

@title[Functions]

```[python]
def fib(n: int):
    """calculates the n'th digit of the fibonacci sequence"""
    if n in {0, 1}:
        return n
    else:
        return fib(n-1) + fib(n-2)

fib.__class__
# <class 'function'>
dir(fib)
# ['__annotations__', '__call__', '__defaults__', '__doc__', '__kwdefaults__', ...]

@[1-6] a simple fib function for demonstration purposes
@[7-8] the fib function is actually an instance of the function class
@[9-10] this class implements a few special data access methods which define how the instance works when called
```
---
- __annotations__: contains the type annotation for a function (mostly used by IDE's)
- __call__: tells the interpreter that this instance is callable
- __defaults__: stores the default values of default parameters used by the function
- __doc__: contains the doc string of the function (mostly used by IDE's)
  - this parameter is not specific to functions it is actually used by all other types that support doc strings such as classes and modules
- __kwdefaults__: store the defaults of keyword only arguments
- note: that any object that defines a __call__ attribute is made callable by the python interpreter
---

### Decorators

@title[Decorators]

```[python]
@decorator
def fib(n: int):
   ...
```
@[1-4] how do you think decorators work

---

```[python]
def fib(n: int)
    ...
fib = decorator(fib)
```
@[3] the previous code is functionally equivalent to  this
---

- decorators themselves are just functions.
- the decorator function is passed the function that was defined below as its only parameter
- the decorator can then either:
    - return a new function that will be used in place of the original definition
    - manipulate the data model methods of the existing function and return the modified function


```[python]
class Cache(object):
    def __init__(self, function):
        self._cache = {}
        self._function = function

    def __call__(self, n)
        try:
            return self._cache[n]
        except KeyError:
            value = self._function(n)
            self._cache[n] = value
            return value

@Cache
def fib(n: int):
   ...

fib.__class__
# <class __main__.Cache at 0x106942a78>
```
@[1] lets create a class that can be used as our decorator
@[2-4] the __init__ function for this class is what initially gets called passing in the function
@[6-12] the __call__ function of our new class will be what gets called in place of our original function
@[14-15] we add the decorator to our function 
@[17-18] note out fib object in now an instance of the Cache class not function like it was originally.
---

### generators

- a generator is a funtion making use of the `yield` statement within python
- when a generator function gets called it returns a generator object which can be used to iterate through a sequence of results
- a yield statement results in the state of the variables in the function being saved while the yielded value is handed to the calling function
- eventually when the generator runs out of values to yield and the end of a function is hit a StopIteration exception is raised and execution halts

---
```[python]
def count(start: int, end: int):
   cur = start
   while cur < end:
       yield cur
       cur += 1
count.__class__
# <class 'function'>
count(1, 10).__class__
# <class 'generator'>
dir(count(1, 10))
# ['__iter__', '__next__', ...]
```
@[1-6] this is what the basic definition of a generator would look like
@[7-8] you will notic that count is just simply a function
@[9-10] however when that function is called a special generator type is returned
@[11-12] these two properties are what allows for the generator to be iterated in the way it does.

---

- __iter__: allows the function to be iterable.
  - other iterable classes such as lists and sets also define this fuction (can be used with `for .. in` loops)
- __next__: this function is used to step through each value one at a time
  - this is the function that is responsible for raising the StopIteration when no more values are avaliable
  - this function can be called by passing this instance to the next function

---

```
counter = count(1, 2)
print(next(counter))
# 1
print(next(counter))
# 2
print(next(counter))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```
---

### Iterators

```[python]
class Counter:
    def __init__(self, start: int, end: int):
        self._start = start
        self._end = end
        self._cur = start
    def __iter__(self):
        return self
    def __next__(self):
        val = self._cur
        if val < self._end:
            self._cur += 1
            return val
        raise StopIteration
```
@[1-13] the same two data models methods generators use to iterate values can be used by any class
@[6-7] the same __iter__ function returns the object we will be iterating in this can self
@[8-13] the __next__ function progresses the iterator or raises my stop iteration error
---

### Why would I use an Iterator over a Generator

- Generators are:
    - fewer lines of code
    - easier to follow
    - and simpler to implement
- however they are not able to
    - be subclassed
    - implement additional public methods
    - implement additional data model methods
- In general though I would suggest initially making use of generators until they no longer fit your use case.

--- context managers

### Context managers

- context managers allow for for blocks of code with a setup and teardown
- additionally context managers are able to seamlessly handle errors thrown within them
- they must define a __enter__ and __exit__ function
- a common use case for context managers is opening a file.

```
f = open("test.txt")
dir(f)
# ['__enter__', '__exit__', ...]

```
---

```
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, exception_type, exception_value, traceback):
        if(exception_type is not None):
           print("exception handled") 
        self.file_obj.close()
        return True

with File("test.txt") as log:
    log.write("test")
```
@[1-3] create a function for opening a file
@[4-5] the enter function is called at the start of the block
@[5] the return from __enter__ can optionally be set to a variable using the as keyword
@[6-10] the __exit__ function handles the clean up and can optionally handle exceptions
@[10] returning a True prevents the exception from propigating
---

- alternativly context managers are able to be defined via the contextmanager library
- this library actually allows you to use you to define a generator which can be used as a context manager

```
import contextmanager

@contextmanager
def file(filename)
    file = open(filename)
    try:
        yield file
    except Exception:
        print("exception handled")
    finally:
        file.close()

with file("test.txt") as log:
    log.write("test")
```
---

- data model methods are used in a lot more ways then what could be covered in this presentation
- some sample uses:
    - slicing object (list[1:3])
    - getting, setting and deleting attributes on object
    - hashing of an object
    - determining if an object should evaluate represent true or false when used conditionally
    - creating new classes and subclasses
    - and much more
- understanding these methods is your key to understanding many of the `magic` within python


---




### Questions?

@fa[github gp-contact](@BrandonHoffman)

@fa[medium gp-contact](brandon.michael.hoffman@gmail.com)
