class CustomRange:
    def __init__(self, a, b=None):
        if isinstance(a, int) and isinstance(b, int): 
            self.a = a
            self.b = b
        if isinstance(a, str) and isinstance(b, str):
            if a.isnumeric() and b.isnumeric():
                self.a = int(a)
                self.b = int(b)
        if isinstance(a, list) and b==None:
            if len(a) == 2:
                self.a = a[0]
                self.b = a[1]
                
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.a < self.b:
            self.a += 1
            return self.a
        else:
            raise StopIteration
        return self.a

myiter = iter(CustomRange(3,8))

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
