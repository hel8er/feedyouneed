from tg import context, resolvers

@context.require('commands_resolver')
def test(update):
    print('comand!!!', update.message.text)