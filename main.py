import torch as tr
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision.utils import make_grid
import matplotlib.pyplot as plt
import numpy as np

def U(x,y,U_0=0.4): #potential function, U_0 is the amplitude, x and y are the coordinates, Gradient needs to be calculated manually in forward pass.
    if (x**2+y**2)**0.5<=0.5:
        return tr.tensor((16*U_0*((x**2+y**2)**0.5-0.25)**2),dtype=tr.half)
    else:
        print('potato')
        return tr.tensor(0,dtype=tr.half)
def F(x,y):#Force
    return tr.gradient(U(x,y))

def rotate_vector(vector,phi):
    return tr.tensor([vector[0]*tr.cos(phi)-vector[1]*tr.sin(phi),vector[0]*tr.sin(phi)+vector[1]*tr.cos(phi)],dtype=tr.half)



class Agent(nn.Module):
    def __init__(self,x=-0.5,y=-0.5,b=0):#initialize agent at location (-0.5,-0.5)
        super(Agent, self).__init__()
        self.x=x #x coordinate
        self.y=y #y coordinate
        self.b=b #bias
        self.input = nn.Linear(5, 64) #input layer
        self.hidden = nn.Linear(64, 32) #hidden layer
        self.output = nn.Linear(32, 4) #hidden layer
        self.activation = nn.ReLU() #activation function
        #self.arctan = nn.Atan() #arctan function

    def forward(self, x): #forward pass
        x1 = self.activation(self.input(x))
        x2 = self.activation(self.hidden(x1))
        x3 = self.activation(self.output(x2))
        return x3
    

    def move(self,dx,dy):
        if not -0.5<=self.x+dx<=0.5:
            dx=0
        if not -0.5<=self.y+dy<=0.5:
            dy=0
        self.x+=dx
        self.y+=dy
     



X,Y = tr.as_tensor(np.meshgrid(np.linspace(-0.75,0.75,43),np.linspace(-0.75,0.75,43)))

print(F)
    