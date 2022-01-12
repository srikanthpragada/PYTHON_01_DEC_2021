import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details of countries!")
    exit(1)

countries = resp.json()  # Convert json to dict

for c in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    print(f"{c['name']['common']:50} {c['population']:10} {c['area']:10}")
