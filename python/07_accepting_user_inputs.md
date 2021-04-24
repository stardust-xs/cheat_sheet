# Accepting User Inputs

Up until now we've been assigning or hard coding the values to the variables. But we may come across instances where we need to take dynamic inputs from the user. This is where Python's builtin `input` function comes handy.

This function is dead simple and straightforward in usage.<br>It suspends the control flow until the input is provided by the user. Please note that the output of the `input` function is always a string. So you may need to do the type conversion whenever you need to work with other data structures beyond strings.

This is how you use `input` function
```python
>>> print(f"Hello {input()}")  # This will wait until an input is provided
XA                             # Input provided to the execution
Hello XA                       # Output
>>>
```
