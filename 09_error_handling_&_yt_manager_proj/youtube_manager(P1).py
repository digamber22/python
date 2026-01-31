
import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print(type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name")
        time = input("Enter the new video time")
        videos[index-1] = {'name':name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid video index selected")


def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
        # print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ ==  "__main__":
    main() 


'''
1.# JSON Handling (json module) :- 
Used to store data permanently in a file so it persists after the program closes.

 # json.dump(data, file) :-

Purpose: Writes Python data (like a list or dictionary) into a file.
How to remember: You are "dumping" data into the storage.
Used in code: save_data_helper function to update the youtube.txt file.

 # json.load(file) :-

Purpose: Reads the file and converts the JSON data back into a Python object.
Used in code: load_data function to retrieve previous videos.

2.# enumerate()  :-

Used in loops when you need both the item and its position (index).
Syntax: enumerate(iterable, start=0)
Why used here: To list videos with numbers like 1. Video Name, 2. Video Name.
Key Parameter: start=1 was used so the list starts counting from 1 instead of the default 0 (which is how Python counts internally).

# Returns: (1, video_object), (2, video_object)...
for index, video in enumerate(videos, start=1):

3. # with Statement vs. try-except

| Feature                    | `with` (Context Manager)                          | `try-except` (Error Handling)                 |
| -------------------------- | ------------------------------------------------- | --------------------------------------------- |
| **Primary Job**            | Resource management                               | Crash prevention                              |
| **Purpose**                | Open/close resources safely                       | Handle runtime errors                         |
| **Main Focus**             | Files, DB, sockets, connections                   | Exceptions like FileNotFoundError, ValueError |
| **Action**                 | Automatically closes file after block             | Catches errors and runs fallback code         |
| **Prevents Memory Leak**   | ✅ Yes                                            | ❌ No                                        |
| **Prevents Program Crash** | ❌ No                                             | ✅ Yes                                       |
| **Code Length**            | Short & clean                                     | Slightly longer                               |
| **Pythonic?**              | ✅ Recommended                                    | ✅ Required for risky code                   |
| **When to Use**            | Saving/writing files                              | Reading files that may not exist              |
| **In Your Code**           | `save_data_helper` → ensures file closes properly | `load_data` → returns `[]` if file missing    |


4. #  Entry Point: if __name__ == "__main__":

This is a standard boilerplate code in Python scripts.

Purpose: It checks if the script is being run directly (e.g., clicking the file or running python youtube.py).

Behavior:
If run directly: The main() function executes.
If imported (e.g., import youtube_manager in another file): The main() function will not run automatically.

Why use it? It makes your code modular and prevents unwanted code execution when reusing functions in other projects.