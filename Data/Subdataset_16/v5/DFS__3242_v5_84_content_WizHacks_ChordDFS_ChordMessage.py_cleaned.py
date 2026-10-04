class class1:
    b1 = "b1"
    b2 = "b2"
    b3 = "b3"
    b4 = "b4"
    b5 = "b5"
    b6 = "b6"
    b7 = "b7"
    b8 = "b8"
    b9 = "b9"
    b10 = "b10"
    b11 = "b11"
    b12 = "b12"
    b13 = "b13"
    b14 = "b14"
    b15 = "b15"
    b16 = "b16"
    b17 = "b17"
    b18 = "SEND"
    b19 = "REQUEST"
    b20 = "INSERT"
    b21 = "b21"
    b22 = "b22"
def fonk1():
    return {
        'msg_type': None,
        'filename': None,
        'finger': None,
        'client_ip': None,
        'successor_ip': None,
        'key': None,
        'target': None,
        'predecessor_ip': None,
        'content': None,
        'hash': None,
        'dead_node': None,
        'file_list': None,
        'hops': 0
    }
def fonk2(b24):
    print("Message Dictionary:")
    for key, value in b24.items():
        print(f"{key}: {value}")
if b23 = = "__main__":
    b24 = fonk1()
    b24['msg_type'] = class1.b8
    b24['filename'] = 'example.txt'
    b24['client_ip'] = '192.168.1.1'
    fonk2(b24)