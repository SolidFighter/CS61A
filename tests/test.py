def first(x):
    x += 8
    def second(y):
        print('second')
        return x + y
    print('first')
    return second
f = first(15)
f
print(f(16))


def even(f):
    def odd(x):
        if x < 0:
            return f(-x)
        return f(x)
    return odd

stevphen = lambda x: x
stewart = even(stevphen)
stewart
stewart(61)
