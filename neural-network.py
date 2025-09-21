import math
import numpy  as np


class Operator:
    def __init__(self,op):
        self.op = op


class Tanh(Operator):
    def __init__(self,input):
        super().__init__("Tanh")
        self.input = input


    def __str__(self):
        input = None
        if self.input.op != None:
            input = self.input.op
        else:
            input = self.input


        return f"(tanh({input}))"

class BinaryOp(Operator):
    def __init__(self, op,left,right):
        super().__init__(op)
        self.left = left
        self.right = right

    def __str__(self):
        left = None
        right = None


        if self.left.op != None:
            left = self.left.op
        else:
            left = self.left

        if self.right.op != None:
            right = self.right.op
        else:
            right = self.right

        return f"({left} {self.op} {right})"


class Add(BinaryOp):
    def __init__(self, l, r):
        super().__init__("+",l,r)


class Subtract(BinaryOp):
    def __init__(self, l, r):
        super().__init__("-",l,r)


class Multiply(BinaryOp):
    def __init__(self,l,r):
        super().__init__("*",l,r)


class Divide(BinaryOp):
    def __init__(self,l,r):
        super().__init__("/",l,r)
    
    

class Value:
    op = None
    def __init__(self,value):
        self.value = value

    def __add__(self,other):
        v = Value(self.value + other.value)
        v.op = Add(self,other)
        return v
    
    def __sub__(self,other):
        v = Value(self.value - other.value)
        v.op = Subtract(self,other)
        return v
    
    def __mul__(self,other):
        v = Value(self.value * other.value)
        v.op = Multiply(self,other)
        return v

    def __truediv__(self,other):
        v = Value(self.value * other.value)
        v.op = Divide(self,other)
        return v

    def __str__(self):
        left = None
        if self.op != None:
            left = str(self.op)
        
        if left != None:
            return f"{left} = {str(self.value)}"

        return str(self.value) 


class Perceptron: 
    weights = np.random.random(4)
    def __init__(self,inputs):
        self.output = self.activation(inputs @ self.weights)

    def activation(self,input):
        return math.tanh(input)
        
    


# input = np.random.random(4)

# p = Perceptron(input)

# a = Value(10)
# b = Value(20)

# c = a + b

# d = a * c

# e = d - c

# print(e)