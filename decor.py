from time import time

def verbose(f):
    def wrapped(*args, **kwargs):
        print f.func_name, 'called with args:', args, 'and keyword args:', kwargs
        return f(*args, **kwargs)
    wrapped.__name__ = f.__name__
    return wrapped

def timer(f):
    def wrapped(*args, **kwargs):
        a = time()
        print 'Executing', f.func_name + '...'
        ret = f(*args, **kwargs)
        print 'Finished execution of', f.func_name + '. Execution time = %d ms.' % int((time() - a) * 1000)
        return ret
    wrapped.__name__ = f.__name__
    return wrapped
        
@verbose
@timer
def testF(a, b, c, d=5, e=6, f=7):
    for i in range(1000000000):
        a += b + c + d + e + f
    return a

@timer
def test2(a, b, c, d=5, e=6, f=7):
    for i in range(1000000000):
        a += b + c + d + e + f
    return a

@verbose
def test3(a, b, c, d=5, e=6, f=7):
    for i in range(1000000000):
        a += b + c + d + e + f
    return a

print test2(1, 2, 3, 4, **{'e': 7, 'f':10})
print test3(1, 2, 3, 4, **{'e': 7, 'f':10})
print testF(1, 2, 3, 4, **{'e': 7, 'f':10})
