# Python Variables

Variables are **placeholders** or **pointers** to an *object* in any programming language. Their concept is same across all programming paradigms. This is how we write variables in Python, `var_1 = 10` or `var_2 = "Python string"`.

Here, **10** is an **integer**  value stored somewhere in Python's **[heap memory](https://docs.python.org/3/c-api/memory.html#overview)** (memory) and `var_1` is the pointer to this integer object similarly **"Python string"** is the **string** value stored somewhere again in Python's **heap memory** and `var_2` is the pointer to this string object. So we casually say it like, `var_1` has value of **10** and `var_2` has value of **Python string** assigned to it.

In *Pythonic* terms, expressions (statements) or objects like **10** or **"Python string"** are considered to be **[Literals](https://docs.python.org/3/reference/expressions.html?highlight=identifier#literals)**. Basically all **constants** like strings, numbers and booleans are considered as **Literals**. This is because they literally mean exactly what they are whereas, `var_1` and `var_2` are called as **[Identifiers](https://data-flair.training/blogs/identifiers-in-python/)**, because they used to identify or find or point to the object's location in Python's **memory**.

**Note:** We normally use **identifiers** and **variables** interchangeably, and that's fine until we know what is what!

## Restrictions on variable names

These identifiers have certain rules or restrictions that every developer must follow while creating them. They are as follows:

- The variables can consist of **letters**, **digits**, or **underscores** ("\_") and they **must start** with a letter.
  - Although it is not mandatory to use combination of letters, digits and an underscore always.
  - We can create variable names with either all letters, prefixed underscores or in combination of all.
  - One must remember of starting the variable name with a letter **always**.
  - For example: `xa`, `xames3`, `xa_mes3`, `XaMeS3` and `_xames3` all are considered to be **valid** variable names.

- Punctuation and blanks are **not allowed** in variables.
  - In case you need to define a longer identifier name, then replace the spaces with underscores.
  - For example: `long variable name = "something"` is **syntactically incorrect**.
  - To use longer identifier name, replace spaces with underscores like this: `long_variable_name = "something"` :heavy_check_mark:.
  - In Python, using punctuations (any symbols except underscore) as an identifier name will throw **SyntaxError**.

- Skip using **reserved** keywords.
  - There are some words that are **reserved** for special use in Python. These words are called as **[keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)**.
  - Here's a complete list of all the keywords in Python:

    ```python
        False      await      else       import     pass
        None       break      except     in         raise
        True       class      finally    is         return
        and        continue   for        lambda     try
        as         def        from       nonlocal   while
        assert     del        global     not        with
        async      elif       if         or         yield
    ```

    This list keeps changing with new python versions.

- Python is **[case-sensitive](https://en.wikipedia.org/wiki/Case_sensitivity#In_programming_languages)** programming language and so are the **variables**.
  - For example: `var`, `VAR`, and `VaR` are all **different** variables.
  - Be sure to be consistent with your variables throughout your code to maintain resuability.
  - Preferable case for creating variable is a **[Snake Case](https://en.wikipedia.org/wiki/Letter_case#Special_case_styles)**.

- Meaningful names for variables are important for the developers who are looking at your programs, understanding and revising them. This is very important when more than one developer is working on a piece of code.

**Note:** Please note that there's difference between keywords and built-in classes.

## Variable assignments

Python is a **[dynamically](https://en.wikipedia.org/wiki/Dynamic_programming_language)** typed language. We don't need to declare variables like C, C++. To create an variable, we just assign a value and then start using it. Assignment is done with a single equal sign (**=**). Variable assignment is of **O(1)** complexity in Python.

### Augmented assignment

Like C, Python allows something called as **[Augmented assignment](https://en.wikipedia.org/wiki/Augmented_assignment)** or **Compound assignment**.

An augmented assignment is generally used to replace a statement where an operator takes a variable operates on it and then assigns the result back to the same variable.

```python
>>> xa = 10   # Simple assignment
>>> xa += 42  # Augmented addition
>>> xa *= 42  # Augmented multiplication
```

### Chained assignment

Python allows something called as **[Chained assignment](https://en.wikipedia.org/wiki/Assignment_(computer_science)#Chained_assignment)**, which makes it possible to assign the same **value** (object) to multiple variables simultaneously.

```python
>>> a = b = c = 42
>>> a
42
>>> b
42
>>> c
42
>>>
```

Here, value of **42** is assigned to all the variables `a`, `b` and `c`.

**Note:** This is a nice and clean way of assigning same object to multiple variables at once but is little risky as this could potentially affect the values of other variables if not proceeded with caution.

### Multiple variable assignment

Like C, Python also allows **[Multiple variable assignment](https://en.wikipedia.org/wiki/Assignment_(computer_science)#Parallel_assignment)** or **Parallel assignment**, which essentially means more than one identifier can be assigned to multiple **literals**.

```python
>>> xa, mes3 = "XA", "MES3"
>>> xa
'XA'
>>> mes3
'MES3'
>>>
```

Here it means, `xa = "XA"` and `mes3 = "MES3"` in simple terms.

**Note:** Ensure the number of variables on left-hand side is **equal** to number of objects on right-hand side (Currently we're assuming this for variable assignments only). Assigning multiple values to a single identifier on the other hand is going to create a **tuple**.

## What happens when we assign values to variables

When we write `var_1 = 42`, the **[interpreter](https://en.wikipedia.org/wiki/Interpreted_language)** does the following:

- Remember this! In Python, the statements (expressions) execute from **right to left**.
- Python creates object in memory, the value of **42** somewhere in its memory randomly. This is called as **initialization**.
- The Python interpreter now will try to understand what exactly the type of the object is. This process is like an **analysis**.
- Once it understands that its an integer object, it will initialize an integer class and then assign the value of **42** to the variable `var_1`.

## Type of variables

Generally speaking there are 2 types of variables, **Global** and **Local** variables and they operate exactly the way they sound.

### Global variables

These are referred as **[Public](https://en.wikipedia.org/wiki/Global_variable#Java)** variables in Java.

- Global variables are the ones which are available globally across your entire Python script.
- They're accessible in your entire script at any point presuming they're not deleted.
- They can also be created by prefixing **[global](https://docs.python.org/3/reference/simple_stmts.html#global)** keyword in a class or a function to extend it outside its scope.
- Globals should be used **sparingly**! As they have potential of changing the values across your entire Python script.
  Read more **[here](https://medium.com/better-programming/alternatives-to-using-globals-in-python-a3b2a7d5411b)**.

### Local variables

These are referred as **[Private](https://en.wikipedia.org/wiki/Class_(computer_programming)#Member_accessibility)** variables in Java.

- Opposite of Global variable in a sense.
- Accessible only in loops and class and functions.
- They act like a **private** property or object in a callable (class or function) object.

## How to delete variables

Deleting a variable in Python is easy. Prefix **[del](https://docs.python.org/3/reference/simple_stmts.html#del)** to an identifier and it gets deleted as simple as that.
Ensure that you don't prefix it while writing an expression. Otherwise, it'll throw **SyntaxError**.

For example: `del some_variable` is :heavy_check_mark: while `del some_variable = "some value"` is :x:!

Other ways of deleting an identifier or variable references are:

- Setting value as `None` (not really).
  - This is one of the misconception that lies around in Python.
  - You can assign **None** to an identifier to update the reference to the object.
  - Identifier will be now pointing to the newly assigned None object but the previous object may or may not remain in the memory.

- Using class methods (Only for iterables).
  - This method is applicable only to **iterators** or **containers**.
  - This method relies on understanding the concepts of **Object Oriented Programming**.

## How to delete values of a variable

You **don't**!

When we create an object and if it is being used by your script, we can assign or delete multiple references to that object as per our requirements. But when the number of references (pointers pointing) to a particular object becomes **zero**, it is **no longer** accessible!

It means the value or object stored in the memory is officially **deleted** by Python.

```python
>>> xa = "XAMES3"
>>> print(id(xa))
139635360436592
>>>
```

We'll create one more reference to the same **"XAMES3"** object.

```python
>>> xames3 = "XAMES3"
>>> print(id(xames3))
139635360436592
>>>
```

Now for some reason we deleted or updated both the variables `xa` and `xames3`. This ensures the count of variables pointing to the **"XAMES3"** has dropped to **0**.

```python
>>> del xa               # Deleted xa
>>> xames3 = "God-Tier"  # Updated xames3
```

Python keeps a track of unused/un-referred objects. And when it feels that the user is not using it, it deletes it so that the occupied memory could be released and thus making it available for something else. This process is called **"Garbage Collection"** in computer science.

So, when we re-create the same **"XAMES3"** object and check its `id()` it is going to be different.

```python
>>> xa = "XAMES3"
>>> print(id(xa))
139635360541896
>>>
```
**Tip:** For the sake of optimization, Python assigns lower memory addresses to values in range of **-5** to **256**.<br>Try this out:

```python
print(id(5), id(-2), id(100), id(256), id(257), id(1000), sep="\n")
```
