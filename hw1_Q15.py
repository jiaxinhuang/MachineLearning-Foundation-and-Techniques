#-*- coding:utf-8 -*-
'''
Created on 2017年10月23日

@author: Administrator
'''
import numpy as np

def getData(filename):
    with open(filename, 'r') as f:
        dataTotal = f.readlines()
    
    num = len(dataTotal)
    X = np.zeros((num, 5))
    Y = np.zeros((num, 1))
    
    for i in range(num):
        data = dataTotal[i].split()
        data = map(float, data)
        X[i, 0] = 1.0
        X[i, 1:5] = data[0:4]
        Y[i, 0] = data[4]
        
    return X, Y
   

def sign(num):
    if num <= 0:
        return -1
    else:
        return 1

def PLAnaive(X, Y, w0):
    num = len(X)
    w = w0
    step = 0
    while True:
        err_count = 0
        for i in range(num):
#             print np.dot(X[i], w)[0]
            sign_value = sign(np.dot(X[i], w)[0])
            if sign_value != Y[i, 0]:
                w = w + Y[i, 0] * np.matrix(X[i]).T
                err_count += 1
                step += 1
#                 if (sign_value == -1) and (Y[i, 0] == -1):
#                 print sign_value, Y[i, 0]
        print 'the step: ', step, 'err_count: ', err_count
        if err_count == 0:
            break
    return w
    

if __name__ == '__main__':
    filename = 'hw1_15_train.dat'
    X, Y = getData(filename)
    w0 = np.zeros((5, 1))
    w_opt = PLAnaive(X, Y, w0)
    print w_opt