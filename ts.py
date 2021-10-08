import AWP

s = AWP.Server()

@s.route('/')
def home(t, p, d):
    return 200, {}, d['text']

@s.route('/h')
def h(t, p, d):
    return 200, {}, 'Hello\nWorld'

s.serve()