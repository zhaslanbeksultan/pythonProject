import json
with open("sample_data.json", "r") as read_file:
    data = json.load(read_file)
print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU
-------------------------------------------------- --------------------  ------  ------""")
for i, k in data["imdata"][0]['l1PhysIf']["attributes"].items():
    # for key, value in d.items():
    if i == 'dn':
        print(k, end = "                                ")
    if i == "speed":
        print(k)
    if i == "mtu":
        print(k, end="   ")