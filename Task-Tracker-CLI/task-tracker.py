#hello world


#Requirements
# The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:
# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done
# List all tasks that are not done
# List all tasks that are in progress

#find the tracker, and then update it if present, otherwise, create new one

# the json module helps us perform activities on files
import json
# path helps us find the path of a file
from pathlib import Path
# for cli arguments
import argparse
#for datetime
from datetime import datetime, date, timedelta
#for pretty tables
from tabulate import tabulate

#json.dump() helps you write python data into an external json file

# with.... open 
# -w for write
# -a for append
# -r for read

# Tracker format
# Tasks = {id1 = {desc: 'xx', status: 'yy', createdAt: datetime, updatedAt: datetime}}

# list tasks

def list_tks(tracker_name, task_status=None):
    # ask what tracker they want
    # check if tracker exists
    # if doesn't exist, return error message
    # otherwise, list contents

    print("I see you want to see what's left right in your", tracker_name, "tracker, right? \n")
    task_cabinet = Path("Task-Cabinet")
    task_cabinet.mkdir(parents=True, exist_ok=True) #if directory exists
    
    #checking if the tracker exists
    tracker = task_cabinet / f"{tracker_name}.json"

    if not tracker.exists():
        return("You've not created the "+tracker_name+" tracker yet babes")
    try:
        with tracker.open("r", encoding="utf-8") as current_tracker:
            tasks = json.load(current_tracker)
    except (json.JSONDecodeError, OSError):
        return("This tracker has been compromised sweets")        

    if not isinstance(tasks, list):
        return("This tracker has been damaged sweets")
    
        # print(tasks)
    task_c = len(tasks)
    
    status_map = {
        None: None,
        "todo": "not-started",
        "in-progress": "in-progress",
        "done": "done"
    }
    
    if task_status not in status_map:
        return("Wrong status request babes")
    
    task_items = [task for task in tasks if task_status == None or task["status"] == status_map[task_status]]
    # print(task_items)
    entries = []
    for task in task_items:
        entries.append({
            "ID": f"{task['id']}",
            "Task Title": task["desc"],
            "Status": task["status"],
            "Created At": task["createdAt"].replace("T", " "),
            "Updated At": task["updatedAt"].replace("T", " ")
        })

    if entries != []:
        print(tabulate(entries, headers="keys", tablefmt="fancy_grid"))
    else:
        print("No tasks are", task_status,"yet sweets.")       

def add_tks(tracker_name, task_name):
    # add a task to a tracker
    # if tracker doesn't exist, create it and add the new task, priority being the order it's currently at
    tracker_dir = Path("Task-Cabinet/") 
    
    tracker = tracker_dir
    tracker.mkdir(parents=True, exist_ok=True)
    tracker = tracker / f"{tracker_name}.json"
    now = datetime.now().isoformat(timespec="seconds")

    if not tracker.exists():
        print("no, ", tracker_name, "doesn't exist, creating tracker right away...")
        tasks = []
    else:
        print("yes,",tracker_name,"exists")
        try:
            with tracker.open("r", encoding="utf-8") as current_tracker:
                tasks = json.load(current_tracker)
                #normalize list
                if not isinstance(tasks, list):
                    tasks = []
        except (json.JSONDecodeError, OSError):
            tasks = []

    next_id = tasks[-1]["id"] + 1 if tasks else 1
        
    new_entry = {"id": next_id, 'desc' : task_name, 'status': 'not-started', 'createdAt': now, 'updatedAt': now}
    tasks.append(new_entry)

    with tracker.open("w+", encoding="utf-8") as current_tracker:
        # current_tracker.seek(0)
        json.dump(tasks, current_tracker, indent=2)
        current_tracker.truncate()
        # json.dump(latest_task, current_tracker, indent=2)
    
    return new_entry

