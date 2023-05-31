[Tutorial](https://www.youtube.com/watch?v=EtAGd-3arNE&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=11)

## Lists:

Ordered - Mutable - Allows duplicate elements

- We want 5 zeros in a list => `a = [0] * 5`
- Concat with + operator
- Negative Index a\[-1\] => latest index
- list\_copy = list\_org => if append to org, appended to copy too
- list\_copy = list\_org.copy() or list(list_org) or list\[:\] => if append to org not appended to copy.

## Tuples:

Ordered. - Immutable - allows duplicate elements

- my_tuple = ("Max") => identified as a string ( only in single element tuple )
- my_tuple = ("Max", ) => identified as a tuple
- Negative Index a(-1) => latest index
- my_tuple\[0\] = "Parsa" => Error because immutable.
- tuple(my\_list) and list(my\_tuple)
- a\[::-1\] => latest number means step => here means reversed step, if 2, 2 step 2 step

```python
my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple
print(i2) # [1,2,3]
```

- tuples in time and memory usage is better than lists (but immutable)

## Dicts

Key-value pairs, Unordered, Mutable

- dict(name="A") is = {'name' : 'A'}
- del my_dict\['name'\] => delete key and value
- my_dict.popitem() => pop latest (right) key and value from dict
- my\_dict.keys() => all keys .values() => all values, key value in my\_dict.items() both :/
- dict\_copy = dict\_org => if changed org, change copy too
- dict\_copy = dict\_org.copy() or dict(dict_org) => if change org not chamge copy.
- my_dict.update(dict(name="B", age=2))
- my_dict = {(1,2) : 5}, key cannot change in this example because tuples are immutable

## Sets

Unordered - Mutable - no duplications

- set('Hello') => {'o', 'l', 'H', 'e'}
- empty set => `a = set()` a= {} is empty dict
- myset.add(1)
- myset.remove() => if not found in set error occured,
- myset.discard() => if not found in set nothing happend.
- my_set.clear() => remove all
- my\_set.pop() => returns first item of set and pop it from set ex: print(my\_set.pop()) => 1
- union => first\_set.union(second\_set) => odds.union(evens) => all numbers
- intersection => odds.intersection(evens) => set() or empty set => odds.intersection(primes)
- diff = setA.difference(setB) => members of A that not exist on B
- sym\_diff = setA.symmetric\_difference(setA) => Members of A that not exist on B + Members of B than not exists on A
- setA.intersection_update(setB)
- setA.difference_update(setB)
- setA.symmetric\_difference\_update(setB)
- setA.issubset(setB)
- setA.issuperset(setB)
- setA.isdisjoint(setB) => without any intersection
- setB = setA => also original one changed
- setB = setA.copy() or set(setA)
- a = frozenset(\[1,2,3,4\]) => add, remove and ... not work on it

## Strings

Ordered - immutable - text representation
my_string\[0\] = 'a' => Error
my_string\[::-1\] => reverse
my_string.strip() => removes whitespaces
my\_string.startswith("hello") / my\_string.endswith("world")
my_string.find("substring") => returns index or -1
my\_string.count("substring") / my\_string.replace('World', "Universe")
' '.join(my_list) => String: too faster than for loop

## Collections

Counter - namedtuple - OrderedDict - defaultdict, deque

```python
from collections import Counter, namedtuple, OrderedDict,defaultdict, deque
# Coutner
a = "aaabbbbcc"
my_counter = Counter(a)
print(my_counter.most_common(1))
# namedtuple
Point = namedtuple("Point", 'x,y')
pt = Point(1, -4) # Create a class with x and y attr
print(pt.x, pt.y)
# OrderedDict
ordered_dict = OrderedDict()
ordered_dict['b'] = 2
ordered_dict['a'] = 1
print(ordered_dict) # first print [(b,2),(a,1)] so order is important
# defaultdict
d = defaultdict(int) # integer is default type
d['a'] = 1
d['b'] = 2
print(d[0]) # => if default type was int return 0 if float 0.0 and ...
# Deque double ended queue
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.popleft()
d.extend([4,5,6])
d.extendleft([4,5,6])
d.rotate(1)
print(d)
```

## itertools

```python
from itertools import product, permutations, combinations,combinations_with_replacement , accumulate, groupby
# product
a = [1,2]
b = [3,4]
prod = product(a,b, repeat=1) # or 2 or 3 repeat is acceptable
print(list(prod)) # [(1,3),(1,4),(2,3),(2,4)]

# permutations and combinations
a = [1,2,3]
perm = permutations(a, 2) # (jaygasht) second is len of it (1,2) (2,1) 
comb = combinations(a, 2) # (1,2) (1,3) (1,4) ... order is important
comb_wr = combination_wtih_replacement(a,2) # (1,1) (1,2)...(2,2)...

# accumulate
a = [1,2,3,4]
acc = accumulate(a, func=operator.sum) # [1,3,6,10] can be sum mul max 

# groupby
a = [1,2,3,4]
def smaller_than_3(x):
    return x <3
group_obj = groupby(a, key=smaller_than_3) # or key=labmda x: x<3
print(group_obj) # True [1,2] , False [3,4]

# infinite iterators
from itertools import count, cycle, repeat
for i in count(10):
    print(i) # 10 11 12 ...
    if i == 15:
        break
for i in cycle([1,2,3]):
        print(i) # 1 2 3 1 2 3 1 2 3..
    for i in repeat(1,4):
        print(i) # 1 1 1 1
```

## Lambda function

lambda arguments: expression

```python
add10 = lambda x: x + 10
add10(5) # 15
mult = lambda x,y: x*y
mult(2,7) # 14
points2D = [(1,2),(15,1),(5,-1)]
points2D_sorted = sorted(points2D, key=lambda x: x[1]) #or x[1] + x[0]
a = [1,2,3,4,5]
b = map(lambda x: x*2, a)
c = [x*2 for x in a] # equal with above command
b = filter(lambda x: x%2 ==0, a)
c = [x for x in a if x%2==0] # equal with above command
from functools import reduce
product_a = reduce(lambda x,y: x*y, a)
print(product_a) # => Print result of times of all elements 1*2*3*4
```

## Exception

```python
print("h")) # SyntaxError
a = 5 + '10' # TypeError
b = c # NameError c not defiend
f = open("file.txt") # FileNotFoundError
a = [1,2,3]
a.remove(4) # ValueError
a[4] # IndexError
my_dict = {'name' : 'parsa' }
my_dict['age']  # KeyError
raise Exception('test exception') # Exception
assert (x>=0), 'x is not positive'
try:
    a = 5 / 0 # ZeroDivisionError
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    # Always run, dont matter exception or not
    print('cleaning up...')

class ValueTooHighError(Exception):
        pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 50
        raise ValueTooSmallError('value is to small', x)
        
```

## Logging

```python
# main.py
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
import helper

# helper.py
logger = logging.getLogger(__name__)
logger.info("hello from helper")
```

There are more details about logging that i dont need them yet

## JSON

dict to json => Serialization / Encoding
personJSON = json.dumps(person, indent=4, sort_keys=True) # dumps mean dump to string
dump used for write dictionary as a JSON in a file

json to dict => Deserialization / Decoding
person = json.loads(personJSON) # loads mean load from string
load used for load json from file

```python
from json import JSONEncoder
import json
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
user = User('Max', 27)
# Encode
# userJSON = json.dumps(user) we will get type error
def encode_user(obj):
    if isinstance(obj,User): # its check obj is instance of User Class
        return {'name': obj.name, 'age': obj.age,
                obj.__class__.__name__:True}
    else:
        raise TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)

# or we can use JSONEncoder Class
class UserEncoder(JSONEncoder):
    def default(self,obj): # Override default method JSONEncoder Class
        if isinstance(obj,User):
        return {'name': obj.name, 'age': obj.age,
                obj.__class__.__name__:True}
        return JSONEncoder.default(self,obj)
    
userJSON = json.dumps(user, cls=UserEncoder)
#OR
userJSON = UserEncoder().encode(user)
print(userJSON)

# Decode back
user = json.loads(userJSON)
print(type(user)) # is dict not object
user.name # we get error because it returns Dict not class instance
def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    return dct
user = json.loads(userJSON, object_hook=decode_user)
print(type(user)) # is class
print(user.name) # it works 
```

## Random numbers:

### Not recommended for scurity purposes

a = random.random()
a = random.uniform(1,10)
a = random.randint(1, 10)
a = random.randrange(1,10)
a = random.normalvariate(0, 1) # normal distrobution
mylist = list("ABCDEFGH")
a = random.choice(mylist)
a = random.sample(mylist,3)
a = random.choices(mylist,k=3) # Repeat is ok
random.shuffle(mylist)
print(mylist)
random.seed(1)
print(random.random()) # Psudo random because reproducable
random.seed(1)
print(random.random()) # Exact same

### For security perposes use secrets

import secrets # => true random numbers
a = secrets.randbits(4) # 1101
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)

