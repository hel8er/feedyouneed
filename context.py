class Context:
    def __init__(self) -> None:
        self.context = {}
        self.resolvers = {}
        self.runners = {}

    def resolver(self, resolver_func):
        self.resolvers[resolver_func.__name__] = resolver_func
        return resolver_func

    def require(self, *resolvers):
        print('required', resolvers)

        def wrapper(fn):
            def check_required(*args, **kwargs):
                try:
                    for rs in resolvers:
                        assert self.context.get(rs) == True
                    print('resolver passed:', rs)
                    return fn(*args, **kwargs)
                except AssertionError:
                    return('resolver failed', rs)
                
            self.runners[fn.__name__] = check_required
            return check_required
        return wrapper

    def build_context(self, *args, **kwargs):
            for resolver in self.resolvers.values():
                self.context[resolver.__name__] = resolver(*args, **kwargs) 
            print('context:', self.context, self.resolvers, self.runners)

            for fn in self.runners.values():
                print(fn(*args, **kwargs))
