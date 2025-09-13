import json

task = []

def show_menu():
    print("""
===== TO-DO LIST MENU =====
1. Add Task
2. View Task
3. Mark Task as Complete
4. Delete Task
5. Exit
""")

tasks = []  # 

def add_task():
    """Function to ask for the ask and add the task """
    task_name = input("Enter task name:")
    tasks.append({"name": task_name, "status": "pending",})     # Add the task name and pending status as defauult
    
