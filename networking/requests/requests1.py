import requests

def get_sorted_authors():
    #response = requests.get("http://192.168.1.12:5000/api/v2/resources/books?author=JK Rowling")
    response = requests.get("http://192.168.1.12:5000/api/v2/resources/books/all")

    #print(response.text)

    authors = []
    data = response.json()
    for entry in data:
        authors.append(entry["author"])

    sorted_authors = sorted(authors)
    print(sorted_authors)

#get_sorted_authors()

def post_author():
    data = {"author" : "Judith Kerr",
            "title" : "The Tiger Who Came To Tea",
            "first_sentence" : "Once there was a little girl called Sophie, and she was having tea with her mummy in the kitchen.",
            "publish" : "1968"}
    requests.post("http://192.168.1.12:5000/api/v2/resources/books", json=data)

post_author()

response = requests.get("http://192.168.1.12:5000/api/v2/resources/books?author=Judith Kerr")
print(response.text)