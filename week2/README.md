# Week 2 – Modularisation and 2D Structures

## Key Concepts Covered

- **Modularisation** means breaking your code into smaller parts that each do one specific job. These parts can be reused and are easier to work with.

## Questions and Answers

### 1. What is a module in Python? How do you create one?

A module is a piece of code, like a function or a class, that we can import and use in different scripts.  
For example, we have our scripts in the `src` folder, and it also has a `__init__.py` file.  
Let’s say we have a function in our script `my_functions.py` like:

```python
def greet(name: str):
    print(f"Hello, {name}")
```

We can use this function in other files by importing it like this:

```python
from src.my_functions import greet
```

Then we can call the function anywhere we need.

---

### 2. What is the purpose of the import statement in Python? Can you provide a code example of its usage?

The `import` statement is used to bring in code from another module so we can use it outside its original script.

Example:

```python
from src.my_functions import greet as gr

gr("Marcos")
```

Output: `Hello, Marcos`

---

### 3. How can you import only a specific function or class from a module in Python? What is the syntax for this?

Already answered above in question 2.

---

### 4. How would you explain Python's parameter-passing mechanism? Is it more similar to pass-by-value or pass-by-reference?

Python uses a mechanism that is often called "pass-by-object-reference".  
For mutable objects like lists, when we pass them to a function, we are passing a reference to the object in memory, not a copy.

That means if we change the list inside the function, it will also change the original list.

Example:

```python
def add_item(my_list):
    my_list.append("new item")
```

This modifies the original list because we are working with a reference.

So, even though it is not exactly like pass-by-reference in other languages, the behavior is similar for mutable objects.  
That’s different than passing by value, where a copy is created and the original value remains unchanged.  
In Python, immutable types like integers or strings behave this way: changes inside a function don’t affect the original value.

### 5. Given the following Python code, what will be the output and why?

```python
def modify_list(lst):
    lst.append("new")
    lst = ["completely", "new"]

items = ["original"]
modify_list(items)
print(items)
```

**Answer:**

The output will be:

```python
['original', 'new']
```

**Explanation:**

Lists are mutable, so when we pass the list `items` to the function, it is passed by reference.  
The line `lst.append("new")` modifies the original list.  
However, the line `lst = ["completely", "new"]` creates a new local list and assigns it to the local variable `lst`, which does not affect the original list.  
So, only the `append("new")` part has an effect on the original list.

---

### 6. If Python uses pass-by-reference, why doesn't reassigning a variable inside a function change the original variable outside the function? How is this related to the mutability of Python objects?

Python passes objects by reference, but the function parameter is just a **local variable** pointing to the same object.

If the object is mutable (like a list), changes **to the object itself** (e.g. `.append()`) will affect the original.

However, **reassigning the parameter** to a new object **only changes the local variable**, not the original one.

Example:

```python
def modify_list(lst):
    lst.append("new")                 # Affects original
    lst = ["completely", "new"]      # Local reassignment
    return lst

items = ["original"]
result = modify_list(items)
print(items)  # ['original', 'new']
print(result) # ['completely', 'new']
```

So even though Python *passes the reference*, the **name binding** inside the function is independent.

That’s why the original list is only affected by the `.append()` but not by `lst = [...]`.

To keep the new list, we must `return` it from the function.

## Benefits of Modular Coding

1. **Reusability** – You can reuse your functions and modules in other parts of your code or even in other projects.
2. **Maintainability** – It's easier to find and fix bugs, update features, and understand what your code does.

These benefits are very useful when building medium-sized programs. If everything was written in one big file, it would be hard to find where to make changes. Modular code keeps things organized.
