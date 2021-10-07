import AWP

s = AWP.Server()

@s.route('/')
def home(t, p, d):
    return 200, {}, d['text']

s.serve()