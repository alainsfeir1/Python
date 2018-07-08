class passwordChecker:
    def __init__(self,password,passwordSplit=[],valid=True):
        self.password=password
        self.passwordSplit=passwordSplit
        self.valid=valid
    def passwordConverter(self):
        self.passwordSplit=list(self.password)
    def passSize(self):
        size=len(self.passwordSplit)
        if size >=12 or size <=6:
            print("1.Size["+str(size)+",Invalid size]")
            self.valid=False
        else:
            print("1.Size["+str(size)+",valid size]")
    def letterChecker(self):
        countUpper=0
        countLower=0
        for i in self.passwordSplit:
            if i.isupper():
                countUpper+=1
            if i.islower():
                countLower+=1
        if countUpper>=1:
            print("2.Upper letter exsits["+str(countUpper)+"]")
        if countUpper<1:
            print("2.Upper letter missing")
            self.valid=False
        if countLower>=1:
            print("3.Lower letter exsits["+str(countLower)+"]")
        if countLower<1:
            print("3.Lower letter missing")
            self.valid=False
    def specialChararacterChecker(self):
        counter=0
        chars=["$","#","@"]
        for words in self.passwordSplit:
            for char in chars:
                if words==char:
                    counter+=1
        if counter>=1:
            print("4.Valid characters")
        else:
            print("4.Missing special characters\n")
            self.valid=False
    def Validity(self):
        if self.valid==True:
            print("Password accepted by system")
        else:
            print("Password rejected by system")
