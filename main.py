import requests
from emailme import send_email

topic = "tesla"
api_key = "545de4557d19470a9038997fae78e5b0"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=545de4557d19470a9038997fae78e5b0&" \
      "language=en"

# make request
requests = requests.get(url)

# getting a dictionary using Json
content = requests.json()

body = ""
# Access the article titles and description
for article in content['articles'][:20]:
    if article["author"] is not None:
        body = "Subject: Today's News" \
               + "\n" + body + article["title"] + "\n" + \
               article["description"] + '\n' +\
               article['url'] + 2*"\n"

body = body.encode("utf-8")
send_email(user_message=body)
