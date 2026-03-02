import json

f = open("tmp.json", "rb")
mapping = json.load(f)


f = open("tmp2.json", "rb")
procs = json.load(f)

q = input("Filter keyword: ")

res = {}

for p in procs:
    if q.lower() in p["Name"].lower():
        r = None
        res[p["Name"]] = []
        for m in mapping:
            if m["OwningProcess"] == p["Id"]:
                res[p["Name"]].append(m)
                print(p["Id"]," | ",p["Name"],"|","local:"+str(m["LocalPort"]),"|","remote:"+str(m["RemotePort"]))

filt = ""
flag = False
for rr in res:
    for rrr in res[rr]:
        if flag:
            filt += " || "
        else:
            flag = True

        if rrr["LocalPort"] != 0 and rrr["RemotePort"] != 0:
            filt += "tcp.port == "+str(rrr["LocalPort"])
            filt += " || "
            filt += "tcp.port == "+str(rrr["RemotePort"])
        else:
            if rrr["LocalPort"] != 0:
                filt += "tcp.port == "+str(rrr["LocalPort"])
            if rrr["RemotePort"] != 0:
                filt += "tcp.port == "+str(rrr["RemotePort"])

print("\n"+filt)

