import requests

url = 'https://unsplash.com/'
response = requests.get(url)
print(response.text)
print("Status code:")
print("\t*", response.status_code)

if response.status_code :
    print('OK')
else:
    print('BOO')

h = requests.head(url)
print("Header: ")
print("Top of the header")
for y in h.headers:
    print("\t", y, ":", h.headers[y])
print("Bottom of the header")
