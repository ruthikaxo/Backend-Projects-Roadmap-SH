# 📝 Task Tracker CLI  

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-success)](#)  
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)](#)  

A lightweight, command-line task management app built with Python.  
It lets you create, update, delete, and track tasks across multiple trackers, with progress statuses and pretty table outputs.  

---

## ✨ Features  
- Create **trackers** (separate JSON files for each project).  
- **Add** tasks with auto-incremented IDs.  
- **Update** task descriptions.  
- **Delete** tasks (reindexes IDs after removal).  
- Mark tasks as:  
  - `not-started` (default)  
  - `in-progress`  
  - `done`  
- **List** tasks in pretty table format with optional status filters.  
- Stores data as human-readable JSON in a `Task-Cabinet/` directory.  

---

## 📦 Requirements  
- Python **3.9+**  
- Install dependencies:  
  ```bash
  pip install tabulate
  ```

---

## 🚀 Installation & Usage  

Clone the repo:  
```bash
git clone https://github.com/ruthikaxo/Backend-Projects-Roadmap-SH.git
cd task-tracker
```

Run the app with Python:  
```bash
python task-tracker.py <command> [arguments]
```

---

## 🔧 Commands  


### 📖 Get Help 
```-h
python task-tracker.py -h
```

### ▶️ Add a Task  
```bash
python task-tracker.py add <tracker_name> "<task_name>"
```

### 📋 List Tasks  
```bash
python task-tracker.py list <tracker_name> [status]
```
- `status` can be `todo`, `in-progress`, or `done`.  

### ✏️ Update a Task  
```bash
python task-tracker.py update <tracker_name> <task_id> "<new_task_name>"
```

### ✅ Mark as Done  
```bash
python task-tracker.py mark-done <tracker_name> <task_id>
```

### ⏳ Mark as In-Progress  
```bash
python task-tracker.py mark-in-progress <tracker_name> <task_id>
```

### ❌ Delete a Task  
```bash
python task-tracker.py delete <tracker_name> <task_id>
```

---

## 📂 Data Storage  
Tasks are stored as JSON inside `Task-Cabinet/<tracker_name>.json`:  

```json
[
  {
    "id": 1,
    "desc": "Finish math homework",
    "status": "in-progress",
    "createdAt": "2025-09-28T14:35:00",
    "updatedAt": "2025-09-28T15:10:00"
  },
  {
    "id": 2,
    "desc": "Clean room",
    "status": "done",
    "createdAt": "2025-09-28T14:40:00",
    "updatedAt": "2025-09-28T15:12:00"
  }
]
```

---

## 🎥 Demo  
Here’s an example of how it looks in action:  

```bash
$ python task-tracker.py add School-Tracker "Finish math homework"
$ python task-tracker.py add School-Tracker "Clean room"
$ python task-tracker.py list School-Tracker

╒════╤═══════════════════╤═══════════════╤════════════════════╤════════════════════╕
│ ID │ Task Title        │ Progress      │ Created At         │ Updated At         │
╞════╪═══════════════════╪═══════════════╪════════════════════╪════════════════════╡
│  1 │ Finish math hw    │ not-started   │ 2025-09-28 14:35   │ 2025-09-28 14:35   │
├────┼───────────────────┼───────────────┼────────────────────┼────────────────────┤
│  2 │ Clean room        │ not-started   │ 2025-09-28 14:40   │ 2025-09-28 14:40   │
╘════╧═══════════════════╧═══════════════╧════════════════════╧════════════════════╛
```

## 📜 License  
MIT License — free to use, modify, and share.  