import numpy as np
its psudo random too and not recommended for security purposess

```python
a = np.random.rand(3)
a = np.random.rand(3,3)
a = np.random.randint(0,10,(3,3))
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr)
print(a)
```

## Decorators*

2 different decorators:
1- Function Decorators ( More Common )
2- Class Decorators

```python
@mydecorator
def do_something():
    pass
```

**A decorator is a function that takes another function as an argument and extends the behavior of this function without explicitly modifying it**
in other words
**decorator allows you to add new functionality to an existing function**
we have to know that **Functions in Python are first-class objects, this means that like any other objects they can be defined inside another function, passed as an argument to another function, and even returned from another function**

### ==Decorator Logic==

```python
def start_end_decorator(func): 
    def wrapper():
        print("Start") # Before function triggered
        func()
        print("End") # After function triggered
        return wrapper
    
def print_name():
    print('Alex')
    
print_name = start_end_decorator(print_name) # ** equal to @start_end_decorator **
print_name()
# Print Start Alex End :)
```

above example is all logic of decorator and `start_end_decorator()` function extend the behavior of `print_name()` function with a decorator.

```python
import functools

def start_end_decorator(func): # Template for decorator
    @functools.wraps(func)
		def wrapper(*args, **kwargs):
				print("Before") # Before function triggered
				result = func(*args, **kwargs) # Get Arguments and Return Result
				print("After") # After function triggered
				return result		
	return wrapper

@start_end_decorator
def add5(x):
	return x + 5

add5(10) # We'll get error because wrapper didn't get argument (we defined now)
print(result) # None (we resolve it now)

print(add5.__name__) # returns wrapper :| handle with functools
```

