# 👀 GitHub Stalker (CLI)

A tiny command-line tool that fetches a user’s **public GitHub activity** and prints a human-readable report.

It looks up `https://api.github.com/users/<username>/events` and summarizes things including pushes, stars, issues, comments, and pull requests.

---

## ✨ Features

- ✅ Summarizes **pushes** (counts commits per repository)
- ⭐ Detects when a repo is **starred** (`WatchEvent`)
- 🗑️ Notes **deletions** (`DeleteEvent`) as “Deleted the <repo> repo”
- 🐞 Tracks **issues** (`opened`, `edited`, `closed`)
- 💬 Tracks **issue comments** (`created`, `edited`, `deleted`)
- 🔃 Tracks **pull requests** (`opened`, `edited`, `closed`)
- 🧾 Prints a readable, line-by-line **activity report**

> ℹ️ Only **public events** are available from this endpoint. Private activity is not included.

---

## 📦 Requirements

- Python 3.8+
- `requests` library

Install deps:
```bash
pip install requests
```
---

## 🚀 Installation & Usage  

Clone the repo:  
```bash
git clone https://github.com/ruthikaxo/Backend-Projects-Roadmap-SH.git
cd Github-Stalker
pip install -e .
```

Run the app with Python:  
```bash
github-stalker <username>
```

---

## 🔧 Commands  


### 📖 Get Help 
```-h
github-stalker -h
```

## 🎥 Demo  
Here’s an example of how it looks in action:  

```bash
$ github-stalker mattt


Here's what Mattt has been up to
Deleted the huggingface/swift-transformers repo.
Closed the pull request titled 'Update lint CI job to checkout PR merge ref' in the 'huggingface/swift-transformers repo.
Commented 'CI continues to use the workflow file in `main` which checks out `HEAD` of `main`, so there's no way to get lint job to pass. We'll just have to YOLO merge and hope for the best 🤞 ' on the 'Update lint CI job to checkout PR merge ref' issue in the huggingface/swift-transformers repo.
Starred the ManimCommunity/manim repo.

```

## 📜 License  
MIT License — free to use, modify, and share.  

## 📎 Roadmap Project Link
Roadmap.sh - https://roadmap.sh/projects/github-user-activity