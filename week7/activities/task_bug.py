'''A buggy Task Manager that provides an opportunity to debug code by both reasoning about it and stepping through using pdb.

The program has a number of bugs that are introduced one at a time. 

The goal is to find and fix the bugs.

Ensure you step through this program in pdb only to understand how the program works and to find the bugs.'''

# Once debugged add some documentation examples to help the next programmer!
import sys
import pdb
# import os

def add_task(task_list, task):
    #pdb.set_trace()
    task_list.append((task, False))

def mark_task_completed(task_list, index):
    #pdb.set_trace()
    if index >= 0 and index < len(task_list):
        task_list[index] = (task_list[index][0], True)
    else:
        print("Invalid task index.")

def delete_task(task_list, index):
    # pdb.set_trace()
    if index >= 0 and index < len(task_list):
        task_list.remove(task_list[index])
    else:
        print("Invalid task index.")

def list_tasks(task_list):
    #pdb.set_trace()
    if not task_list:
        print("No tasks available.")
        return

    for index, task in enumerate(task_list):
        print(f"{index}. {'[X]' if task[1] else '[ ]'} {task[0]}")

def sort_tasks(task_list):
    #pdb.set_trace()
    task_list.sort(key=lambda x: x[0])
    print(task_list)

def binary_search(tasks, target):
    low, high = 0, len(tasks) - 1
    while low <= high:
        mid = (low + high) // 2
        if tasks[mid][0] == target:
            return mid
        elif tasks[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def main():
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
            index = binary_search(task_list, target)
            if index != -1:
                print(f"Task '{target}' found at index {index}.")
            else:
                print(f"Task '{target}' not found.")
        elif choice == "7":
            sys.exit("Exiting program.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
