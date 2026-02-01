# Python + MongoDB (pymongo) — Beginner Notes

## What is this project?
A simple CLI (terminal) app that:
- connects Python to MongoDB
- stores video data
- performs CRUD operations

CRUD = Create, Read, Update, Delete

---

# Overall Flow

Start program
   ↓
Connect to MongoDB
   ↓
Select DB → Collection
   ↓
Show menu
   ↓
User selects operation
   ↓
Perform CRUD
   ↓
Repeat until Exit

---

# Core Concepts Used

## 1. MongoClient (Connection)
Used to connect Python to MongoDB server.

Code:
from pymongo import MongoClient
client = MongoClient("mongodb+srv://...")

Meaning:
→ establishes database connection

Without this → nothing works

---

## 2. Database Selection

db = client["ytmanager"]

Meaning:
→ selects database
→ created automatically if not present

Like SQL database

---

## 3. Collection Selection

video_collection = db["videos"]

Meaning:
→ like SQL table
→ stores documents (JSON data)

Example document:
{
  "_id": ObjectId(...),
  "name": "Python Basics",
  "time": 10
}

---

# CRUD Operations

## Create (Insert)
video_collection.insert_one({...})

Purpose:
→ add new document

Adds automatically:
→ _id (unique id)

---

## Read (Find)
video_collection.find()

Purpose:
→ get all documents

Returns:
→ cursor (iterator)

Used with:
for loop

---

## Update
video_collection.update_one(
   {"_id": ObjectId(id)},
   {"$set": {...}}
)

Purpose:
→ update specific fields

Important:
$set → modifies only given fields
Without $set → replaces whole document

---

## Delete
video_collection.delete_one({"_id": ObjectId(id)})

Purpose:
→ removes document permanently

---

# ObjectId (Important)

MongoDB _id is NOT string.

Wrong:
"_id": "123"

Correct:
"_id": ObjectId("123")

So always convert:
ObjectId(video_id)

---

# Functions in Code

add_video()     → insert
list_videos()   → read
update_video()  → update
delete_video()  → delete
main()          → menu control

---

# CLI Menu Logic

while True:
   show menu
   take input
   call function
   repeat

Break when user chooses Exit

---

# Special Python Concept

if __name__ == "__main__":
    main()

Meaning:
→ run only when file executed directly
→ not when imported

Best practice

---

# Best Practices

✔ use virtual environment  
✔ convert time to int  
✔ use try/except  
✔ validate ObjectId  
✔ never hardcode password  
✔ use environment variables  

---

# Commands to Run

Install:
python -m pip install pymongo

Run:
python youtube_manager_mongodb.py

---

# Quick Revision (1 line each)

MongoClient → connect DB  
Database → container  
Collection → table  
Document → record  
insert_one → create  
find → read  
update_one → update  
delete_one → delete  
ObjectId → id type  

---

# One Line Summary

Python CLI app that performs CRUD operations on MongoDB using pymongo.
