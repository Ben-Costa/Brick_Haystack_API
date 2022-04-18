import re
import requests
import timeit
import time
from permulations import perm1,perm2, perm3, perm4, perm5, perm6
from Backend.Operations import ReadHS

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

#response = requests.get(BASE + "helloworld/hi")

#response = requests.patch(BASE + "video/2", {"views": 99})
#print(response.json())

#+ '?q=unit and unocc'

file = open('log.txt', 'w')

#_id == a-0000
#+ '?q=sp and cooling and geoAddr'
#numberRuns = 10
#counter = 0
#while counter < numberRuns:
#    start = time.perf_counter()
#    response = requests.get(BASE )
#    finish = time.perf_counter()
#    print('time was: ' + str(finish - start) )
#    print(str(finish-start), file = file)
#    counter = counter + 1

#print('\n', file = file)    
#print(ReadHS('a', '', 10, 1).rowsLength(), file = file)


for search in perm4:    
    testQuery = search
    url = BASE + '?q=' + search[0] + ' and ' + search[1] + ' and ' + search[2] + ' and ' + search[3]#+ ' and ' + search[1] + ' and ' + search[2] + ' and ' + search[3] + ' and ' + search[4]
    print(search[0] + ' and ' + search[1] + ' and ' + search[2]+ ' and ' + search[3], file = file )#+ ' and ' + search[1] + ' and ' + search[2] + ' and ' + search[3] + ' and ' + search[4], file = file)
    numberRuns = 10
    counter = 0
    while counter < numberRuns:
        start = time.perf_counter()
        response = requests.get(url)
        finish = time.perf_counter()
        print('time was: ' + str(finish - start) )
        print(str(finish-start), file = file)
        counter = counter + 1
    
    print('\n', file = file)
    print(ReadHS('a', search[0] + ' and ' + search[1] + ' and ' + search[2] + ' and ' + search[3], 10, 1).rowsLength(), file = file)
    print('\n', file = file)

#url = BASE + '?q=' + '_id == a-0000'
#response = requests.get(url)
#temp = response.json()
#'_id == a-0000
#file.close()



#tests
#1 make the testit infrastructure, select 10 random from each permutation and run 10 times, print the results to text file
#2 test the query on the Point database for various random queries and compare to same queries on the shaystack api
#3 try to find a way to time the shaystack data