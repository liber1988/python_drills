def my_generator():
    print("Start")

    try:
        yield 1
        print("After first yield")

        yield 2
        print("After second yield")

    except Exception as e:
        print("Caught inside generator:", e)

    print("End")
user=my_generator()
print(next(user))
user.throw(Exception("An error occurred"))
print(user.__next__())
# print(user.__next__())


