def add(x:int, y:int)->int:
    return x+y


if __name__ == "__main__":
    print(add(x=1, y=2))
    print(add(x=1.5, y=2))
    print(add.__annotations__)