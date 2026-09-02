# \
import requests
api="https://fakestoreapi.com/products"
data=requests.get(api)
print(data.json())

import requests
res = requests.get("https://fakestoreapi.com/products")
res=res.json()
for post in res:
    print(post.get("id"))


res= requests.get("https://jsonplaceholder.typicode.com/posts")
print(res)

send_data ={

}
api = "http://localhost:3000/mobiles/WFf4fH46AHM"

res=requests.get(api,)
print(res.json()) 


import json #json module
send_data={
    "user_id":12,
    "Id":102,
    "title":"New post",
    "body":"This is a new post"
}    
res=requests.post(api,send_data)
print(res)
print(res.json())


import json
send_data={
    "id":1,
    "name":"Samsung S25",
    "ram":"12gb",
    "processor":"Snapdragon"
}
json_data=json.dumps(send_data)  #dumps method converts the python object into json code
res=requests.post(api,data=json_data)
print(res)
print(res.json())


import json
new_mobile={
    "id":3,
    "name":"vivo 300x",
    "ram":"12",
    "processor":"sdgen8 elite"
}
# json_data=json.dumps(new_mobile) 

res = requests.post(api,json=new_mobile)  #json keyword converts data automatically
print(res.json())

data = {"processor":"sdgen 7" ,"name":"vivo 200","ram":"6gb"}

res = requests.patch(api,json=data)
print(res.json())

data = {"ram":"6gb"}
res = requests.put(api,json=data)
print(res.json()) #{'error': 'Not Found'} - we didn't provide id

api = "http://localhost:3000/mobiles/MIkrrY2aJ9M"
res=requests.delete(api)
print(res.json())

res=requests.post(api)
print(res.json())

res=requests.get(api+"/hello")
print(res.json())


import requests

api="http://127.0.0.1:8000/redoc"

res = requests.get(api+"/")
print(res.json())

res = requests.get(api+"/employee")
print(res.json())


res = requests.put(api+"/employee")
print(res.json())

res = requests.post(api+"/employee")
print(res.json())


res = requests.patch(api+"/employee")
print(res.json())


res = requests.delete(api+"/employee")
print(res.json())