### Multiple decorators
```python
import functools

def start_end_decorator(func): # Template for decorator
    @functools.wraps(func)
		def wrapper(*args, **kwargs):
				print("Before") # Before function triggered
				result = func(*args, **kwargs) # Get Arguments and Return Result
				print("After") # After function triggered
				return result		
	return wrapper

def debug(func): # Print more information about a function
	@functools.wraps(func)
	def wrapper(*args,kwargs):
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		print(f"Calling {func.__name}({signature})")
		result = func(*args, **kwargs)
		print(f"{func.__name__!r} returned {result!r}")
		return result
	return wrapper


@debug # at first trigger insite it
@start_end_decorator # trigger it and inside it triggers
def say_hello(name): # it
	greeting = f'hello {name}'
	print(greeting)
	return greeting

```

### Decorator with args:
```python
import functools

def repeat(num_times):
	def decorator_repeat(func):
		@functools.wraps(func)
		def wrapper(*args, **kwargs):
			for _ in range(num_times):
				result = func(*args, **kwargs)
			return result
		return wrapper
	return decorator_repeat

@repeat(num_times=3)
def greet(name):
	print(f'hello {name}')
greet('Alex')
```
- in the provided code, `repeat` is a decorator. It is a higher-order function that takes an argument num_times and returns the decorator_repeat function, which is the actual decorator.
- The inner decorator, decorator_repeat, uses the functools.wraps decorator from the functools module to preserve the metadata of the original function func. This ensures that the decorated function retains its original name, docstring, and other attributes.
- when decorator have argument itself, we must take func in inner function (i think)

### Class Decorators
typically used if we want to maintain and update a state, time, debug, check and ...
```python
class CountCalls:
	def __init__(self, func):
		self.func = func
		self.num_calls = 0
	def __call(self, *args, **kwargs): # like inner function in function decorator
		self.num_calls += 1
		print(f'This executed {self.num_calls} times')
		return self.func(*args, **kwargs)


@CountCalls
def say_hello():
	print('Hello')
	
say_hello()
say_hello() # Return 2 times
```

## Generators
**Generators are functions that return an object can be iterated over and special thing is that they generate the items inside the object lazily which means they generate the tiems only one at a time and only when you ask for it
and because of it they are much more memory efficient than other sequence objects when you have to deal with large data sets.**
- very memory efficient

```python
def mygenerator():
	yield 1
	yield 2
	yield 3
g = mygenerator()
print(g) # print <generator object ... >
# for i in g:
# 	print(i) # print 1 2 3
value = next(g)
print(value) # 1
value = next(g)
print(value) # 2
value = next(g)
print(value) # 3
value = next(g)
print(value) # StorIteration Exception

sum(g) # 6
sorted(g) # [1,2,3]
```
another example:
```python
def countdown(num):
	print('Starting')
	while num > 0:
		yield num
		num -= 1
cd = countdown(4) # not execute Starting
value = next(cd) # execute
print(value) # 4
print(next(cd)) # 3
print(next(cd)) # 2
print(next(cd)) # 1
print(next(cd)) # StopIteration
```
how its memory efficient?
```python
import sys

def firstn(n):
	nums = []
	num = 0
	while num < n:
		nums.append(num)
		num += 1
	return nums

my_list = firstn(10) # [0,1,...,9]

def fristn_generator(n): # we dont need list anymore
	num = 0
	while num < n:
		yield num # just one variable addressed until we get it not save in store.
		num += 1
		
print(sum(firstn(10))) #45
print(sum(firstn_generator(10))) #45

print(sys.getsizeof(firstn(10))) # 192
print(sys.getsizeof(firstn_generator(10))) # 120

print(sys.getsizeof(firstn(1000000))) # 8697464
print(sys.getsizeof(firstn_generator(1000000))) # 120
```

**another important advantage of the generator object is that we do not have to wait until all the elements have been generated before we start to use them because we can get just get first next statement and we don't have to calculate all the numbers YEAH**

```python
def fibonacci(limit):
	# 0 1 1 2 3 5 8 13...
	a, b = 0, 1
	while a < limit:
		yield a
		a, b = b, a+b

fib = fibonacci(30)
for i in fib:
	print(i)
```

```python
import sys
mylist = [i for i in range(10000000) if i % 2 == 0]
print(sys.getsizeof(mylist)) 4066496
mygenerator = (i for i in range(10000000) if i % 2 == 0)  # Shortcut of generator :)
print(sys.getsizeof(mygenerator)) 120
for i in mygenerator:
	print(i)
```
