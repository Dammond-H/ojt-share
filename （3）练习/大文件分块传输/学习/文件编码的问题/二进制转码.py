if __name__ == '__main__':
    text = "黄林强academic%￥nn1234..."
    data = text.encode("utf-8")
    print(type(data))
    # encode = text.encode("unicode")
    # print(encode)
    print(data)
    temp = b""
    for item in data:
        temp += chr(item).encode("latin1")
        # print(item)
        # print(type(chr(item).encode("latin1")))
        # print(chr(item).encode("latin1"),end=" ")
    print(temp)