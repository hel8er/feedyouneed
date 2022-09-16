from context.resolvers import ctx


@ctx.require('commands_resolver')
def test(update):
    return('comand!!!', update.message.text)


