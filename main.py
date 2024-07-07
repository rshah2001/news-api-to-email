import requests

api_key = "545de4557d19470a9038997fae78e5b0"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "from=2024-06-07&sortBy=publishedAt&" \
      "apiKey=545de4557d19470a9038997fae78e5b0"

# make request
requests = requests.get(url)

# getting a dictionary using Json
content = requests.json()

# Acess the article titles and description
for article in (content['articles']):
    print(article['title'])
    print(article['description'])
