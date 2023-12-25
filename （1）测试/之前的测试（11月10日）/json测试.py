import json
def isJson(s):
    try:
        dictData = json.loads(s)
    except ValueError as e:
        return False
    return True

if __name__ == '__main__':
    d = {
        "name":"jack",
        "age":20,
        "gender":"male"
    }
    s = "shishsihsi"
    encode = json.dumps(d).encode("utf-8")
    s_encode = s.encode("utf-8")
    print(isJson(encode.decode("utf-8")))
    print(type(encode.decode("utf-8")))
    print(type(s_encode.decode("utf-8")))
    print(isJson(s_encode.decode("utf-8")))
