from tg.schemas import Update
from context import Context
ctx = Context()

@ctx.resolver
def is_message(u: Update):
    return u.message


@ctx.resolver
def commands_resolver(u: Update):
    return is_message(u) and u.message.text.startswith('/')

@ctx.resolver
def start_command(u: Update):
    return u.message.text == '/start'

@ctx.resolver
def start_deeplink(u: Update):
    return u.message.text.split(' ').__len__ == 2