# Running Python

## Starting Python session
The most common way of getting started with python is by typing `python` in terminal. This will start your Python session.

```bash
$ python
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
Here you can do whatever you want!<br>This is a quick and dirty way of testing or trying out new things in python.

## Running Python code

By running Python code I mean running either python via script or directly as  code.

### DeFacto method

If you have an existing python script (file), then you can invoke the script with `python myscript.py`. This command will run your python file. It is the most common and basic way of running your script. You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#command-line)**.

### Execute command

Execute the Python code in *command* mode. Command can be one or more statements separated by newlines.

```bash
$ python -c 'print("Hello World!")'
Hello World!
```

You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#cmdoption-c)**.

### Execute module

In Python, modules are basically the scripts but without `.py` extension. To execute python modules directly from the terminal, use `python -m <MODULE NAME> <ARGUMENTS...>`

```bash
$ python -m pip install --upgrade pip
```

You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#cmdoption-m)**.

## Miscellaneous options

### Help

Use `-?`, `-h` or `--help` to print a short description of all command line options.

### Version info

Use `-V` or `--version` for printing short version and `-VV` for printing complete version.

```bash
$ python -V
Python 3.8.5

$ python -VV
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0]
```

### Interactive mode

Use `-i` to run your scripts in interactive mode.

```bash
$ python -i myscript.py
```

You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#cmdoption-i)**.

### Anti-Assertion mode

Use `-O` to disable assert statements.

```bash
$ python -O myscript.py
```
You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#cmdoption-o)**.

### Anti-Assertion-Dosctring mode

Use `-OO` to disable assert statements and discard the docstrings.

```bash
$ python -OO myscript.py
```

### No copyright and version info mode

Use `-q` to disable the copyright and version messages in interactive mode.

```bash
$ python -q
>>>

$ python -q myscript.py
>>>
```

### Disable user packages

Use `-S` to disable the loading of user installed packages (*apps*).

```bash
$ python
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
>>> import hannah
>>>

$ python -S
Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
>>> import hannah
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'hannah'
>>>
```

You can read more about this **[here](https://docs.python.org/3/using/cmdline.html#id3)**.

### Verbose mode

Use `-v` to print a message each time a module is initialized, showing the place from which it is loaded. When given twice `-vv`, it prints a message for each file that is checked for when searching for a module.

```bash
$ python -v
```
