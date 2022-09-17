from resolvers import ctx


@ctx.require('commands_resolver', 'start_deeplink')
def test(update):
    return('comand!!!', update.message.text)
