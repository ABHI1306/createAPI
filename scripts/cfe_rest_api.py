import os
import json
import requests

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
ENDPOINT = "http://127.0.0.1:8000/api/status/"
image_path = os.path.join(os.getcwd(),"OIP1.jpg")
headers = {
    'Content-Type':'application/json',
    #'Authorization': "JWT " + token,
}
data = {
    'username': 'abhijitshete13',
    'email': 'abhijitshete13@gmail.com',
    'password': 'abhijitshete13',
    'password2': 'abhijitshete13'
}

r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token = r.json()#['token']
print(token)

# refresh_data = {
#     'token': token
# }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = r.json()
# print(new_token)

# headers = {
#     #'Content-Type':'application/json',
#     'Authorization': "JWT " + token,
# }

# with open(image_path,'rb') as image:
#     file_data = {
#                 'image':image
#     }
#     data = {
#         "user": 1,
#         "content": "Updated latest content"
#     }
#     json_data = json.dumps(data)
#     posted_response = requests.put(ENDPOINT + str(11) + "/", data=data, headers=headers, files=file_data)
#     print(posted_response.text)

# headers = {
#     #'Content-Type':'application/json',
#     'Authorization': "JWT " + token,
# }

# data = {
#     "user": 1,
#     "content": "Updated latest content"
# }
# json_data = json.dumps(data)
# posted_response = requests.put(ENDPOINT + str(11) + "/", data=data, headers=headers)
# print(posted_response.text)



#get_endpoint = ENDPOINT + str(10)

# r = requests.get(get_endpoint)
# print(r.text)

# r2 = requests.get(get_endpoint)
# print(r2.status_code)

# post_headers = {
#     'content-type': 'application/json'
# }

# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)



# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     if img_path is not None:
#         with open(image_path,'rb') as image:
#             file_data = {
#                 'image':image
#             }
#             r = requests.request(method, ENDPOINT, data=data, files=file_data,headers=headers)
#     else:
#         r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

# do_img(method='put', data={'id':9,'user':1,'content':"Yooooooooo"}, is_json=False, img_path=image_path)


# def do(method='get', data={}, is_json=True):
#     headers = {}
#     if is_json:
#         headers['content-type'] = 'application/json'
#         data = json.dumps(data)
#     r = requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

#do(data={'id':5})
#do(method='delete', data={'id':3})
#do(method='put',data={'id':5, "content":"Some cool new content", 'user':1})
#do(method='post',data={"content":"Some cool new content", 'user':1})

