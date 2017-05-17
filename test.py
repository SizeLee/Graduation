# from theano import *
import theano
# import theano.tensor as T
import numpy as np
from io import BytesIO
import pylab
import sys
import matplotlib.pyplot as plt

# x = np.array([[1,2,3],[4,5,6]])
# y = np.asarray([[1,2,3],[4,5,6]])
# z = np.array(x)[1] = 2
# a = np.asarray(y)[1] = 2
# print(x)
# print(y)
# print(a)

# x = np.array([1,2,3])
# y = np.array([1.,2.,3.])
# x = x.astype(float)
# x = np.float32(x)
# print(x.dtype)
# print(y.dtype)

# a = np.arange(10)**3
# print(a)
# a[:6:2] = -1
# print(a,'\n')
# print(a[:6:2],'\n')
#
# def myadd(x,y):
#     return 10*x+y
#
# b = np.arange(10).reshape(2,5)
# print(myadd(a.reshape([2,5]),b),'\n')
#
# print(a,'\n')
#
# for row in b:
#     print(row)
#     row = 1
# print(b,'\n')
#
# print(np.tile(b,[3,2]),'\n')
#
# print(np.arange(0,6),'\n')
#
# for column in np.arange(0,5):
#     print(b[:,column])
#
# print(b.shape)
#
# b.shape = (5,2)
#
# print(b)
# print()
#
# b.reshape(2,5)
# print(b)
#
# b.resize(2,5)
# print(b)
#
# print(np.random.random((10,10)))
# # print(b[np.newaxis,:,:])
# # print(b[:,np.newaxis,:])
# # print(b[:,:,np.newaxis])
#
# a=np.array([4.,2.])
# b=np.array([2.,8.])
#
# print(a[:,np.newaxis])

# print(np.column_stack((a,b)))
# print(np.row_stack((a,b)))
#
# print(np.column_stack((a[:,np.newaxis],b[:,np.newaxis])))
# print(np.row_stack((a[:,np.newaxis],b[:,np.newaxis])))
#
# print(np.column_stack((a[np.newaxis,:],b[np.newaxis,:])))
# print(np.row_stack((a[np.newaxis,:],b[np.newaxis,:])))

# l=[1,2,3]
# ll=l
# print(ll is l)
# lll = l.copy()
# print(lll is l)
# print()
#
# i = np.array( [ [0,1],                        # indices for the first dim of a
#                 [1,2] ] )
# j = np.array( [ [2,1],                        # indices for the second dim
#                 [3,3] ] )
#
# a = np.arange(12).reshape(3,4)
# s = np.array([i,j])
# print(s)
# print(tuple(s))
# # print(a[s])  #wrong indicies
# print(a[tuple(s)])
# print()

# A = np.arange(12)
#
# A.shape = (3, 4)
# M = np.mat(A.copy())
# print(type(A), "  ", type(M))
#
# print(A)
# print(M)
#
# M = np.mat(A)
# print(type(A), "  ", type(M))
# print(M is A)
# print(M.base is A)
#
# print(A[:,1].shape,A[:,1])
# print()
# print(M[:,1].shape,M[:,1])
#
# print(M[:,] == M[:])
#
# print(np.ix_((1,2),(1,3)))
# print(A[[[1,1]
#         ,[2,2]],[[1,3],
#                  [1,3]]])
# print(A[np.ix_((1,2),(1,3))])
#
#
# A[0,:]>1
# #array([False, False, True, True], dtype=bool)
# print(A[:,A[0,:]>1])
# '''array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])'''
# M = np.mat(A.copy())
# print(type(M))
# print(M[0,:]>1)
# #matrix([[False, False, True, True]], dtype=bool)
# #print(M[:,M[0,:]>1])
# #matrix([[2, 3]]) this code went wrong,too many indices for array
#
# print(M.A[0,:]>1)
# print(M[:,M.A[0,:]>1])
# '''matrix([[ 2,  3],
#            [ 6,  7],
#            [10, 11]])'''
#
# print(A[A[:,0]>2,A[0,:]>1])
# #array([ 6, 11])
# print(M[M.A[:,0]>2,M.A[0,:]>1])
# #matrix([[ 6, 11]])      变成索引对号入座形式  两个相同维度的索引，每个位置一一对应，得到元素的横纵坐标，所以取了两个数。需要采用ix_()的方法,
# #或者采用两个多维索引来一一对应
#
# print(A[np.ix_(A[:,0]>2,A[0,:]>1)])
# '''array([[ 6,  7],
#        [10, 11]])'''
# print(M[np.ix_(M.A[:,0]>2,M.A[0,:]>1)])
# '''matrix([[ 6,  7],
#         [10, 11]])'''
# print()
#
# print(A[-1,1:4])
# print(M[-1,1:4])
# print(A[-3:-1,1:4])
# print(M[-3:-1,1:4])
# print()
#
# ########################################################################
#
# x = np.arange(0,10,2)                     # x=([0,2,4,6,8])
# y = np.arange(5)                          # y=([0,1,2,3,4])
# m = np.vstack([x,y])                      # m=([[0,2,4,6,8],
#                                        #     [0,1,2,3,4]])
# xy = np.hstack([x,y])                     # xy =([0,2,4,6,8,0,1,2,3,4])
#
# n = np.array([x,y])
# print(n)
# print(n==m)
# print(type(n),type(m))
#
# # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# mu, sigma = 2, 0.5
# v = np.random.normal(mu,sigma,10000)
# # Plot a normalized histogram with 50 bins
# pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
# pylab.show()
# # Compute the histogram with numpy and then plot it
# (n, bins) = np.histogram(v, bins=50, normed=True)  # NumPy version (no plot)
# pylab.plot(.5*(bins[1:]+bins[:-1]), n)
# pylab.show()

