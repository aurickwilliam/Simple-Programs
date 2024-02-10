def foo(x):
    try:
        return 10 / x
    except ZeroDivisionError:
        return "Error"
    finally:
        return 0
    

print(foo(0))