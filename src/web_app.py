import fastapi
import os
from model import *
import json
from datetime import datetime


api_router = fastapi.APIRouter()

def pr_token():
    with open('token.txt', 'r') as file:
        token = file.read()
    return token

def filter():
    files = os.listdir(r'C:\Users\Pudge228\Desktop\git_repos\lab4\src\notes')
    result = [0]
    ext = '.json'
    for filename in files:
        if filename.endswith(ext):
            filename = filename.replace('.json','')
            result.append(filename)
    return sorted(list(map(int,result)))

def create():
    files = filter()
    name = int(len(files))
    with open('C:\\Users\\Pudge228\\Desktop\\git_repos\\lab4\\src\\notes\\'+str(name)+'.json', 'w') as file:
        a = Notes_text(id=name, text="")
        b = Notes_info(created=datetime.now(), updated=datetime.now())
        b = {k: str(v) for k,v in b.dict().items()}
        c = {
            'note': a.dict(),
            'data': b
        }
        json.dump(c, file)
    return name

@api_router.post('/create')
def create_note(token: str):
    if token == pr_token():
        id = Notes_create(id=create())
        return id
    else:
        return 'Неверный токен'
##
@api_router.get('/get_note')
def get_note(token: str, id:int):
    if token == pr_token():
        with open('C:\\Users\\Pudge228\\Desktop\\git_repos\\lab4\\src\\notes\\'+str(id)+'.json', "r") as file:
            notes = json.load(file)
        note = notes['note']
        a = Notes_text(id=note['id'], text=note['text'])
        return a
    else:
        return 'Неверный токен'
##
@api_router.patch('/up_note')
def up_note(token: str, id:int, text:str):
    if token == pr_token():
        with open('C:\\Users\\Pudge228\\Desktop\\git_repos\\lab4\\src\\notes\\'+str(id)+'.json', "r") as file:
            notes = json.load(file)
        notes['note']['text'] = text
        notes['data']['updated'] = str(datetime.now())
        with open('C:\\Users\\Pudge228\\Desktop\\git_repos\\lab4\\src\\notes\\'+str(id)+'.json', "w") as file:
            json.dump(notes, file)
        note = notes['note']
        a = Notes_text(id=note['id'], text=note['text'])
        return a
    else:
        return 'Неверный токен'
##
@api_router.get('/get_info')
def get_info(token: str, id:int):
    if token == pr_token():
        with open('C:\\Users\\Pudge228\\Desktop\\git_repos\\lab4\\src\\notes\\'+str(id)+'.json', "r") as file:
            notes = json.load(file)
        note = notes['data']
        c_d = datetime.strptime(note['created'],"%Y-%m-%d %H:%M:%S.%f")
        u_d = datetime.strptime(note['updated'],"%Y-%m-%d %H:%M:%S.%f")
        a = Notes_info(created=c_d, updated=u_d)
        return a
    else:
        return 'Неверный токен'
##
@api_router.delete('/delete_note')
def delete_note(token: str, id:int):
    if token == pr_token():
        path = r'C:\Users\Pudge228\Desktop\git_repos\lab4\src\notes'+f'\{str(id)}.json'
        try:
            os.remove(path)
            return f'Заметка {id} удалена'
        except:
            return 'Заметки с таким id не найдено'
    else:
        return 'Неверный токен'
##
@api_router.get('/list_note')
def list_note(token: str):
    if token == pr_token():
        n_list : List[int] = list(map(int,filter()))
        n_list.remove(0)
        return Notes_list(notes_list=n_list)
    else:
        return 'Неверный токен'