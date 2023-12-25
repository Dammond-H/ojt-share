import time
if __name__ == '__main__':
    fo = open("1.txt", "rb")
    while True:
        data = fo.readline()
        try:
            text = data.decode("utf-8")
            print(text)
        except Exception as e:
            print(data)
            time.sleep(1)