##############################################

# x = np.eye(2, dtype=theano.config.floatX)
# w = np.ones((2, 2), dtype=theano.config.floatX)
# b = np.ones((2), dtype=theano.config.floatX)
# b[1] = 2
# print(b,'\n')
# print(x.dot(w)+b,'\n')
# print(np.tanh(x.dot(w) + b),'\n')

############
# a = tuple([1,2])
# b = tuple([2,3])
# c = a+(4,)
# print(c)
###########
# x = np.floor(5*0.39999999)
# print(x)
# print('123'
#       '456')
# x = range(5)
# print(x)
#
# x = np.array([[[ -0.25435214,  0.14849252,  0.28359378,  0.54253786],
#   [ 0.11925088,  -0.14849252,  0.28359378,  0.54253786],
#   [ 0.11925088,  0.25435214,  -0.28359378,  0.54253786]],
#               [[ 0.06751567,  -0.11925088,  0.25435214,  0.54253786],
#   [ -0.06751567,  0.11925088,  0.25435214,  0.28359378],
#   [ 0.06751567,  0.11925088,  0.25435214,  -0.14849252]]])
# print(x)
# print(x.shape)
# print(np.amax(x, axis=0))
# print(np.argmax(x, axis=0))
# print(x.max(0),'\n')##sample
#
# print(np.amax(x, axis=1))
# print(np.argmax(x, axis=1))
# print(x.max(1),'\n')##column
#
# print(np.amax(x, axis=2))
# print(np.argmax(x, axis=2))
# print(x.max(2),'\n')##row
# print()
#
# y = x[0,:,:]
# print(y.max(0),'\n')
# print(y.max(1),'\n')
#
# print(np.abs(x))

# y = np.array([[ -0.25435214,  0.14849252,  0.28359378,  0.54253786],
#   [ 0.11925088,  -0.14849252,  0.28359378,  0.54253786],
#   [ 0.11925088,  0.25435214,  -0.28359378,  0.54253786]])
# k = np.array([[ 0.06751567,  -0.11925088,  0.25435214,  0.54253786],
#   [ -0.06751567,  0.11925088,  0.25435214,  0.28359378],
#   [ 0.06751567,  0.11925088,  0.25435214,  -0.14849252]])

# z = np.hstack((y,k))
# print(z)
# z[:] = 1
# print(y)
# print(z)
# z = y.transpose()
# print(y[1:2,:])
#
# x = 2 * np.ones((10, 4, 2))
# y = 3 * np.ones((10, 2))
# z = np.dot(x, y.T)
# print(z)
# print(z.shape)

# for sample in x:
#   print(sample)
#   print()
#
# print((2,3,4)==(2,3,4))
#
# x = 2 * np.ones((10, 4, 2))
# y = 3 * np.ones((10, 2))
#
# # for a,b in x,y:    wrong way to iterate
# #   print(a)
# #   print(b)
# print(x[1])
# print(x[1,:,:])
# x = np.ones((2,2))
# ls = list()
# for i in range(5):
#     ls.append(x)
#
# print(ls)
# y = np.array(ls)
# print(y)
# print(y.shape)

# a = None
# if a is not None:
#     print(1)
# else:
#     print(0)
#
# print(k[1:3,:].shape)
# a = np.array([[1, 2, 3], [2, 4, 3]])
# b = np.array([1, 3, 3])
# print(np.argmax(a, axis=1))
# print(np.argmax(a, axis=0))
#
# print(float('1.'))

# print(str(np.array([[1,0,0], [2,0,0]])[1, :]))
# x = np.array([[1,0,0], [2,0,0]])
# print(x.argmax(1))
#
# l = [0] * 5
# print(l)
#
# d = dict()
# d[1] = 0
# print(d)

# a = 0.
# b = 0.
# print(a<=b)
#
# class A:
#     pass
#
# def func(sdf):
#     sdf1 = sdf
#     return sdf1
#
# x = A()
# y = func(x)
# print(x is y)

x = np.linspace(-4, 4, 30)
y = np.sin(x)

plt.figure(figsize=(4,4))
plt.plot(x, y, '--*b')
plt.savefig('123.png')

x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)

plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("Time(s)")
plt.ylabel("Volt")
plt.title("PyPlot First Example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.savefig('234.png')
# plt.show()

plt.figure()
plt.plot([1,2,3], [7,5,6])
plt.show()
