from .schemas import Update
context = {}
functions = ()
def resolver(resolver_func):

    def wrapper(*args, **kwargs):
        context[resolver_func.__name__] = resolver_func()
        
    return wrapper


def require(func):        
    def zerofunc():
        pass

    def wrapper(*resolvers):
        try:
            for resolver in resolvers:
                assert context.get(resolver) == True
            return func

        except AssertionError:
            return zerofunc
    return wrapper


def webhook(fn):
    def wrapper(update: Update):
        print('update text:', update.message.text)
        return fn
    return wrapper