import requests

BASE = "http://127.0.0.1:5000/"

#response = requests.get(BASE + "helloworld/ben")
#print(response.json())


#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())

#response = requests.delete(BASE + "video/0")
#print(response)
#input()
#response = requests.get(BASE + "video/7")
#print(response.json())

response = requests.get(BASE + "helloworld/hi")

#response = requests.patch(BASE + "video/2", {"views": 99})
print(response.json())