def update_tks(tracker_name, task_id, new_task_name):
    tracker_dir = Path("Task-Cabinet/") 
    
    tracker = tracker_dir
    tracker.mkdir(parents=True, exist_ok=True)

    tracker = tracker / f"{tracker_name}.json"
    now = datetime.now().isoformat(timespec="seconds")

    if not tracker.exists():
        return("The", tracker_name, "doesn't exist babes")

    try:
        with tracker.open("r+", encoding="utf-8") as current_tracker:
            tasks = json.load(current_tracker)
            #normalize list
            if not isinstance(tasks, list):
                return("This tracker isn't properly formatted babes")
            
            tasks[int(task_id)-1]["desc"] = new_task_name
            tasks[int(task_id)-1]["updatedAt"] = now
            task_update = [{
                    "ID": tasks[int(task_id)-1]["id"],
                    "Task Title": tasks[int(task_id)-1]["desc"],
                    "Status": tasks[int(task_id)-1]["status"],
                    "Created At": tasks[int(task_id)-1]["createdAt"].replace("T", " "),
                    "Updated At": tasks[int(task_id)-1]["updatedAt"].replace("T", " ")
                }]
    
            current_tracker.seek(0)
            current_tracker.writelines(json.dumps(tasks, indent=2))
            current_tracker.truncate()

            print(tabulate(task_update, headers="keys", tablefmt="fancy_grid"))

    except (json.JSONDecodeError, OSError):
        return("This tracker has been compromised though")
    
def mark_done_tks(tracker_name, task_id):
    tracker_dir = Path("Task-Cabinet/") 
    
    tracker = tracker_dir
    tracker.mkdir(parents=True, exist_ok=True)

    tracker = tracker / f"{tracker_name}.json"
    now = datetime.now().isoformat(timespec="seconds")

    if not tracker.exists():
        return("The", tracker_name, "doesn't exist babes")

    try:
        with tracker.open("r+", encoding="utf-8") as current_tracker:
            tasks = json.load(current_tracker)
            #normalize list
            if not isinstance(tasks, list):
                return("This tracker isn't properly formatted babes")
            
            tasks[int(task_id)-1]["status"] = "done"
            tasks[int(task_id)-1]["updatedAt"] = now
            task_update = [{
                    "ID": tasks[int(task_id)-1]["id"],
                    "Task Title": tasks[int(task_id)-1]["desc"],
                    "Status": tasks[int(task_id)-1]["status"],
                    "Created At": tasks[int(task_id)-1]["createdAt"].replace("T", " "),
                    "Updated At": tasks[int(task_id)-1]["updatedAt"].replace("T", " ")
                }]
    
            current_tracker.seek(0)
            current_tracker.writelines(json.dumps(tasks, indent=2))
            current_tracker.truncate()

            print(tabulate(task_update, headers="keys", tablefmt="fancy_grid"))

    except (json.JSONDecodeError, OSError):
        return("This tracker has been compromised though")

def mark_ip_tks(tracker_name, task_id):
    tracker_dir = Path("Task-Cabinet/") 
    
    tracker = tracker_dir
    tracker.mkdir(parents=True, exist_ok=True)

    tracker = tracker / f"{tracker_name}.json"
    now = datetime.now().isoformat(timespec="seconds")

    if not tracker.exists():
        return("The", tracker_name, "doesn't exist babes")

    try:
        with tracker.open("r+", encoding="utf-8") as current_tracker:
            tasks = json.load(current_tracker)
            #normalize list
            if not isinstance(tasks, list):
                return("This tracker isn't properly formatted babes")
            
            tasks[int(task_id)-1]["status"] = "in-progress"
            tasks[int(task_id)-1]["updatedAt"] = now
            task_update = [{
                    "ID": tasks[int(task_id)-1]["id"],
                    "Task Title": tasks[int(task_id)-1]["desc"],
                    "Status": tasks[int(task_id)-1]["status"],
                    "Created At": tasks[int(task_id)-1]["createdAt"].replace("T", " "),
                    "Updated At": tasks[int(task_id)-1]["updatedAt"].replace("T", " ")
                }]
    
            current_tracker.seek(0)
            current_tracker.writelines(json.dumps(tasks, indent=2))
            current_tracker.truncate()

            print(tabulate(task_update, headers="keys", tablefmt="fancy_grid"))

    except (json.JSONDecodeError, OSError):
        return("This tracker has been compromised though")
       
