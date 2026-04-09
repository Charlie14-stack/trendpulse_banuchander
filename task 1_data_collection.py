import requests
import json

# This function helps me grab the post data from the website
def fetch_data():
    # Setting up the link for the posts
    api_link = "http://jsonplaceholder.typicode.com/posts"
    
    print("Starting the download...")

    try:
        # Actually calling the website to get data
        response = requests.get(api_link)

        # 200 means the connection is successful
        if response.status_code == 200:
            # Turn the raw response into a Python list we can work with
            post_data = response.json()
            
            # Saving it as a JSON file so I have a backup for Task 2
            filename = 'raw_trending_data.json'
            
            with open(filename, 'w') as my_file:
                # Using indent=4 makes the file easy to read for humans
                json.dump(post_data, my_file, indent=4)
            
            print("Finished! Everything is saved in raw_trending_data.json")
            
        else:
            # Error handling if the website is down
            print("Something went wrong. Status code:", response.status_code)

    except Exception as error:
        # This catches things like no internet or timeout errors
        print("I ran into an error:", error)

# Running the function
if __name__ == "__main__":
    fetch_data()