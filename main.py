"""
tohidi
""" 
question = input("Enter your question.")

import requests

url = "https://api.t.parsaqa.com/api/user/question/search"

params = {"type":"semantic",
        "query": question,
        "page_size": 1,
        "page": 1,
        "is_send_answer": False
}

answer = requests.get(url, params=params)

#print(answer)

data = answer.json()
#print(data)

first_result = data["data"]["result"][0]

#print(first_result["highlight"])

text = first_result["highlight"]
parts =text.split("answer:")

print (parts[1])