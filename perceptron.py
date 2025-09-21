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

    def __radd__(self,other):
        v = Value(self.value + other)
        v.op = Add(self,Value(other))
        return v
    
    def __sub__(self,other):
        v = Value(self.value - other.value)
        v.op = Subtract(self,other)
        return v
    
    def __mul__(self,other):
        v = Value(self.value * other.value)
        v.op = Multiply(self,other)
        return v

    def  __rmul__(self,other):
        v = Value(self.value * other)
        v.op = Multiply(self,Value(other))
        return v

    def __truediv__(self,other):
        v = Value(self.value * other.value)
        v.op = Divide(self,other)
        return v

    def tanh(self):
        v = Value(math.tanh(self.value))
        v.op = Tanh(self)
        return v

    def __str__(self):
        left = None
        if self.op != None:
            left = str(self.op)
        
        if left != None:
            return f"{left} = {str(self.value)}"

        return str(self.value) 


class Perceptron: 
    output = None
    def __init__(self,sw):
        self.weights = [Value(0) for _ in range(sw)]  


    def __call__(self,inputs):
        sigmaResult = self.sum([i * w for i,w in zip(inputs,self.weights)])
        v = sigmaResult.tanh()
        self.output = v
        return v

    def sum(self,inputs):
        total = Value(0)
        for input in inputs:
            total += input
        return total



class Layer:
    perceptrons = []

    def __init__(self,sp,sw):
        self.perceptrons = [Perceptron(sw) for _ in range(sp)] 

    def __call__(self,inputs):
        outputs = []
        for p in self.perceptrons:
            outputs.append(p(inputs))
        return outputs


        

class MultiLayer:
    def __init__(self, numOfInputs, size):
        total_size = [numOfInputs] + size
        self.layers = [Layer(total_size[i + 1],total_size[i]) for i in range(len(size))]

    def run(self,inputs):
       temp = inputs
       for layer in self.layers:
        layer * temp
        temp = layer
       return temp

    def __call__(self, inputs):
        for layer in self.layers:
            inputs = layer(inputs)
        return inputs
        
        
inputs = [1,2,3]

network = MultiLayer(3,[4,4,1])

outputs = network(inputs)


for i in outputs:
    print(i)