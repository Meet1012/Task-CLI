import sys
from datetime import datetime
import time
import json

json_file = open("tasks.json", "r+")
try:
    tasks = json.load(json_file)
except json.JSONDecodeError:
    tasks = []

def add(task, Status="To-Do"):
    print("[+] Adding Task [+]")

    if len(tasks) == 0:
        last_Sr = 0
    else:
        last_Sr = tasks[-1]["Sr"]
    new_task = {"Sr": last_Sr + 1, "Task": task, "Status": Status,
                "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "updatedAt": None}
    tasks.append(new_task)
    json_file.seek(0)
    json.dump(tasks, json_file)
    json_file.truncate()
    print("-"*100)
    time.sleep(1)
    print("[+] Added Task [+]")


def delete(sr_no):
    for i in tasks:
        if i["Sr"] == sr_no:
            tasks.remove(i)
            time.sleep(1)
            print("[+] Deleted Task [+]")
            break
    else:
        print("[-] No such Task [-]")
    for j in range(sr_no - 1, len(tasks)):
        tasks[j]["Sr"] -= 1
    json_file.seek(0)
    json.dump(tasks, json_file)
    json_file.truncate()


def update(sr, updatetask):
    for i in tasks:
        if i["Sr"] == sr:
            i["Task"] = updatetask
            i["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            time.sleep(1)
            print("[+] Updated Task [+]")
            break
    else:
        print("[-] No Such Task [-]")
    json_file.seek(0)
    json.dump(tasks, json_file)
    json_file.truncate()


def markinprogress(sr):
    for i in tasks:
        if i["Sr"] == sr:
            i["Status"] = "In Progress"
            time.sleep(1)
            print("[+] Status Updated [+]")
            break
    else:
        print("[-] No Such Task [-]")
    json_file.seek(0)
    json.dump(tasks, json_file)
    json_file.truncate()


def markdone(sr):
    for i in tasks:
        if i["Sr"] == sr:
            i["Status"] = "Done"
            time.sleep(1)
            print("[+] Status Updated [+]")
            break
    else:
        print("[-] No Such Task [-]")
    json_file.seek(0)
    json.dump(tasks, json_file)
    json_file.truncate()


def display(stat):
    if stat == None:
        for i in tasks:
            string = json.dumps(i, indent=3)
            print(string)
    elif stat == "done":
        for i in tasks:
            if i["Status"] == "Done":
                string = json.dumps(i, indent=3)
                print(string)
    elif stat == "not_done":
        for i in tasks:
            if i["Status"] == "To-Do":
                string = json.dumps(i, indent=3)
                print(string)
    elif stat == "in-progress":
        for i in tasks:
            if i["Status"] == "In Progress":
                string = json.dumps(i, indent=3)
                print(string)


if __name__ == "__main__":
    func = sys.argv[1]
    if func == "add":
        val = sys.argv[2]
        add(val)
    elif func == "delete":
        val = int(sys.argv[2])
        delete(val)
    elif func == "update":
        sr = int(sys.argv[2])
        updatetask = sys.argv[3]
        update(sr, updatetask)
    elif func == "mark-in-progress":
        sr = int(sys.argv[2])
        markinprogress(sr)
    elif func == "mark-done":
        sr = int(sys.argv[2])
        markdone(sr)
    elif func == "list" and len(sys.argv) > 2:
        val = sys.argv[2]
        if val == "done":
            display("done")
        elif val == "in-progress":
            display("in-progress")
        elif val == "todo":
            display("not_done")
    elif func == "list":
        display(None)
