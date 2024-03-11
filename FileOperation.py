import os
import re
import json
import shutil
from datetime import datetime

def funcReadFile(pathFile):
    with open(pathFile,'r') as fileTxt:
        message = fileTxt.read().replace('\n',' ')
    return message

def funcWriteFile(data,pathFile):
    with open(f"{pathFile}\code.json", 'w') as file:
        data = json.loads(json.dumps(data, indent=4))
        json.dump(data, file)

def funcMakeDir():
    dirName = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    if not os.path.isdir(dirName):
        os.mkdir(dirName)
        return (f"{os.getcwd()}\{dirName}")

def clearHistory():
    pattern = re.compile(r'\d{4}-\d{2}-\d{2}-\d{2}-\d{2}-\d{2}')
    for object in os.listdir():
        if pattern.match(object):
            shutil.rmtree(object)