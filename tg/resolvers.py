from tg.schemas import Update
RESOLVERS = dict()

def resolver(func):
    """Регистрирует функцию как плагин"""
    RESOLVERS[func.__name__] = func
    return func

@resolver
def commands_resolver(u: Update):
    return u.message.text and u.message.text.startswith('/')
    


class Resolver:
    def validate():
        return False

    def run():
        pass