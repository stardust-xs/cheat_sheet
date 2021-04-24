# Data Structures in Python

**Data Structure** or **[Datatypes](https://en.wikipedia.org/wiki/Data_type)** are the one of the fundamental concepts in **computer science** and in all programming paradigms. In simple terms it means the **type** of data. Now this data is often referred as an **object** in python.

There are a lot of data structures, ranging from the most primitive or basic type like lists, tuples, etc to more complicated types like pandas series or numpy ndarrays. For our sake of sanity we'll start with the most basic types in python.

The most basic types of python **[built-in](https://docs.python.org/3/library/stdtypes.html?highlight=list#built-in-types)** objects are numeric type (**[int/float/complex](https://docs.python.org/3/library/stdtypes.html?highlight=list#numeric-types-int-float-complex)**), strings (**[str](https://docs.python.org/3/library/stdtypes.html?highlight=list#text-sequence-type-str)**), lists (**[list](https://docs.python.org/3/library/stdtypes.html?highlight=list#lists)**), dictionaries (**[dict](https://docs.python.org/3/library/stdtypes.html?highlight=list#mapping-types)**), sets (**[set](https://docs.python.org/3/library/stdtypes.html?highlight=list#set-types-set-frozenset)**), tuples (**[tuple](https://docs.python.org/3/library/stdtypes.html?highlight=list#tuples)**) and booleans (**[bool](https://docs.python.org/3/library/stdtypes.html?highlight=list#boolean-values)**). Data structures mainly help the python interpreter to understand the type of object it is working with and then it prepares the interpreter to be ready to execute a particular operation on the data.

Before understanding data structures, we need to understand type of data (**object**) in python.

## Type of Data

In Python, objects come in all shapes and sizes. But if you want to understand data structures my way, we'll classify it into **two** major types: **Single type** and **Containers type** data.

### Single Type

Single type data (object) is a **single entity** assigned to a variable. Strings, Numbers, NoneType (**[None](https://docs.python.org/3/library/constants.html?highlight=nonetype#None)**), Boolean (**[bool](https://docs.python.org/3/library/functions.html#bool)**), etc are examples of Single type data. We can consider them as **constants** or **[Literals](https://github.com/xames3/python_tuts_v2/blob/master/basics/0200_variables_in_python.md#introduction)**. Read more here about **[built-in constants](https://docs.python.org/3/library/constants.html?highlight=nonetype#built-in-constants)** in python.

#### Strings (str)

By definition, *strings are **[immutable](https://github.com/xames3/python_tuts_v2/blob/master/basics/0301_types_of_data_in_python.md#immutable-objects)** sequences or collections of **characters***.

Strings are what I like to call, "**Kachha Limbu**" in python. It behaves like both Single type and a Container type object. Strings are often referred as **Text sequence type** as they are literally a sequence (collection) of **characters** or **texts**. Unlike C, in python we don't have a dedicated **char** datatype. Hence, even a single character is also considered as **string**.

Anything and everything wrapped in pair of either single quotes (**'like this'**), double quotes (**"or like this"**) or even triple quotes (**'''or even like this'''**) and (**"""this too...sigh"""**) is considered as a **string** object. Triple quotes are often used for writing string object that span over multiple lines. String objects can have one or multiple characters.

```python
# Single quotes
# These quotes are useful for writing strings which use ("") in statements.
'I am not able to "see him".'

# Double quotes
# These quotes are useful for writing strings which use apostrophe (') in statements.
"Of course you can't see him, he's John Cena!"

# Triple quotes
# These are helpful for writing long paragraphs or multi-line statements.
"""
I thought this is good example for displaying
Multi-line statements but turns out it's not!
You guys have a better suggestion?
"""
```

#### Numbers (int/float/complex)

There are three distinct numeric types: **integers**, **floating point** numbers, and **complex** numbers. In addition, Booleans are a subtype (child) of integers. Integers have **unlimited precision**.

Numbers are created by numeric literals (constants **0-9**). Numeric literals containing a decimal point (**.**) or an exponent sign (**e**) yield floating point numbers. Adding **'j'** or **'J'** to a numeric literal yields an imaginary number (a complex number with a zero real part) which you can add to an integer or float to get a complex number with real and imaginary parts. They support all sort of arithmetics. Please see **[this](https://github.com/xames3/python_tuts_v2/blob/master/basics/0201_operations_on_variables.md#arithmetic-operations)** for quick reference.

These are few ways of representing Integers in python:

```python
>>> var_1 = 69              # Unsigned int
>>> var_2 = -69             # Signed int
>>> var_3 = 69_000_000      # Integer with commas (69,000,000)
```

These are few ways of representing Floats in python:

```python
>>> var_1 = 69.0            # Unsigned float
>>> var_2 = -69.0           # Signed float
>>> var_3 = 69_000_000.420  # Float with commas (69,000,000.420)
>>> var_4 = 6.9e+8          # Exponents
```

This is how we represent Complex in python:

```python
>>> var_1 = 69j             # Only imaginary part
>>> var_2 = 420 + 69j       # With real part
```

#### Booleans (bool)

By definition, *Booleans mean either of the two literals (constant) objects **False** and **True**.*

They are used to represent truth values. Also Booleans are subclass (child class) of Integers, hence in python 0 and 1 can also be resolved or treated as False and True respectively.

```python
>>> xa_is_god = True
>>> xa_is_mortal = False
```

#### None (NoneType)

By definition, *None represents the absence of a value or **[null](https://docs.python.org/3/library/stdtypes.html?highlight=list#the-null-object)**.*

None is a **singleton** (fancy advance concept that we will explore later). Python uses the keyword **None** to define null objects and variables.

This is how we write None:

```python
>>> xa = None
```

**Note:** None resets the variable. It **doesn't** delete it.

### Container Type

Container objects in this context means any python object that holds multiple elements. In simple terms, containers are exactly what it sounds like - they contain **elements**. These containers are special and play very important role in python's ecosystem. Strings, Sequences (**[list](https://docs.python.org/3/library/stdtypes.html?highlight=list#list)**/**[tuple](https://docs.python.org/3/library/stdtypes.html?highlight=list#tuple)**), Dictionaries (**[dict](https://docs.python.org/3/library/stdtypes.html?highlight=list#mapping-types-dict)**) and Sets (**[set](https://docs.python.org/3/library/stdtypes.html?highlight=list#set-types)**) etc are examples of Container type data.

#### Lists (list)

Lists are probably one of the most used and simplest data structure in python which is used to **contain** (hence a container) or store or hold a **list** of values.

Technically, a "*List is an **ordered** collection of elements.*"

But what does **ordered** means? Ordered means having **index** and retaining the **order** of creation in layman terms. Lists have **[indexes](https://en.wikipedia.org/wiki/Index_notation#In_computing)** or **index notations**. Hence, we can access elements of a list using its **index** position. In python, the index starts with **zero**.

```python
>>> xa = []                                       # Empty list
>>> xa = ["Srusthi"]                              # List with single element
>>> xa = ["Shailesh", "Shivam", "Sagar"]          # List of all string elements (array)
>>> xa = [True, 4.0, 5, "6", None, _, 4.0, None]  # List of elements with different datatypes and duplicates
```

Lists can hold virtually any valid python object and need not to be homogeneous (same elements). There are **no restrictions** on having number of elements in a list but lists are always **definite**! Meaning all the elements in the **square brackets** seperated by **commas** will be part of the list. There can be an empty list (zero elements), there can be list with only one element or there could be multiple elements. A list could nest another list too.

#### Tuple (tuple)

Like Lists, Tuples are another **sequence type** data structure in python. If you understand lists, you'll be able to understand tuples in no time! Like lists, tuples also have **indexes** hence you can access elements of a tuple like a list. Tuples are written with **round brackets** with elements separated with **commas** in python.

By definition, ***~~List~~** Tuple is an **ordered** collection of elements but its **immutable**.*

```python
>>> xa = ()                                   # Empty tuple
>>> xa = ("Ashish",)                          # Tuple with single element, the comma is very important
>>> xa = ("CR07", "Game Player", "Shubham")   # Tuple of all string elements
>>> xa = (None, "DBZ", 42.0, tuple(), "DBZ")  # Tuple of elements with different datatypes and duplicates
```

Tuple can also hold virtually any valid python object and need not to be homogeneous (same elements). Similarly, there are **no restrictions** on having number of elements in a tuple and are **definite** too. There can be an empty tuple (zero elements), there can also be tuple with only one element or there could be multiple elements. A tuple could nest another tuple too just like a list.

**Note:** Tuples are **faster** than a list in terms of program execution.

#### Dictionary (dict)

By definition, *Dictionaries are **unordered** collection of a **key-value** pairs*.

Dictionaries are unordered means, it doesn't support indexing and the order of the **"elements"** are not retained after the creation. Well, it is not completely **true**! Python 3.6 and up **retains** a dictionary's order. This is an implementation detail. Dictionaries are created using **curly brackets**, where the key-value pairs are separated by **commas** in python.

There are some important things to note before creating a dictionary:

- A dictionary needs to have a key-value pair.
- The dictionary keys must be unique (not a compulsion though).
- Key must be an immutable object.
- A dictionary can be empty.
- Dictionary values can hold nested objects.

```python
>>> xa = {}                                         # Empty dictionary
>>> xa = {"name": "XA"}                             # Dictionary with single key-value pair
>>> xa = {"name": "XA", "age" : 25, "type": "God"}  # Dictionary with multiple key-value pairs
```

Here for the last example, **"name"** is the key whose paired value is **"XA"**. Similarly, for **"age"** its respective value is **25** (integer) and so on. This tells us value of a key-value pair of a dictionary object could be of any datatype.

#### Set (set)

By definition, *Sets are **unordered** collection of **unique** elements.*

Like dictionaries, these are unordered too, meaning the elements of a set cannot be accessed using an **index**. These is for a special reason. Since, a **set** is a collection of **unique** elements the duplicates are ignored and so is their **index**. It would be difficult to visualize this so its better to test it out by ourselves.

The whole concept of set is based on **Set Theory**. Just like a dictionary, sets are created using **curly brackets** with elements seperated by **commas** in python but you **cannot** create an empty set using this method. Since a pair of curly brackets **{}** resembles an empty dictionary, we need to use the **built-in** set type for creating an empty set.

```python
>>> xa = set()                                                     # Empty set
>>> xa = {"Shivam"}                                                # Set with single element
>>> xa = {True, "Gamer", 42.0, "Daulat", 69, range(10), "Daulat"}  # Set of elements with different datatypes and duplicates
```

Here for the last example, we can see there are **duplicates**. By definition, we cannot have duplicates in sets and hence when you print the output of last example, you'll get something like this

```python
>>> xa
{True, range(0, 10), 69, 42.0, 'Game', 'Daulat'}
>>>
```
