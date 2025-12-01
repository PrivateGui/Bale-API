import requests

url = "https://bale-member-api.zonercm.workers.dev/tehranstudio"

try:
    response = requests.get(url)
    print("Status Code:", response.status_code)
    # Try to parse JSON (common for APIs)
    try:
        data = response.json()
        print("JSON response:", data)
    except ValueError:
        # not JSON — print raw text
        print("Response text:", response.text)
except requests.exceptions.RequestException as e:
    print("Request error:", e)
