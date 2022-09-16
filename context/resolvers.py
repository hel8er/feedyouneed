from tg.schemas import Update
from tg.obj import ctx
from bot_logic import *

@ctx.resolver
def commands_resolver(u: Update):
    print('cmd resolcer')
    return u.message.text and u.message.text.startswith('/')