from .schemas import Update
context = {}
functions = {}

def resolver(resolver_func):
    print('reslover', resolver_func)
    functions[resolver_func.__name__] = resolver_func
    return resolver_func

def require(func):        
    

    def zerofunc():
        pass

    def wrapper(*resolvers):
        print('wrap')
        functions[func.__name__] = func
        try:
            for resolver in resolvers:
                assert context.get(resolver) == True
            return func

        except AssertionError:
            return zerofunc
    return wrapper


def webhook(fn):
    def wrapper(update: Update):
        [fn() for fn in context.values()]
        [fn(update) for fn in functions.values()]
        return fn
    return wrapper

def build_context(update: Update):
    
    for resolve in functions.values():
        context[resolve.__name__] = resolve(update) 
    print('context:', context, functions)
