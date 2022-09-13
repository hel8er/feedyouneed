from tg.schemas import Update
from .context import resolver

@resolver
def commands_resolver(u: Update):
    print('cmd resolcer')
    return u.message.text and u.message.text.startswith('/')