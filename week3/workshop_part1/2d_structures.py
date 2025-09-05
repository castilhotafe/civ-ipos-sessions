# # Exercise 1: manually create a 2D data structure
# my_2dim_list = [
#     [0, 1, 2],
#     [3, 4, 5],
#     [6, 7, 8]
# ]
#
# print(my_2dim_list)
# # # random access
# print(my_2dim_list[0])
# print(f"The element on index 1 is {my_2dim_list[1]} and "
#       f"the element two is  {my_2dim_list[1][2]}")
#
# # # Exercise 2: sequential iteration over 2D - aka sequential access
# # for row in my_2dim_list:
# #     for grid_square in row:
# #         # check, change remove, set initial
# #         print(grid_square)
#
# # Exercise 3: build a 2D data structure and initialise with values
def make_2d(rows, columns, value=None):
    '''
    # Create a rows x cols 2D data structure
    # initialised to default or starting value
    # Example:
    # >>> make_2d(3, 3)
    # returns: [[None, None, None], [None, None, None], [None, None, None]]
    '''
    list_2d = []
    for _ in range(rows):
        elems = []
        for _ in range(columns):
            elems.append(value)
        list_2d.append(elems)

    return list_2d


# Exercise 3a: Refactor to list comprehension
def make_2d_cool(rows, cols, value=None):
    '''Same function as above implemented as a list comprehension
    Returns a rows x cols grid filled with `value`.
    '''
    return [[value for _ in range(cols)] for _ in range(rows)]


# Example 2 — multiplication table
# This code gives us [[1, 2, 3], [2, 4, 6], [3, 6, 9]] when rows=3, cols=3
def mult_table(rows, cols):
    return [[(i + 1) * (j + 1) for j in range(cols)] for i in range(rows)]


# Example 3 — sequential numbers row-by-row
# This gives us [[1, 2, 3], [4, 5, 6], [7, 8, 9]] when rows=3, cols=3
def sequential_grid(rows, cols):
    return [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]


# # Drive the code above...
print('#'*20)
# --- 3 ---
print(make_2d(3, 3))
print(make_2d(3, 3, 42))

print('#'*20)
# # --- 3a ---
print(make_2d_cool(3, 3, None))
print(mult_table(3, 3))
print(sequential_grid(3, 3))
print('#'*20)


# Numpy & Pandas examples - view in Pycharm
# import numpy as np
# import pandas as pd
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#
# arr2 = arr * 2
#
# df = pd.DataFrame({
#     'A':[1,2,3],
#     'B':[4,5,6],
#     'C':[7,8,9]
# })
#
# print()

