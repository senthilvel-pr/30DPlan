import requests

def fetch_food_product_data():
    # URL simulating a Product Database API
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    print(f"🌐 Connecting to API: {url}...")
    
    try:
        # 1. Sending the GET request
        response = requests.get(url, timeout=10)
        
        # 2. Checking the Status Code
        # 200 = Success, 404 = Not Found, 500 = Server Error
        if response.status_code == 200:
            print("✅ Connection Successful!")
            
            # 3. Parsing JSON data into a Python Dictionary
            data = response.json()
            
            print("\n--- Received Product Data ---")
            print(f"Product ID: {data['id']}")
            print(f"Batch Name: {data['title'][:30]}...") # Showing first 30 chars
            print(f"Description: {data['body'][:50]}...")
            print("-----------------------------\n")
            
        else:
            print(f"❌ Server returned an error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Network Error: Please check your internet connection.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_food_product_data()