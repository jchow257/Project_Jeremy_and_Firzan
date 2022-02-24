import requests

url = 'https://unsplash.com/'
x = requests.get(url)
print(x.text)
print(x.status_code)
print("\t*", x.status_code)

if x.status_code:
    print('OK')
else:
    print('BOO')

h = requests.head(url)
print("Header: ")
print("Top of the header")
for y in h.headers:
    print("\t", y, ":", h.headers[y])
print("Bottom of the header")


headers = {
    'User-agent' : 'Mobile'
}

ur12 = 'http://httpbin.org/headers'
xh = requests.get (ur12,
headers=headers)
print(xh.text)


