
### Lists:
Ordered - Mutable - Allows duplicate elements
* We want 5 zeros in a list  => `a = [0] * 5`
* Concat with + operator
* Negative Index a[-1] => latest index
* list_copy = list_org => if append to org, appended to copy too
* list_copy = list_org.copy() or list(list_org) or list[:] => if append to org not appended to copy.

### Tuples:
Ordered. - Immutable - allows duplicate elements
* my_tuple = ("Max") => identified as a string ( only in single element tuple )
* my_tuple = ("Max", ) => identified as a tuple
* Negative Index a(-1) => latest index
* my_tuple[0] = "Parsa" => Error because immutable.
* tuple(my_list) and list(my_tuple)
* a[::-1] => latest number means step => here means reversed step, if 2, 2 step 2 step
 ```python
my_tuple = (0,1,2,3,4)
i1, *i2, i3 = my_tuple
print(i2) # [1,2,3]
```
* tuples in time and memory usage is better than lists (but immutable)


### Dicts
Key-value pairs, Unordered, Mutable
* dict(name="A") is = {'name' : 'A'}
* del my_dict['name'] => delete key and value
* my_dict.popitem() => pop latest (right) key and value from dict
* my_dict.keys() => all keys .values() => all values, key value in my_dict.items() both :/
* dict_copy = dict_org => if changed  org, change copy too
* dict_copy = dict_org.copy() or dict(dict_org) => if change org not chamge copy.
* my_dict.update(dict(name="B", age=2))
* my_dict = {(1,2) : 5}, key cannot change in this example because tuples are immutable

## Sets

Unordered - Mutable - no duplications
* set('Hello') => {'o', 'l', 'H', 'e'}
* empty set => `a = set()` a= {} is empty dict
* myset.add(1)
* myset.remove() => if not found in set error occured, 
* myset.discard() => if not found in set nothing happend.
* my_set.clear() => remove all
* my_set.pop() => returns first item of set and pop it from set ex: print(my_set.pop()) => 1
* union => first_set.union(second_set) => odds.union(evens) => all numbers
* intersection => odds.intersection(evens) => set() or empty set => odds.intersection(primes)
* diff = setA.difference(setB) => members of A that not exist on B
* sym_diff = setA.symmetric_difference(setA) => Members of A that not exist on B + Members of B than not exists on A
* setA.intersection_update(setB)
* setA.difference_update(setB)
* setA.symmetric_difference_update(setB)
* setA.issubset(setB)
* setA.issuperset(setB)
* setA.isdisjoint(setB) => without any intersection
* setB = setA => also original one changed
* setB = setA.copy() or set(setA)
* a = frozenset([1,2,3,4]) => add, remove and ... not work on it

## Strings
Ordered - immutable - text representation
my_string[0] = 'a' => Error
my_string[::-1] => reverse
my_string.strip() => removes whitespaces
my_string.startswith("hello") / my_string.endswith("world")
my_string.find("substring") => returns index or -1
my_string.count("substring") / my_string.replace('World', "Universe")
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
