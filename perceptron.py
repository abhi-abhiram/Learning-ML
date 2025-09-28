import math

class Value:
    def __init__(self,value):
        self.value = value
        self.children = []
        self.op = None

    def __add__(self,other):
        v = Value(self.value + other.value)
        v.op = "+"
        v.children = [self,other]
        return v

    def __radd__(self,other):
        v = Value(self.value + other)
        v.op = "+"
        v.children = [self,Value(other)]
        return v
    
    def __mul__(self,other):
        v = Value(self.value * other.value)
        v.op = "*"
        v.children = [self,other]
        return v

    def  __rmul__(self,other):
        v = Value(self.value * other)
        v.op = "*"
        v.children = [self,Value(other)]
        return v


    def tanh(self):
        v = Value(math.tanh(self.value))
        v.op = "tanh(x)" 
        v.children = [self]
        return v

    def __str__(self):
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