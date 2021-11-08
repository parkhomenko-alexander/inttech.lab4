from clientFile import ClientFile
url = 'http://127.0.0.1:5000'

client = ClientFile(url)
print(client.files_post('1.txt'))
print(client.files_get())
print(client.download_file('222.txt'))
print(client.delete_file('3.txt'))
