
def main():
    print("start")
    _dict = {
        "key1" : "value 1",
        "key2" : "value 2"
    }
    print(_dict)
    keys = _dict.keys()
    print(keys)
    print(type(keys))
    for k in keys:
        print(k)
    print(_dict.values())
    _tup = (1,2,3,4)
    print(_tup)
    print(type(_tup))
    _tup = (1,2)
    print(_tup)


if __name__ == "__main__":
    main()