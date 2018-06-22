@title[Introduction]

# Python

---

### Functional or Object-oriented?

@title[Functional or Object-orientd?]

@ul

- python, allows developers to write code in either a functional or object-oriented fashion
- however, python itself is completly object oriented
- In fact python has classes for:
    - basic types: int, str, float...
    - containers: list, set, dict...
    - functions/methods
    - class/types
    - modules

@ulend

---

@title[Sample Classes]

```[python]
>>> def test():
...     pass
>>> test.__class__
<class 'function'>
```

```[python]
>>> class Test(object):
...     pass
>>> Test.__class__
<class 'type'>
```

```[python]
>>> import sys
>>> sys.__class__
<class 'module'>
```
---

@title["Data Model"]

### Python Data Model

@ul

- python uses an internal data model to define all objects
- These data models define objects as:
    - hashable
    - iterable
    - callable
    - operable with mathmatical operators +, -, %, <, <=, ...
    - and a lot more (https://docs.python.org/3/reference/datamodel.html)

@ulend

---

@title["Why does this matter"]

### Why does this matter?

@ol
- It can be really useful when debugging
- effecticly using these data model methods can create classes that are:
    @ul
    - easier to use
    - more efficient
    - more flexible
    @ulend
@olend

---?code=sample/binomial/binomial.py&lang=python&title=Binomial

@[1-4](Simple binomial class definition)
@[6-8](create and print a binomial)

---?code=sample/binomial/binomial.txt&title=Binomial Output

@[1](lets make this output more useful)

---?code=sample/binomial/binomial_str.py&title=Binomial Str

@[6-8](added \_\_str\_\_ function to provide a specific string representation for this class)

---?code=sample/binomial/binomial_str.txt&title=Binomial Str Output
@[1](new output is much more useful)
---

@title[Callable]

### Callable

@ul
- mathmatical functions should be callable
- we can make our new binomial class callable by defining a \_\_call\_\_ method
- this method is the data model method functions define to make themself callable
- the parameters to \_\_call\_\_ are the parameters passed by the caller
@ulend

---?code=sample/binomial/binomial_call.py&title=Binomial Callable

@[10-11](a simple call function for out binomial)
@[16-17](make a few calls to out binomial)

---?code=sample/binomial/binomial_call.txt&title=Binomial Callable Output

---

@title[Operator Overloading]
### Operator Overloading

@ul
- Binomials should support mathmatical functions like +, -, * and /
- python allows you to overide these functions using data model methods as well
- to save time we are only going to look at + which is defined by \_\_add\_\_
@ulend

---?code=sample/binomial/binomial_add.py&title=Binomial Add
@[10-13](define the add functionality)
@[20](create a second binomial)
@[24](add the two binomials together and compute result)

---?code=sample/binomial/binomial_add.txt&title=Binomial Add

---

@title[Iterators]

### Iterator

@ul
- Iterators allow python to iterator over a list of values computing results 1 step at a time
- Iterators must define a \_\_iter\_\_ function which enables them to work with the in keyword
- they also must define a \_\_next\_\_ function that progresses the iterator to the next value (note: next in python2)
- once there are no more values to iterate a StopIteration exception should be raised
@ulend

---?code=sample/binomial/binomial_iter.py&title=Binomial Iterator

@[1-6](define the Iterator class and initializer)
@[8-9](define an the \_\_iter\_\_ function that just returns self)
@[11-17](define the \_\_next\_\_ that returns the current value and moves the iterator to the next value)
@[25-26](define a function on our binomial class that returns this iterator)
@[43-44](test out the iterator)

---?code=sample/binomial/binomial_iter.txt&title=Binomial Iterator Output

---

@title[Iterators Summary]

### Iterator continued

@ul
- iterators are great since they only store one iteration in memory at a time
- you can add other method to them that may be useful like reset()
- however in order to define one you must implement a few different methods
- luckily python provides another option that can be implemented easier
@ulend

---
@title[Generators]

### Generators

@ul
- a generator is actually a type of iterator
- instead of defining an \_\_iter\_\_ and \_\_next\_\_ function you simply use the yield keyword
- the python interpreter will then create the iterator for you
@ulend

---?code=sample/binomial/binomial_generator.py&title=Binomial Generator

@[6-10](replace iter_range with generated form)

---?code=sample/binomial/binomial_generator.txt&title=Binomial Generator Output

---?code=sample/binomial/binomial_generator.dir&title=Binomial Generator Dir

@[4-7](notice out generator contains an \_\_iter\_\_ and \_\_next\_\_ function)
---

### Questions?

@fa[github gp-contact](@BrandonHoffman)

@fa[medium gp-contact](brandon.michael.hoffman@gmail.com)
