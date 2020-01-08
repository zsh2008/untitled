
class chess:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self, kind):
        return 'Chesse(%r)' % (self.kind)


import weakref

if __name__ == "__main__":
    stock = weakref.WeakKeyDictionary()
    