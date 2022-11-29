class Pohon :
    def __init__(self,A:int=None,L:int=None,R:int=None):
        self.A = A
        self.L = L
        self.R = R
    
    def __repr__(self):
        return "((%s, %s, %s))" % (repr(self.A), repr(self.L), repr(self.R))
    
def root(P) :
    return P.A

def left(P) :
    return P.L

def right(P) :
    return P.R

def MakeBT(A:int=None,L:int=None,R:int=None) :
    return Pohon(A,L,R)

#Predikat
def IsEmptyTree(P:Pohon) :
    return P == None
    
def IsBiner(P:Pohon) :
    return not(IsEmptyTree(P)) and not(IsEmptyTree(left(P))) and not(IsEmptyTree(right(P))) 

def IsUnerLeft(P:Pohon) :
    return not(IsEmptyTree(left(P))) and IsEmptyTree(right(P)) and not(IsEmptyTree(P))

def IsUnerRight(P:Pohon) :
    return not(IsEmptyTree(right(P))) and IsEmptyTree(left(P)) and not(IsEmptyTree(P))

def IsOneElmt(P:Pohon) :
    return not(IsEmptyTree(P)) and IsEmptyTree(left(P)) and IsEmptyTree(right(P))

def IsExistLeft(P:Pohon) :
    return not(IsEmptyTree(P)) and not(IsEmptyTree(left(P)))

def IsExistRight(P:Pohon) :
    return not(IsEmptyTree(P)) and not(IsEmptyTree(right(P)))

def IsMember(P:Pohon,x:int) :
    if (root(P) == x) :
        return True
    elif IsEmptyTree(P) :
        return False
    else : 
        if IsBiner(P) :
            return IsMember(left(P),x) or IsMember(right(P),x)
        elif IsUnerLeft(P) :
            return IsMember(left(P),x)
        elif IsUnerRight(P) :
            return IsMember(right(P),x)
        
# def IsSkewright(P:Pohon) :
#     if IsEmptyTree(P) :
#         return False
#     elif IsOneElmt(P) :
#         return False
#     else :
#         if IsBiner(P) and IsUnerLeft(P):
#             return False
#         elif IsUnerRight(P) :
#             if IsBiner(P) :
#                 return False
#             else :
#                 return IsSkewright()
            
def IsSkewLeft(P:Pohon) :
    if IsEmptyTree(P) and IsOneElmt(P) :
        return False
    else :
        if IsUnerLeft(P) :
            if IsOneElmt(left(P)) :
                return True
            else :
                if IsUnerLeft(left(P)) :
                    return IsSkewLeft(left(P))
                else : 
                    return False
        else :
            return False
        
def IsSkewRight(P:Pohon) :
    if IsEmptyTree(P) and IsOneElmt(P) :
        return False
    else :
        if IsUnerRight(P) :
            if IsOneElmt(left(P)) :
                return True
            else :
                if IsUnerRight(right(P)) : 
                    return IsSkewRight(right(P))
                else :
                    return False
        else :
            return False
            
#Konstruktor
def NbElmt(P:Pohon) :
    if IsOneElmt(P) :
        return 1
    else :
        if IsBiner(P) :
            return NbElmt(left(P)) + 1 + NbElmt(right(P))
        elif IsUnerLeft(P) :
            return NbElmt(left(P)) + 1
        else :
            return 1 + NbElmt(right(P))
        
def NbDaun(P:Pohon) :
    if IsOneElmt(P) :
        return 1
    else :
        if IsBiner(P) :
            return NbDaun(left(P)) + NbDaun(right(P))  
        elif IsUnerLeft(P) :
            print(P)
            return NbDaun(left(P))
        else :
            print(P)
            return NbDaun(right(P))

def RepPrefix(P:Pohon) :
    if IsOneElmt(P) :
        return [root(P)]
    else :
        if IsBiner(P) :
            return [root(P)] + RepPrefix(left(P)) + RepPrefix(right(P))
        elif IsUnerLeft(P) :
            return [root(P)] + RepPrefix(left(P))
        elif IsUnerRight(P) :
            return [root(P)] + RepPrefix(right(P))

#PredikatVersi2
# def IsMember(P:Pohon,x:int) :
#     if (root(P) == x) :
#         return True
#     elif (IsEmptyTree(P)) :
#         return False
#     else :
#         if IsBiner(P) :
#             return IsMember(left(P),x) or IsMember(right(P),x)
#         elif IsUnerLeft(P) :
#             return IsMember(left(P),x)
#         elif IsUnerRight(P) :
#             return IsMember(right(P),x)
#         else :
#             return False

#Operator
def LevelOFX(P:Pohon,x) :
    if not(IsMember(P,x)) :
        return 0
    else :
        if root(P) == x :
            return 1
        else :
            if IsBiner(P) :
                return 1 + LevelOFX(right(P),x) + LevelOFX(left(P),x)
            elif IsUnerLeft(P) :
                return 1 + LevelOFX(left(P),x)
            else :
                return 1 + LevelOFX(right(P),x)

def AddDaunTerkiri(P:Pohon,x:int) :
    if IsEmptyTree(P) :
        return MakeBT(x)
    else :
        if IsEmptyTree(left(P)) :
            return MakeBT(root(P),MakeBT(x),right(P))
        else :
            return MakeBT(root(P),AddDaunTerkiri(left(P),x),right(P))     

def AddDaunTerkanan(P:Pohon,x:int) :
    if IsEmptyTree(P) :
        return MakeBT(x)
    else :
        if IsEmptyTree(right(P)) :
            return MakeBT(root(P),left(P),right(x))
        else :
            return MakeBT(root(P),left(P),AddDaunTerkanan(right(x)))

# def AddDaun(P,x,y,Kiri) :
    

  


pohon = MakeBT(10,MakeBT(5,MakeBT(2),MakeBT(7)),MakeBT(12,MakeBT(15),MakeBT(17)))
# print(IsSkewRight(pohon))
print(NbDaun(pohon))
print(LevelOFX(pohon,5))
print(AddDaunTerkiri(pohon,8))
print(IsMember(pohon,2))
print(RepPrefix(pohon))
 
            
            
