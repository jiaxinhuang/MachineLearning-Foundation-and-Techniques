#-*- coding:utf-8 -*-
'''
Created on 2017年10月23日

@author: Administrator
'''
import numpy as np
import matplotlib.pyplot as plt
import random

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

def calError(X, Y, w_t):
    num = len(X)
    error = 0
    for i in range(num):
        sign_value = sign(np.dot(X[i], w_t))
        if sign_value != Y[i, 0]:
            error += 1
    return error*1.0/num

def PLApocket(X, Y, w0, limit):
    num = len(X)
    w_temp = w0
    rand_sord = random.sample(range(num), num)
    
    for i in range(limit):
        sign_value = sign(np.dot(X[rand_sord[i]], w_temp))
        if sign_value != Y[rand_sord[i], 0]:
            w_temp = w_temp + Y[rand_sord[i], 0] * np.matrix(X[rand_sord[i]]).T
    error_now = calError(X, Y, w_temp)
    return w_temp, error_now
    
if __name__ == '__main__':
    filename_train = 'hw1_18_train.dat'
    filename_test = 'hw1_18_test.dat'
    X_train, Y_train = getData(filename_train)
    X_test, Y_test = getData(filename_test)
    train_total_err = 0
    test_total_err = 0
    
    limit = 50
    for i in range(2000):
        w0 = np.random.rand(5,1)
        w_result, err_train = PLApocket(X_train, Y_train, w0, limit)
#         print 'result of w: ', w_result, 'the err: ', err_train
        train_total_err += err_train
        err_test = calError(X_test, Y_test, w_result)
        test_total_err += err_test
    avg_train_err = train_total_err*1.0/2000
    avg_test_err = test_total_err*1.0/2000
    print 'avg_train_err:', avg_train_err, 'avg_test_err: ', avg_test_err