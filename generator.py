
############ Random Number Generator ########################

""" Coding a pseudo-random number generator using a Linear Congruential Generator algorithm:

X(n+1)=(a*X(n) + c)mod(M)

Parameters:
0<a<M, a is called multiplier
0=<c<M, c is called increment
M is the modulus which is also the max range for this sequence
M>0
X_{0},0=<X_{0}<m — the "seed" or "start value"
mod stands for modulus operation. Eg. 7 mod 3 = 1 """

class LCG(object):
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current_random = seed
        self.recurrence_relation = (self.multiplier*self.current_random + self.increment)%self.modulus

    
    def get_seed(self):
        return self.seed
        
    def set_seed(self,seed):
        self.seed = seed
    
    def get_multiplier(self):
        return self.multiplier 
        
    def set_multiplier(self, mult):
        self.multiplier = mult
        
    def get_increment(self):
        return self.increment
        
    def set_increment(self,inc):
        self.increment = inc
        
    def get_modulus(self):
        return self.modulus
        
    def set_modulus(self,mod):
        self.modulus = mod

    def next_random_number(self):
        self.current_random = ((self.multiplier*self.current_random + self.increment)%self.modulus) / self.modulus
        return self.current_random
        
    def sequence_random_number(self,length):
        R = []
        for i in range(0,length):
            R.append(self.next_random_number())
        return R
            
    

#Test case for LCG
seed = 1
multiplier = 1103515245
increment = 2**32
modulus = 12345

myLCG = LCG(seed,multiplier,increment,modulus)
print(myLCG.next_random_number())
print(myLCG.sequence_random_number(4))


""" Creating an inherited class with same attributes but different recurrence relation
Seed of this generator has to satisfy X_{0}%4 = 2"""


class SCG(LCG):
    def __init__(self, seed, multiplier, increment, modulus):
        LCG.__init__(self, seed, multiplier, increment, modulus)
        self.recurrence_relation = (self.current_random*(self.current_random + 1))%self.modulus
        if self.seed % 4 != 2:
            raise ValueError('seed value does not have a remainder of 2') 
    
    def next_random_number_variant(self):
        Xn = ((self.current_random*(self.current_random + 1))%self.modulus) / self.modulus
        self.current_random = Xn
        return Xn
    
    def sequence_random_number_variant(self,length):
        R = []
        for i in range(0,length):
            R.append(self.next_random_number_variant())
        return R

#Test case for SCG
mySCG = SCG(10,multiplier, increment, modulus)
print(mySCG.next_random_number_variant())
print(mySCG.sequence_random_number_variant(4))





