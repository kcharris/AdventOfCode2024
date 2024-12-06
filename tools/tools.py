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
            open(f"Day{i}\\data.txt", mode="x")
        except FileExistsError:
            print("File already Exists")
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
    with open(f"Day{day}\\data.txt", mode="r") as f1:
        if len(f1.read()) == 0:
            f1 = open(f"Day{day}\\data.txt", mode="w")
            cookies = {"session": env.session_cookie}
            address = f"https://adventofcode.com/2024/day/{day}/input"
            r = requests.get(address, cookies=cookies)
            if r.status_code != 404:
                f1.write(r.text)
                print("Successfully retrieved data")
            else:
                print(r.status_code)
        else:
            print("Already has data")

getInputData()