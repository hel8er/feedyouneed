from tg.schemas import Update
# from .resolvers import *
class Context:
    def __init__(self) -> None:
        self.context = {}
        self.resolvers = {}
        self.functions = {}

    def resolver(self, resolver_func):
        print('reslover', resolver_func)
        self.resolvers[resolver_func.__name__] = resolver_func
        return resolver_func

    def require(self, *resolvers):
        print('dec param', resolvers)

        def wrapper(fn):
            print('wrapper', fn)
            def called(update: Update):
            
                try:
                    for rs in resolvers:
                        assert self.context.get(rs) == True
                    return fn(update)
                except AssertionError:
                    return('pass func')
            print('called')
            self.functions[fn.__name__] = called

            return called
        


            
        return wrapper

    def webhook(self, fn):
    #print('webhook', fn)
        def wrapper(update: Update):
            #print('upd', update)
            for resolver in self.resolvers.values():
                self.context[resolver.__name__] = resolver(update) 
            print('context:', self.context, self.resolvers, self.functions)
            for handle in self.functions.values():
                print(handle.__name__)
                print(handle(update))

            return fn
        return wrapper

        
            
