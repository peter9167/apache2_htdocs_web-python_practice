import os

def getList():
    files = os.listdir('data') # 특정 폴더(ex -> 'data') 파일 리스트 가져오기
    listStr = '' # listStr 초기화
    for item in files: # 저장되어 있는 files 만큼 반복
      listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
    