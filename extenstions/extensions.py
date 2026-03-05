import re
def extensionNamer(fileName):
    extension = fileName.split('.')
    #extension = re.findall(r'.[a-z]+', fileName)
    if extension[-1] == 'gif' or extension[-1] == 'png':
        return f'image/{extension[-1]}'
    elif extension[-1] == 'jpg' or extension[-1] == 'jpeg':
        return 'image/jpeg'
    elif extension[-1] == 'pdf':
        return f'application/{extension[-1]}'
    elif extension[-1] == 'txt':
        return f'text/{extension[0]}'
    elif extension[-1] == 'zip':
        return f'application/{extension[-1]}'

    return 'application/octet-stream'

fileName = input("File name: ").lower().strip()

print(extensionNamer(fileName))
