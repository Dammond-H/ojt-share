def sendTo():
    d = {
        "name":"jack",
        "age":20,
        "gender":"male"
    }
    receiveTo(d)

def receiveTo(d):
    print(d)

if __name__ == '__main__':
    sendTo()