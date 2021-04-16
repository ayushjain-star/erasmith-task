import requests

link = input('Enter link to be tested\n')

if(requests.get(link).status_code == 200):
    print(link + ' is working')
else:
    print(link + ' is not working')
