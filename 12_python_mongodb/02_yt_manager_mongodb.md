# Python + MongoDB + pip + venv — Quick Study Notes

Clean beginner notes for:
- virtual environment
- pip
- MongoDB
- pymongo
- CRUD CLI project

============================================================

## 1️⃣ Virtual Environment (venv)

Purpose:
→ isolated Python environment per project
→ avoids package conflicts

Create
python -m venv venv

Activate
Windows:
.\venv\Scripts\activate

macOS / Linux:
source venv/bin/activate

Deactivate
deactivate

Rule:
Always install packages inside venv

------------------------------------------------------------

## 2️⃣ pip (Package Manager)

Purpose:
→ install external libraries from PyPI

Install package
pip install pymongo

Upgrade
pip install --upgrade pymongo

Remove
pip uninstall pymongo

Save packages
pip freeze > requirements.txt

Install all
pip install -r requirements.txt

Meaning:
pip = Pip Installs Packages

------------------------------------------------------------

## 3️⃣ MongoDB Basics

MongoDB = NoSQL database

Structure:

Client
  ↓
Database
  ↓
Collection
  ↓
Document (JSON)

Example document:
{
  "_id": ObjectId(...),
  "name": "Python",
  "time": 10
}

Terms:
Database → like SQL DB
Collection → like table
Document → like row/record

------------------------------------------------------------

## 4️⃣ MongoDB Atlas

Cloud version of MongoDB

Why:
→ no local setup
→ online access
→ easy hosting

Steps:
1. Create cluster
2. Whitelist IP
3. Copy connection string
4. Use in MongoClient

------------------------------------------------------------

## 5️⃣ pymongo (Python Driver)

Connect Python → MongoDB

Import:
from pymongo import MongoClient

Connect:
client = MongoClient("mongodb+srv://...")

Select DB:
db = client["ytmanager"]

Select collection:
collection = db["videos"]

------------------------------------------------------------

## 6️⃣ CRUD Operations

C → Create
collection.insert_one({...})

R → Read
collection.find()

U → Update
collection.update_one({"$set": {...}})

D → Delete
collection.delete_one({...})

------------------------------------------------------------

## 7️⃣ ObjectId (Important)

MongoDB _id is NOT string

Wrong:
"_id": "123"

Correct:
"_id": ObjectId("123")

Import:
from bson import ObjectId

------------------------------------------------------------

## 8️⃣ Your Project Flow

Start program
   ↓
Connect to MongoDB
   ↓
Select database
   ↓
Select collection
   ↓
Show menu
   ↓
User selects CRUD
   ↓
Perform operation
   ↓
Repeat

------------------------------------------------------------

## 9️⃣ Functions Used

add_video()     → insert
list_videos()   → read
update_video()  → update
delete_video()  → delete
main()          → menu loop

------------------------------------------------------------

## 🔟 CLI Menu Logic

while True:
   show menu
   take input
   call function

break → exit

------------------------------------------------------------

## 1️⃣1️⃣ Special Python Concept

if __name__ == "__main__":
    main()

Meaning:
→ run file directly only
→ best practice

------------------------------------------------------------

## 1️⃣2️⃣ Run Project

Install dependency
python -m pip install pymongo

Run
python youtube_manager_mongodb.py

------------------------------------------------------------

## 1️⃣3️⃣ Best Practices

✔ use venv
✔ use try/except
✔ convert types properly
✔ validate ObjectId
✔ use environment variables
✔ don't hardcode passwords
✔ use requirements.txt

------------------------------------------------------------

## 🔥 Quick Revision Sheet

venv → isolated env
pip → install packages
MongoClient → connect DB
DB → container
Collection → table
Document → record
insert_one → create
find → read
update_one → update
delete_one → delete
ObjectId → unique id

------------------------------------------------------------

## One Line Summary

Python CLI app using pymongo to perform CRUD operations on MongoDB Atlas inside a virtual environment.
