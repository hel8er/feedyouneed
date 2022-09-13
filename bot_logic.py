from tg import context, resolvers

@context.require(resolvers.commands_resolver)
def test(update):
    print('comand!!!', update.message.text)