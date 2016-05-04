class Person(object):
    _registry = ['hello', 'haha']

    def __init__(self, name):
        self._registry.append(self)
        self.name = name

print(Person.'Kyle')