def delete_tks(tracker_name, task_id=int):
    tracker_dir = Path("Task-Cabinet/") 
    
    tracker = tracker_dir
    tracker.mkdir(parents=True, exist_ok=True)

    tracker = tracker / f"{tracker_name}.json"

    if not tracker.exists():
        return("The", tracker_name, "doesn't exist babes")

    try:
        with tracker.open("r+", encoding="utf-8") as current_tracker:
            tasks = json.load(current_tracker)
            #normalize list
            if not isinstance(tasks, list):
                return("This tracker isn't properly formatted babes")
            
            tasks.pop(int(task_id)-1)

            updated_tasks = []
            
            for task in tasks:
                case_val = int(task["id"])
                if case_val > int(task_id):
                    task["id"] = case_val - 1
                    updated_tasks.append(task)
                elif case_val < int(task_id):
                    updated_tasks.append(task)

            current_tracker.seek(0)
            current_tracker.writelines(json.dumps(tasks, indent=2))
            current_tracker.truncate()    

            print(tabulate(updated_tasks, headers="keys", tablefmt="fancy_grid"))

    except (json.JSONDecodeError, OSError):
        return("This tracker has been compromised though")

def main():
    print("Hey, welcome to your task manager")
    print(r"""######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
#################################              .###-  #########   ####################################
###############################     ####             #########   #####################################
##############################   #######   ###. -#######   ##    #  ##################################
###############################  ######   ##        .#    ###        #################################
######################################    #   ##    #  #   #    ##   #################################
#####################################    #   -##   #  ##   #       ##  ###############################
####################################    ##                    #       ################################
####################################    ###    #    #     #   ##    ##################################
#########################           ##### ############################################################
######################                    #################   ########################################
######################   #####   #  +#####################    ############   #########################
######################   ####    #   +###.       ##     ##        ##     ##    #######################
############################-   #. #   #   ##   ##   #        #      ##  #     #######################
############################   ##     #    ##   #   ##  #   #    #      #  #   #  ####################
###########################   ##  +  #    #    #    ###      ###    ####  #   #  #####################
##########################    #  #                               #       #      ######################
###########################  ######  ###+.###+-####  #########.##### .###### #########################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################
######################################################################################################""")
    

    parser = argparse.ArgumentParser(description="Task Tracker Manager")
    subs = parser.add_subparsers(dest="command")

    list_tasks = subs.add_parser("list", help="This shows you information related to a particular tracker. Usage = list <tracker_name>.You can also list the tasks with certain statuses by adding the status after the tracker name, i.e. list <tracker_name> <status>, which can be 'not-started, 'in-progress', or 'done'")
    list_tasks.add_argument("tracker_name")
    list_tasks.add_argument("task_status", nargs="?")

    add_task = subs.add_parser("add", help="This adds a new task to a tracker of your choice. Usage = add <tracker_name> <task_name>")
    add_task.add_argument("tracker_name")
    add_task.add_argument("task_name")

    delete_task = subs.add_parser("delete", help="This deletes a task in a tracker of your choice by its unique id. Usage = delete <tracker_name> <task_id>")
    delete_task.add_argument("tracker_name")
    delete_task.add_argument("task_id")

    update_task = subs.add_parser("update", help="This updates a task's name. Usage = update <tracker_name> <task_id> <new_task_name>")
    update_task.add_argument("tracker_name")
    update_task.add_argument("task_id")
    update_task.add_argument("new_task_name")

    in_prg_task = subs.add_parser("mark-in-progress", help="This marks a task's status as in-progress. Usage = mark-done <tracker_name> <task_id>")
    in_prg_task.add_argument("tracker_name")
    in_prg_task.add_argument("task_id")

    cmpltd_task = subs.add_parser("mark-done", help="This marks a task's status as complete. Usage = mark-done <tracker_name> <task_id>")
    cmpltd_task.add_argument("tracker_name")
    cmpltd_task.add_argument("task_id")
    
    tracker_args = parser.parse_args()

    if tracker_args.command == "list":
        # if status isn't specified, just list all the tasks in the required tracker if it exists
        # else list all the tasks with that status
        list_tks(tracker_args.tracker_name, tracker_args.task_status)
    
    elif tracker_args.command == "add":
        add_tks(tracker_args.tracker_name, tracker_args.task_name)

    elif tracker_args.command == "update":
        update_tks(tracker_args.tracker_name, tracker_args.task_id, tracker_args.new_task_name)
    
    elif tracker_args.command == "mark-done":
        mark_done_tks(tracker_args.tracker_name, tracker_args.task_id)

    elif tracker_args.command == "mark-in-progress":
        mark_ip_tks(tracker_args.tracker_name, tracker_args.task_id)
    
    elif tracker_args.command == "delete":
        delete_tks(tracker_args.tracker_name, tracker_args.task_id)
    


        


if __name__ == "__main__":
    main()