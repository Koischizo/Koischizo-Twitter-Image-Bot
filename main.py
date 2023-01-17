import tweepy
import json


# Authentication keys
# Open JSON file
try:
    with open("config.json", "r") as json_file:
        data = json.load(json_file)
except:
    print("Unable to open JSON file.")
    exit()
consumer_key = data["keys"][0]["consumer_key"]
consumer_secret = data["keys"][0]["consumer_secret"]
access_token = data["keys"][0]["access_token"]
access_token_secret = data["keys"][0]["access_token_secret"]

# Authenticate with the Twitter API using the keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


cur = data["count"]
media_id = api.media_upload(f"./images/{cur}.png").media_id
with open(f"./status/{cur}.txt", "r") as txt_file:
    status = txt_file.read()

data["count"] = cur + 1
try:
    with open("config.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("JSON file updated successfully.")
except:
    print("Unable to write to JSON file.")

api.update_status(status, media_ids=[media_id])
print("Tweet posted successfully!")
