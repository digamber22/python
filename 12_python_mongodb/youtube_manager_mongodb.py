from pymongo import MongoClient
from bson import ObjectId

client = MongoClient(
    "mongodb+srv://<project_name>:<password>@cluster0.cvldund.mongodb.net/"
)  # put project_name and password from mongodb_atlas. 

print(client)

db = client["ytmanager"]
video_collection = db["videos"]


def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})


def list_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )


def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})      


def main():
    while True:
        print("\n Youtube manager App")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updated video name: ")
            time = input("Enter the updated video time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)   

        elif choice == '5':
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()


''' 
same code as above only modified somethings  

from pymongo import MongoClient
from bson import ObjectId

# -------------------------
# MongoDB Connection
# -------------------------

client = MongoClient(
    "mongodb+srv://youtubepy:youtubepy@cluster0.cvldund.mongodb.net/"
)

db = client["ytmanager"]
video_collection = db["videos"]


# -------------------------
# CRUD Functions
# -------------------------

def add_video(name, time):
    video_collection.insert_one({
        "name": name,
        "time": time
    })
    print("✅ Video added successfully")


def list_videos():
    print("\n📺 All Videos:\n")

    for video in video_collection.find():
        print(
            f"ID: {video['_id']} | "
            f"Name: {video['name']} | "
            f"Time: {video['time']}"
        )


def update_video(video_id, new_name, new_time):
    try:
        result = video_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$set": {"name": new_name, "time": new_time}}
        )

        if result.modified_count:
            print("✅ Updated successfully")
        else:
            print("❌ Video not found")

    except:
        print("❌ Invalid ID format")


def delete_video(video_id):
    try:
        result = video_collection.delete_one(
            {"_id": ObjectId(video_id)}
        )

        if result.deleted_count:
            print("✅ Deleted successfully")
        else:
            print("❌ Video not found")

    except:
        print("❌ Invalid ID format")


# -------------------------
# Menu App
# -------------------------

def main():
    while True:
        print("\n========== Youtube Manager ==========")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            list_videos()

        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)

        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter new name: ")
            time = input("Enter new time: ")
            update_video(video_id, name, time)

        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)

        elif choice == '5':
            print("👋 Exiting...")
            break

        else:
            print("❌ Invalid choice")


# -------------------------
# Run
# -------------------------

if __name__ == "__main__":
    main()

'''


'''  Notes :- 
🔹 Connection
MongoClient()


→ Connects Python to MongoDB Atlas

🔹 Database
db = client["ytmanager"]


→ Selects database
→ Auto-created if not exists

🔹 Collection
video_collection = db["videos"]


→ Like SQL table
→ Stores documents (JSON)

🔥 CRUD Operations
🟢 Create
insert_one()


→ Add new video

🔵 Read
find()


→ Get all videos

🟡 Update
update_one({"$set": ...})


→ Modify specific fields
→ $set is important

🔴 Delete
delete_one()


→ Remove video

🔹 ObjectId
ObjectId(video_id)


→ Required because _id is not string

🔹 Menu System
while True


→ CLI loop
→ User selects operations

🔹 Entry Point
if __name__ == "__main__":


→ Runs file directly only
→ Best practice


🔹 Flow of Program
Connect DB
   ↓
Show menu
   ↓
User input
   ↓
CRUD function
   ↓
Repeat

'''