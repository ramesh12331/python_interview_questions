def generate():

    i = 0

    while i <= 200:
        yield i
        i += 1


a = generate()

print(next(a))
print(next(a))
print(next(a))
print(next(a))