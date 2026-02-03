import requests
import json

API_URL = "https://randomuser.me/api/"

def fetch_api_data():
    try:
        response = requests.get(API_URL)

        if response.status_code == 200:
            data = response.json()

            user = data["results"][0]
            name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}"
            email = user["email"]
            country = user["location"]["country"]

            print("User Details:")
            print("Name:", name)
            print("Email:", email)
            print("Country:", country)

            with open("api_response.json", "w") as file:
                json.dump(data, file, indent=4)

            print("\nJSON file saved successfully")

        else:
            print("Error! Status Code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("API Error:", e)

fetch_api_data()
