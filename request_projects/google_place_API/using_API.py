import requests

api_key = "AIzaSyCFF3MgmVjgeFyrh7aHGFnAE8MJnAIK-WI"
place_name = "Pacific Catch San Francisco"

# Step 1: Get Place ID
search_url = f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
params = {
    "input": place_name,
    "inputtype": "textquery",
    "fields": "place_id",
    "key": api_key
}

res = requests.get(search_url, params=params)
print(res.url)
res = requests.get(search_url, params=params).json()
print(res)
exit(0)
place_id = res["candidates"][0]["place_id"]

# Step 2: Get Full Details
details_url = f"https://maps.googleapis.com/maps/api/place/details/json"
params = {
    "place_id": place_id,
    "fields": "name,formatted_address,international_phone_number,website,opening_hours,rating,review,user_ratings_total,url,photos",
    "key": api_key
}

details = requests.get(details_url, params=params).json()
print(details["result"])
