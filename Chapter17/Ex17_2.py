import copy

class Kangaroo:
    """
    punch_contents: list
    """
    def __init__(self, name, contents=[]):
        self.name = name
        self.pouch_contents = copy.copy(contents) # different object
        #self.pouch_contents = contents
    def __str__(self):
        print("list: ",id(self.pouch_contents))
        t = [self.name + ' has: ']
        for s in self.pouch_contents:
            s1 = object.__str__(s) + ',  '
            t.append(s1)
        return '\n'.join(t)
    def put_in_pouch(self, other):
        self.pouch_contents.append(other)
        '''

        if isinstance(other, Kangaroo):
            return self.add_other(other)
        else:
            return self.increment(other)
        '''
    def add_other(self, other):
        print('add_other')
        if not other.pouch_contents:
            for item in other.pouch_contents:
                self.pouch_contents.append(item)
    def increment(self, other):
        print('increment')
        if isinstance(other, list):
            for item in other:
                print('list:', item)
                self.pouch_contents.append(item)
        else:
            print('str: ', other)
            self.pouch_contents.append(other)

def main():
    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    print()
    print(roo)

if __name__ == '__main__':
    main()



