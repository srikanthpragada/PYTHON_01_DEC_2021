import requests

user = "srikanthpragada"

resp = requests.get(f"https://api.github.com/users/{user}")
if resp.status_code != 200:
    print("Sorry! Could not get details of user!")
    exit(1)

details = resp.json() # Convert json to dict

print("Name         :", details["name"])
print("Company      :", details["company"])
print("Repos Count  :", details["public_repos"])
print("No. followers:", details["followers"])