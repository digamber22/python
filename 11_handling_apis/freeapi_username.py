import requests

def fectch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country = fectch_random_user_freeapi()
        print(f"Username: {username} \nCountry: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()



''' 
    Notes :-  HW to make it strong , practice more and other methods like put , post ... etc . 

    1. The requests Library

    External Module: Unlike json or sqlite3, this is not built-in to Python. You must install it first using: pip install requests
    requests.get(url): This sends a GET request to the specified URL (like opening a webpage in code) and returns a Response object containing the server's reply.

    2. Handling JSON Responses
    response.json():

    APIs usually send data as a JSON string.
    This method parses that string and converts it directly into a Python dictionary (or list), making it easy to access keys like data['data'].

    3. Working with Nested Data

    The Structure: APIs often nest data deep inside objects to keep it organized.
    Your Code: user_data["login"]["username"]
    Visual: data (dict) -> login (dict) -> username (string).
    Note: You must know the exact structure of the API response (usually found in documentation) to extract data correctly.

    4. Custom Error Handling (raise)
    raise Exception(...):

    Instead of just printing "Error," your function raises an exception.
    Why? This stops the function immediately and passes the error back to the caller (main()). This allows the main function to decide how to handle the error (e.g., print it, log it, or retry).

    5. Logical Success Checks
    if data["success"]...:

    Just because a request returns (HTTP 200 OK), doesn't mean the database query was successful.
    Good APIs include a success flag (True/False) in their JSON. Always check this logical flag before trying to access the actual data to avoid KeyError.

    6. Unpacking Return Values
    username, country = fetch_...:

    Your function returns a tuple (username, country).
    Python allows you to "unpack" these directly into two separate variables in one line.
'''