from sys import path
path.append('/home/kasramvd/Desktop/Gameit/')
from src.RunParser import Run
import pickle


if __name__ == '__main__':
    run = Run(method_path='../test/data/methods.json',
              rules_path='../test/data/rules.json')

    run.create_functions()
