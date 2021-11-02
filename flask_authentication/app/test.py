import requests

BASE = "http://127.0.0.1:5000"

data = [{'name': 'blackpink', 'views': 10000,'likes': 10},
    {'name': 'how to make rest api', 'views': 2000,'likes': 20},
    {'name': 'funny video', 'views': 3000,'likes': 30}]

for i in range(len(data)):
    response = requests.put(BASE + "/video/"+ str(i) , data[i])
    print(response.json())

input('enter')
response = requests.delete(BASE + "/video/0")
print(response.json())
input("enter")
response = requests.get(BASE + "/video/2")
print(response.json())
