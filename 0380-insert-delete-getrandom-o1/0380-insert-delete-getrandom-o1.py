class RandomizedSet:
    def __init__(self):
        self.a,self.d=[],{}


    def insert(self, v: int) -> bool:
        return (v in self.d)^1 and not (setitem(self.d,v,len(self.a)) or self.a.append(v))
        

    def remove(self, v: int) -> bool:
        return v in self.d and not (lambda e,i:i<len(self.a) and (setitem(self.a,i,e) or setitem(self.d,e,i)))(self.a.pop(),self.d.pop(v))
        

    def getRandom(self) -> int:
        return choice(self.a)