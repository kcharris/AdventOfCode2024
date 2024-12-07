import os
import requests
import env
from pprint import pprint

def generateFolders(start, end):
    for i in range(start, end):
        newpath = f"Day{i}"
        if not os.path.exists(newpath):
            os.mkdir(newpath)
        try:
            open(f"Day{i}\\answer1.py", mode="x")
        except FileExistsError:
            print("File already Exists")
        try:
            open(f"Day{i}\\answer2.py", mode="x")
        except FileExistsError:
            print("File already Exists")
        a1 = open(f"Day{i}\\answer1.py", mode="w")
        a1.write(
                f"""f = open("Day{i}\\data.txt")\n""")
        a2 = open(f"Day{i}\\answer2.py", mode="w")
        a2.write(f"""f = open("Day{i}\\data.txt")""")

def ints(s):
    return list(map(int, s.split()))

def getInputData(day):
    try:
        with open(f"Day{day}\\data.txt", mode="x") as f1:
            cookies = {"session": env.session_cookie}
            address = f"https://adventofcode.com/2024/day/{day}/input"
            r = requests.get(address, cookies=cookies)
            if r.status_code == 200:
                f1.write(r.text)
                print("Successfully retrieved data")
            else:
                f1.close()
                os.remove(f"Day{day}\\data.txt")
                print(r.status_code)
    except FileExistsError:
        print("File already created")

getInputData(7)