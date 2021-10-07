import AWP

c = AWP.Client('0.0.0.0')

print(c.get(data={'text':input('> ')}))