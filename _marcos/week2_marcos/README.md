# Week 2 — Outcomes  

## Q1. What is a module in Python? How do you create one?  
A **module** is a single `.py` file with code you can import.

**Create a module (single file):**  
`greeter.py`
```python
def greet(name):
    return f"Hello {name}"
```

`main.py`
```python
import greeter
print(greeter.greet("Marcos"))
```

A **package** is a **folder** that groups modules. It contains an `__init__.py` file so Python treats the folder as a package.

```
src/
  __init__.py       # marks the folder as a package
  greeter.py
```

`src/greeter.py`
```python
def greet(name):
    return f"Hello {name}"
```

`main.py`
```python
from src.greeter import greet
print(greet("Marcos"))  # Hello Marcos
```

---

## Q2. What is the purpose of the import statement in Python? Can you provide a code example of its usage?  
The `import` statement lets us use code from another file. It allows us to separate code into smaller files and reuse them.

**Example:**  
`farewell.py`
```python
def bye(name):
    return f"Goodbye {name}"
```

`main.py`
```python
import farewell
print(farewell.bye("Ana"))  # Goodbye Ana
```

---

## Q3. How can you import only a specific function or class from a module in Python? What is the syntax for this?  
You can import only what you need using `from ... import ...`. This makes the code shorter.

**Example:**  
`math_ops.py`
```python
def add(a, b): 
    return a + b

def sub(a, b): 
    return a - b
```

`main.py`
```python
from math_ops import add
print(add(5, 3))  # 8
```

---

## Q4. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?  
Python passes the **reference to the object** into the function.  
- If the object is **mutable** (like a list), changes inside the function also change the original.  
- If you reassign the variable inside the function, it does not affect the original outside.  

**Example:**  
```python
def add_item(things):
    things.append("new")

items = ["old"]
add_item(items)
print(items)  # ['old', 'new']
```

---

## Q5. Given the following Python code, what will be the output and why?  

```python
def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)
```

**Answer:**  
The output is:  
```python
['original', 'new']
```

Because `lst.append("new")` changes the original list, but `lst = ["completely", "new"]` only creates a new list inside the function.