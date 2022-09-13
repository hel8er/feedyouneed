from .schemas import Update
context = {}
resolvers = {}
functions = {}

def resolver(resolver_func):
    print('reslover', resolver_func)
    resolvers[resolver_func.__name__] = resolver_func
    return resolver_func

def require(*resolvers):
    print('dec param', resolvers)

    def zerofunc():
        print('zerof')

    def wrapper(fn):
        print('wrap', fn)
        try:
            for resolver in resolvers:
                assert context.get(resolver) == True
            return fn

        except AssertionError:
            print('zero')
            return zerofunc
        
    return wrapper


def webhook(fn):
    #print('webhook', fn)
    def wrapper(update: Update):
        #print('upd', update)
        for resolver in resolvers.values():
            context[resolver.__name__] = resolver(update) 
        print('context:', context, resolvers)
        [handle(update) for handle in functions.values()]

        return fn
    return wrapper

def build_context(update: Update):
    
    for resolve in functions.values():
        context[resolve.__name__] = resolve(update) 
    print('context:', context, functions)
