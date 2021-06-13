def Hello_World(n):
    if n > 0:
        print("Hello World!")
        if n > 1:
            Hello_World(n - 1)

Hello_World(0)
Hello_World(1)
Hello_World(10)