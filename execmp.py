try:
    a = 10
    b = 0
    print(a/b)
except Exception as e:
    print(e)
    print('Handle you exception')
finally:
    raise EOFError
