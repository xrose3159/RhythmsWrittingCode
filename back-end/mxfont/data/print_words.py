import json

with open("./chn_primals.json","r") as file_in:
    wlist = json.load(file_in)
    print(wlist)