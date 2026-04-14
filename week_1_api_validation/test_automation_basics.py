import requests
import pytest

# 1. Testing your Day 1 Food Logic
def test_food_safety_logic():
    temp = 3
    # An 'assert' checks if a condition is True. 
    # If False, the test fails automatically.
    assert temp <= 5, "Temperature is too high for cold chain!"

# 2. Testing your Day 2 API Connection
def test_api_status_code():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # This is a real world QA test case:
    # "Verify that the Product API returns a 200 Success code"
    assert response.status_code == 200
    
    # Verify the data structure
    data = response.json()
    assert "id" in data
    assert data["id"] == 1

# 3. A test that is designed to fail (Example of a bug found)
def test_intentional_failure():
    # Imagine we expect a product name to be 'Milk' but it is 'Bread'
    product_name = "Bread"
    # assert product_name == "Milk" # Uncomment this to see a failure!

def test_api_with_param(product_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{product_id}"
    response = requests.get(url)
    
    print(f"\nTesting Product ID: {product_id}")
    assert response.status_code == 200
    assert str(response.json()['id']) == str(product_id)