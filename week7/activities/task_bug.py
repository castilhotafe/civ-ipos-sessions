'''A buggy Task Manager that provides an opportunity to debug code by both reasoning about it and stepping through using pdb.

The program has a number of bugs that are introduced one at a time. 

The goal is to find and fix the bugs.

Ensure you step through this program in pdb only to understand how the program works and to find the bugs.'''

# Once debugged add some documentation examples to help the next programmer!
import sys
import pdb
# import os

def add_task(task_list=list, task=str):
    """
    Adds a new task to the list if the input is not empty.

    Parameters
    ----------
    task_list : list
        The list where the new task will be appended.
    task : str
        The task description to be added.

    Returns
    -------
    None
        Returns nothing. Prints a cancellation message if input is empty.
    Examples
    --------
    >>> my_tasks = []
    >>> add_task(my_tasks, "Buy milk")
    >>> my_tasks
    [('Buy milk', False)]

    >>> my_tasks = []
    >>> add_task(my_tasks, "   Learn Python   ")
    >>> my_tasks
    [('Learn Python', False)]

    >>> my_tasks = []
    >>> add_task(my_tasks, "    ")
    Task addition cancelled.
    >>> my_tasks
    []
    """
    task = task.strip()
    if not task:
        print("Task addition cancelled.")
        return
    task_list.append((task, False))

def mark_task_completed(task_list, index):
    """
    Marks a task as completed in the task list if the index is valid.

    Parameters
    ----------
    task_list : list of tuple
        The list of tasks, where each task is represented as a tuple (task_description, is_completed).
    index : int
        The index of the task to be marked as completed.

    Returns
    -------
    None
        This function updates the task in-place and prints a message indicating completion or an error if the index is invalid.

    Examples
    --------
    >>> tasks_test1 = [("Task 1", False), ("Task 2", False)]
    >>> mark_task_completed(tasks_test1, 0)
    task Task 1 completed
    >>> tasks_test1
    [('Task 1', True), ('Task 2', False)]

    >>> tasks_test2 = [("Task A", False), ("Task B", False)]
    >>> mark_task_completed(tasks_test2, 1)
    task Task B completed
    >>> tasks_test2
    [('Task A', False), ('Task B', True)]

    >>> tasks_test3 = [("Task X", True), ("Task Y", False)]
    >>> mark_task_completed(tasks_test3, 5)
    Invalid task index.
    >>> tasks_test3
    [('Task X', True), ('Task Y', False)]
    """
    #pdb.set_trace()
    if index >= 0 and index < len(task_list):
        task_description = task_list[index][0]
        task_list[index] = (task_description, True)
        print(f'task {task_description} completed')
    else:
        print("Invalid task index.")

def delete_task(task_list, index):
    """
    Delete a task from the task list at the specified index.

    Parameters
    ----------
    task_list : list of tuple
        The list containing tasks as (description, completed) tuples.
    index : int
        The position of the task to be deleted.

    Returns
    -------
    None
        This function modifies the task list in-place and prints the deleted task description.
    Examples
    --------
    >>> tasks_original = [("Study", False), ("Exercise", False), ("Read", False)]
    >>> tasks_copy = tasks_original.copy()
    >>> delete_task(tasks_copy, 1)
    Task "Exercise" deleted.
    >>> tasks_copy
    [('Study', False), ('Read', False)]
    >>> tasks_original
    [('Study', False), ('Exercise', False), ('Read', False)]

    >>> delete_task(tasks_copy, 5)
    Invalid task index.
    >>> tasks_copy
    [('Study', False), ('Read', False)]
    """
    if index >= 0 and index < len(task_list):
        removed_task = task_list.pop(index)
        print(f'Task "{removed_task[0]}" deleted.')
    else:
        print("Invalid task index.")

def list_tasks(task_list):
    """
    Displays all tasks in the task list with their completion status.

    Parameters
    ----------
    task_list : list of tuple
        A list of tasks, where each task is a tuple (description: str, completed: bool).
        The description is the task name, and completed indicates if the task is done.

    Returns
    -------
    None
        This function only prints the list of tasks to the console.
    """
    # pdb.set_trace()
    if not task_list:
        print("No tasks available.")
        return

    for index, task in enumerate(task_list):
        print(f"{index}. {'[X]' if task[1] else '[ ]'} {task[0]}")

def sort_tasks(task_list):
    """
    Sorts the task list alphabetically by task description.

    Parameters
    ----------
    task_list : list of tuple
        A list of tasks, where each task is a tuple (description: str, completed: bool).

    Returns
    -------
    None
        The original list is sorted in place. The sorted list is printed to the console.
    Examples
    --------
    >>> tasks_original = [("Walk dog", False), ("Do homework", True), ("Clean room", False)]
    >>> tasks_test = tasks_original.copy()
    >>> sort_tasks(tasks_test)
    [('Clean room', False), ('Do homework', True), ('Walk dog', False)]
    >>> tasks_test
    [('Clean room', False), ('Do homework', True), ('Walk dog', False)]
    >>> tasks_original
    [('Walk dog', False), ('Do homework', True), ('Clean room', False)]

    >>> empty_test = []
    >>> sort_tasks(empty_test)
    []
    """
    # pdb.set_trace()
    task_list.sort(key=lambda x: x[0])
    print(task_list)

def binary_search(task_list, task_to_find):
    """
    Perform a binary search to find the index of a task in the sorted list.

    Parameters
    ----------
    task_list : list of tuple
        List of tasks (tuples), where each tuple contains the task description and a completion flag.
    task_to_find : str
        The task description to search for.

    Returns
    -------
    str
        A message indicating the index of the found task, or that it was not found.
    Examples
    --------
    >>> tasks_test5 = [("Walk dog", False), ("Do homework", True), ("Clean room", False)]
    >>> tasks_test6 = tasks_test5.copy()
    >>> binary_search(tasks_test6, "Do homework")
    "Task 'Do homework' found at index 1."

    >>> tasks_test7 = tasks_test5.copy()
    >>> binary_search(tasks_test7, "Clean room")
    "Task 'Clean room' found at index 2."

    >>> tasks_test8 = tasks_test5.copy()
    >>> binary_search(tasks_test8, "Cook dinner")
    "Task 'Cook dinner' not found."
    """
    sorted_list = sorted(task_list, key=lambda x: x[0])
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid][0] == task_to_find:
            task_position = task_list.index(sorted_list[mid])
            return f"Task '{task_to_find}' found at index {task_position}."
        elif sorted_list[mid][0] < task_to_find:
            low = mid + 1
        else:
            high = mid - 1

    return f"Task '{task_to_find}' not found."

def main():
    """
        Entry point of the task management application.

        This function displays a menu to the user, handles input,
        and calls the appropriate functions to add, delete, list,
        complete, or sort tasks in a task list.

        Returns
        -------
        None
        """
    # pdb.set_trace()
    task_list = []

    while True:
        print("\n1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. List Tasks")
        print("5. Sort Tasks")
        print("6. Search Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task description: ")
            add_task(task_list, task)
        elif choice == "2":
            pdb.set_trace()
            index = int(input("Enter task index to mark as completed: "))
            mark_task_completed(task_list, index)
        elif choice == "3":
            index = int(input("Enter task index to delete: "))
            delete_task(task_list, index)
        elif choice == "4":
            list_tasks(task_list)
        elif choice == "5":
            sort_tasks(task_list)
        elif choice == "6":
            target = input("Enter task description to search: ")
            result = binary_search(task_list, target)
            print(result)
        elif choice == "7":
            sys.exit("Exiting program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()
