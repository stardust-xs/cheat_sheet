# Python Operators

In Python, operations on variables look similar to a mathematical expressions with some minor differences. Therefore, all the rules of basic mathematical properties like **[Associative property](https://en.wikipedia.org/wiki/Associative_property)**, **[Commutative property](https://en.wikipedia.org/wiki/Commutative_property)**, etc. apply in Python too but you need to be **explicit**.

There are couple of operators like **Arithmetic operations**, **Assignments operations**, **Comparison operations** (Relational operations), **Logical operations** and **Identity-Membership operations**. We'll see them in detail below.

## Arithmetic operators

The basic **[Arithmetic operations](https://en.wikipedia.org/wiki/Arithmetic#Arithmetic_operations)** in Python are **addition**, **subtraction**, **multiplication**, **division**, **floored division**, **modulus** and **exponential** operations.

**Note:** These can be performed only on **numbers** with some exceptions for **strings** and **lists**.

### Addition

Addition is the most basic operation of arithmetics, done with an addition operator (**+**).
Addition is **commutative** and **associative**, so the order in which terms are added does not matter.

**Note:** This is true only for adding numbers.

```python
var_1, var_2 = 415, 5 # Parallel variable assignment
total = var_1 + var_2 # total = 420
```

In Python, we can take addition to one step further. Python supports addition of **strings** and **lists** too.

```python
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]

total = list_1 + list_2 # total = [1, 2, 3, 4, 5, 6] - This is called List extension.
```

and

```python
str_1 = "Hello"
str_2 = "World"

total = str_1 + str_2 # total = "HelloWorld" - This is called String concatenation.
```

**Note:** You can perform addition only on values of **same** datatype. Performing addition on variables of different datatype will throw **TypeError**.

### Subtraction

Subtraction is **opposite** of addition, done with minus operator (**-**). Subtraction is neither **commutative** nor **associative**, so the order in which terms are subtracted does matter alot. Subtraction is only supported by numbers in Python.

```python
var_1, var_2 = 425, 5
total = var_1 - var_2 # total = 420
```

### Multiplication

Multiplication is also **commutative** and **associative** like addition and it is **[distributive](https://en.wikipedia.org/wiki/Distributive_property)** as well. It is done with multiplication operator (**\***).

```python
var_1, var_2 = 42, 10
total = var_1 * var_2 # total = 420
```

Just like addition, multiplication can be performed on **strings** and **lists**.

```python
list_1 = [1, 2, 3]
total = list_1 * 3 # total = [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

and

```python
str_1 = "Ha"
total = str_1 * 3 # total = "HaHaHa"
```

**Note:** You can perform multiplication of **lists** and **strings** with **integers** only.

### Division

Division is essentially **opposite** of multiplication, done with slash operator (**/**). Like subtraction, division is also neither **commutative** nor **associative**, so the order in which terms are divided does matter alot. Division is only supported by **numbers** in Python and output of division operation always returns a **float** value.

```python
var_1, var_2 = 4200, 10
total = var_1 / var_2 # total = 420.0
```

**Note:** Division returns **quotient** in **float**.

### Floored division

Floored division is just like normal division but this return an **integral** part of the output value. Means it always returns an **integer** part before the decimal. Floored division is carried out with **"//"** operator in Python.

```python
# Normal Division:
var_1, var_2 = 25, 9
total = var_1 / var_2 # total = 2.7777777777777777

# Floored Division:
var_1, var_2 = 25, 9
total = var_1 // var_2 # total = 2
```

**Note:** Floored division returns **quotient** as **integer without rounding-off** the value.

### Modulus

Modulus or **[Modulo](https://en.wikipedia.org/wiki/Modulo_operation)** operation returns **remainder**. It is carried out using **"%"** operator in Python. The output of a modulus operation could be either **float** or **integer** depending upon the **type** of the operands.

```python
var_1, var_2 = 4200, 10
total = var_1 % var_2 # total = 0
```

### Exponentiations

**[Exponentiation](https://en.wikipedia.org/wiki/Exponentiation)** or Powers in python are represented using **"\*\*"** (double asterisk) operator. Like modulus, the output of exponentiation operation could also be either **float** or **integer** depending upon the **type** of the operands.

```python
var_1, var_2 = 2, 3
total = var_1 ** var_2 # total = 8
```

## Assignment operators

**[Assignments operations](https://en.wikipedia.org/wiki/Augmented_assignment)** are carried out using **[Augmented assignment](https://en.wikipedia.org/wiki/Augmented_assignment)** or **Compound assignment**.

An augmented assignment is generally used to replace a statement where an operator takes a variable operates on it and then assigns the result back to the same variable.

We can perform Assignment operations for basic arithmetic operators since this method is a short-hand (shortcut) for writing the arithmetic expression. Also Assignment operations are neither **commutative** nor **associative** so the sequence of operands **does** matter a lot.

**Note:** Please remember all the execution or operations on objects in Python happen from **right to left**.

### Addition assignment

This is how we write Addition assignment.

```python
var_1, var_2 = 415, 5
var_1 += var_2 # var_1 = 420

# This is basically
var_1 = var_1 + var_2
```

**Note**: Please note that the first object (object to the left-hand side) gets assigned with the output.

### Subtraction assignment

This is how we write Subtraction assignment. Execution is **similar** to that of Addition assignment.

```python
var_1, var_2 = 425, 5
var_1 -= var_2 # var_1 = 420

# This is basically
var_1 = var_1 - var_2
```

### Multiplication assignment

This is how we write Multiplication assignment. Again execution is **similar** to that of above assignment methods.

```python
var_1, var_2 = 42, 10
var_1 *= var_2 # var_1 = 420

# This is basically
var_1 = var_1 * var_2
```

### Division assignment

This is how we write Division assignment. **Similar** execution as above. This too will return **float** as output by default.

```python
var_1, var_2 = 4200, 10
var_1 /= var_2 # var_1 = 420.0

# This is basically
var_1 = var_1 / var_2
```

### Floored division assignment

This is how we write Floored division assignment.

```python
var_1, var_2 = 4200.0, 10.0
var_1 //= var_2 # var_1 = 420

# This is basically
var_1 = var_1 // var_2
```

### Modulus assignment

This is how we write Modulus assignment.

```python
var_1, var_2 = 420, 10
var_1 %= var_2 # var_1 = 0

# This is basically
var_1 = var_1 % var_2
```

### Exponentiation assignment

This is how we write Exponentiation assignment.

```python
var_1, var_2 = 2, 3
var_1 **= var_2 # var_1 = 8

# This is basically
var_1 = var_1 ** var_2
```

## Comparison operators

**[Comparison operations](https://en.wikipedia.org/wiki/Relational_operator)** or **Relational operations** are carried out to check the **similarities** in Python object. These return **boolean** and are usually used in **If - Else** conditional loops.

Read more **[here](https://en.wikipedia.org/wiki/Relational_operator#Sameness_(object_identity)_vs._content_equality)**. This article will help you understand how, when and why to use **Comparison operations**.

### Equal to

**Equal to** operations are carried out using the **Equality**, **"=="** (double equal to) operator in Python. Equal to is **commutative**.

```python
var_1, var_2 = 69, 69
output = var_1 == var_2 # output = True

var_1, var_2 = 619, 69
output = var_1 == var_2 # output = False
```

### Not equal to

**Not equal to** operations are carried out using **"!="** operator in Python. Like Equal to, Not equal to is **commutative** too.

```python
var_1, var_2 = 69, 69
output = var_1 != var_2 # output = False

var_1, var_2 = 619, 69
output = var_1 != var_2 # output = True
```

### Less than, Greater than, LTET and GTET

These are the obvious ones.

```python
# Less than operation
var_1, var_2 = 69, 420
output = var_1 < var_2 # output = True

# Greater than operation
var_1, var_2 = 619, 69
output = var_1 > var_2 # output = True

# Less than equal to operation
var_1, var_2 = 420, 420
output = var_1 <= var_2 # output = True

# Greater than equal to operation
var_1, var_2 = 619, 69
output = var_1 >= var_2 # output = True
```

## Logical operators

**[Logical operations](https://en.wikipedia.org/wiki/Logical_connective#Computer_science)** are the ones which usually revolves around the concepts of **[logical gates](https://en.wikipedia.org/wiki/Logic_gate)** in Digital Electronics and kinda works exactly like the same. These are **usually\*** used along in the Comparison operations.

The output of the logical operations is often in **0** and **1**.<br>**None**, **False**, **0** (integer/float), **\[\]** (empty list) and **{}** (empty dictionary) are considered to be **0** in Logical operations and rest are considered as **1**.

**Note:** Booleans are **subclass** (child class) of **Integers**, hence in Python **0** and **1** can also be resolved or treated as **False** and **True** respectively.

### Logical AND

If all values are **True** output will be **True**. Treat **AND** operation as **multiplication** (at least for understanding).
See this table:

| Operand 1 | AND | Operand 2 | Output |
|:---------:|:---:|:---------:|:------:|
|     0     |  .  |     0     |    0   |
|     0     |  .  |     1     |    0   |
|     1     |  .  |     0     |    0   |
|     1     |  .  |     1     |    1   |

```python
var_1, var_2 = 420, 420  # Non - Zero values represent True
output = var_1 and var_2 # output = 420 (This represents 1 or True)

var_1, var_2 = [], 420
output = var_1 and var_2 # output = [] (This represents 0 or False)
```

**Important Tip:** If both the operands are False, **first operand** will be considered as the output.

### Logical OR

If all values are **False** output will be **False**. Treat **OR** operation as **addition** (at least for understanding).
See this table:

| Operand 1 | OR | Operand 2 | Output |
|:---------:|:--:|:---------:|:------:|
|     0     |  + |     0     |    0   |
|     0     |  + |     1     |    1   |
|     1     |  + |     0     |    1   |
|     1     |  + |     1     |    1   |

```python
var_1, var_2 = 420, 420  # Non - Zero values represent True
output = var_1 or var_2  # output = 420 (This represents 1 or True)

var_1, var_2 = [], 0
output = var_1 or var_2  # output = 0 (This represents 0 or False)
```

**Important Tip:** If both the operands are False, **last operand** will be considered as the output.

### Logical NOT

This is a simple negation.

```python
var_1 = 420         # Non - Zero value represent True
output = not var_1  # output = False

var_1 = 0           # False value
output = not var_1  # output = 1 (This represents True)
```

## Identity - Membership operators

### Identity operator

Identity operator works on the **id** of the object. If the identity of the objects (ids) is same then it'll return **True** else **False**. It is carried out using the "**is**" keyword.

```python
x = ["a", "b", "c"]
y = ["a", "b", "c"]
x is y  # Returns False
```

This returns **False** because although the object (["a", "b", "c"]) look equal but they're not referencing to the same object i.e their ids are different.

```python
id(x)  # Returns id as 139644023985664
id(y)  # Returns id as 139644025323776
```

Please do no get confused Identity of an object and Equality of the object. Objects may look equal but cannot be the same.
Well there are few exceptions to this clause, integers from **-5** to **256**, **strings** and **Singetons** would return **True** for the above test. This is because of the way Python is implemented and this is one of the implementation detail.

### Membership operator

In python, "**in**" is the membership operator where it checks if an object is present **in** a Container object. If the object is present in the other object then it'll return **True**, else **False**.

```python
x = ["a", "b", "c"]
"a" in x  # Returns True
"z" in x  # Returns False
```

It doesn't matter how many objects are present in the container, if the object is present it will return **True**.
