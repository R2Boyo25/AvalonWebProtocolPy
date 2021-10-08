import AWP

c = AWP.Client('0.0.0.0')

print(c.get(data={'text':input('> ')})[1])
print(c.get('/h')[1])