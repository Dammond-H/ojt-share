if __name__ == '__main__':

    d = {"name":"jack","age":20,"sex":"male"}
    print(d.setdefault("name",{}))
    print(d.setdefault("addr",{}))
    print(d)
    