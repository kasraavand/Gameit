import pickle
from sys import path
path.append('/home/kasramvd/Desktop/Gameit/')
from src.Methods import GetMethod


# methods = GetMethod(method_path=kwargs['method_path'])


with open('functions/func.pickle', 'rb') as f:
    data = pickle.load(f)



def callattr(self):
    return 100


data.callattr = callattr

print(type(data.callattr))
print(data())
