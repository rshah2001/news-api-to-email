import requests
from emailme import send_email
api_key = "545de4557d19470a9038997fae78e5b0"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-06-08&" \
      "sortBy=publishedAt&" \
      "apiKey=545de4557d19470a9038997fae78e5b0"

# make request
requests = requests.get(url)

# getting a dictionary using Json
content = requests.json()

body = ""

# Acess the article titles and description
for article in (content['articles']):
    if article["author"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(user_message=body)

