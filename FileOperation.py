import json

def funcReadFile(pathFile):
    with open(pathFile,'r') as fileTxt:
        message = fileTxt.read().replace('\n',' ')
    return message

def funcWriteFile(data):
    with open('code.json', 'w') as file:
        data = json.loads(data)  
        json.dump(data, file)