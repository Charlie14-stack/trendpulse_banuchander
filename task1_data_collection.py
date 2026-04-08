import requests
import json

# This function helps me grab the post data from the website
def fetch_data():
    # Setting up the link
    api_link = "http://jsonplaceholder.typicode.com/posts"
    
    print("Starting the download...")

    try:
        # Actually calling the website
        response = requests.get(api_link)

        # 200 means everything went okay
        if response.status_code == 200:
            # Turn the raw response into a Python list
            post_data = response.json()
            
            # Now I need to save it to a file so I can use it later
            filename = 'raw_trending_data.json'
            
            with open(filename, 'w') as my_file:
                # indent=4 makes it look pretty and readable
                json.dump(post_data, my_file, indent=4)
            
            print("Finished! Everything is saved in raw_trending_data.json")
            
        else:
            # If the website is down or the link is wrong
            print("Something went wrong. Status code:", response.status_code)

    except Exception as error:
        # This catches things like no internet connection
        print("I ran into an error:", error)

# This part makes sure the function runs when I click 'Play'
if __name__ == "__main__":
    fetch_data()