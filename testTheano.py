# Theano tutorial
# Solution to Exercise in section 'Baby Steps - Algebra'
# import theano.tensor as T

# from __future__ import print_function
# import theano
# a = theano.tensor.vector()  # declare variable
# b = theano.tensor.vector()  # declare variable
# out = a ** 2 + b ** 2 + 2 * a * b  # build symbolic expression
# f = theano.function([a, b], out)   # compile function
# print(f([1, 2], [4, 5]))  # prints [ 25.  49.]

# from theano import In
# from theano import function
# x, y = T.dscalars('x', 'y')
# z = x + y
# f = function([x, In(y, value=1)], z)
# print(f(33))
# print(f(33, 2))
#
# from theano import shared
# state = shared(0)
# inc = T.iscalar('inc')
# accumulator = function([inc], state, updates=[(state, state+inc)])
# accumulator(1)
# print(state.get_value())

# from theano.tensor.shared_randomstreams import RandomStreams
# from theano import function
# srng = RandomStreams(seed=234)
# rv_u = srng.uniform((2,2))
# rv_n = srng.normal((2,2))
# f = function([], rv_u)
# g = function([], rv_n, no_default_updates=True)    #Not updating rv_n.rng
# nearly_zeros = function([], rv_u + rv_u - 2 * rv_u)
# fval0 = f()
# fval1 = f()
# print(fval0,fval1)
#
# gval0 = g()
# gval1 = g()
# print(gval0,gval1)
#
# nzero = nearly_zeros()
# print(nzero)
# print()
#
# state_after_v0 = rv_u.rng.get_value().get_state()
# nearly_zeros()       # this affects rv_u's generator
# '''array([[ 0.,  0.],
#        [ 0.,  0.]])'''
# v1 = f()
# rng = rv_u.rng.get_value(borrow=True)
# rng.set_state(state_after_v0)
# rv_u.rng.set_value(rng, borrow=True)
# v2 = f()             # v2 != v1
# v3 = f()              # v3 == v1
# print(v1,'\n',v2,'\n',v3,'\n')

# from __future__ import print_function
# import theano
# import numpy
# import theano.tensor as T
# from theano.sandbox.rng_mrg import MRG_RandomStreams
# from theano.tensor.shared_randomstreams import RandomStreams
#
# class Graph():
#      def __init__(self, seed=123):
#          self.rng = RandomStreams(seed)
#          self.y = self.rng.uniform(size=(1,))
#
# g1 = Graph(seed=123)
# f1 = theano.function([], g1.y)
#
# g2 = Graph(seed=987)
# f2 = theano.function([], g2.y)
#
# print(f1())
# print(f2())
#
# def copy_random_state(g1, g2):
#      if isinstance(g1.rng, MRG_RandomStreams):
#          g2.rng.rstate = g1.rng.rstate
#      for (su1, su2) in zip(g1.rng.state_updates, g2.rng.state_updates):
#          su2[0].set_value(su1[0].get_value())
#
#
# copy_random_state(g1, g2)
# print(f1())
# print(f2())

###################################logical regression############################
# import numpy
# import theano
# import theano.tensor as T
# rng = numpy.random
#
# N = 400                                   # training sample size
# feats = 784                               # number of input variables
#
# # generate a dataset: D = (input_values, target_class)
# D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))
# training_steps = 10000
#
# # Declare Theano symbolic variables
# x = T.dmatrix("x")
# y = T.dvector("y")
#
# # initialize the weight vector w randomly
# #
# # this and the following bias variable b
# # are shared so they keep their values
# # between training iterations (updates)
# w = theano.shared(rng.randn(feats), name="w")
#
# # initialize the bias term
# b = theano.shared(0., name="b")
#
# print("Initial model:")
# print(w.get_value())
# print(b.get_value())
#
# # Construct Theano expression graph
# p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))   # Probability that target = 1
# prediction = p_1 > 0.5                    # The prediction thresholded
# xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1) # Cross-entropy loss function
# cost = xent.mean() + 0.01 * (w ** 2).sum()# The cost to minimize
# gw, gb = T.grad(cost, [w, b])             # Compute the gradient of the cost
#                                           # w.r.t weight vector w and
#                                           # bias term b
#                                           # (we shall return to this in a
#                                           # following section of this tutorial)
#
# # Compile
# train = theano.function(
#           inputs=[x,y],
#           outputs=[prediction, xent],
#           updates=((w, w - 0.1 * gw), (b, b - 0.1 * gb)))
# predict = theano.function(inputs=[x], outputs=prediction)
#
# # Train
# for i in range(training_steps):
#     pred, err = train(D[0], D[1])
#     print(i,'\n')
#
# print("Final model:")
# print(w.get_value())
# print(b.get_value())
# print("target values for D:")
# print(D[1])
# print("prediction on D:")
# print(predict(D[0]))


##############

# import theano
#  import theano.tensor as T
# x = T.matrix('x')
# y = T.matrix('y')
# z = x*y
# f = theano.function([x,y],z)
# print(f([[1,2],[2,3]],[[3,4],[4,5]]))
'''>>>[[  3.   8.]
       [  8.  15.]]'''

# import numpy
# import theano
# import theano.tensor as T
# from theano import pp
# x = T.dscalar('x')
# y = x ** 2
# gy = T.grad(y, x)
# print(pp(gy))  # print out the gradient prior to optimization
# '((fill((x ** TensorConstant{2}), TensorConstant{1.0}) * TensorConstant{2}) * (x ** (TensorConstant{2} - TensorConstant{1})))'
# f = theano.function([x], gy)
# print(f(4))
# print(numpy.allclose(f(94.2), 188.4))

####################
# import theano
# import theano.tensor as T
# x = T.dvector('x')
# y = x ** 2
# J, updates = theano.scan(lambda i, y,x : T.grad(y[i], x), sequences=T.arange(y.shape[0]), non_sequences=[y,x])
# f = theano.function([x], J, updates=updates)
# print(f([4, 4]))
#
# cost = y.sum()
# gy = T.grad(cost, x)
# H, updates = theano.scan(lambda i, gy,x : T.grad(gy[i], x), sequences=T.arange(gy.shape[0]), non_sequences=[gy, x])
# f1 = theano.function([x], H, updates=updates)
# print(f1([4, 4]))
#
# ''''''''''''''''''''''''
# W = T.dmatrix('W')
# V = T.dmatrix('V')
# x2 = T.dvector('x2')
# y2 = T.dot(x2, W)
# JV = T.Rop(y2, W, V)
# f2 = theano.function([W, V, x2], JV)
# print(f2([[1, 1], [1, 1]], [[2, 2], [2, 2]], [0,1]))
#
# v = T.dvector('v')
# VJ = T.Lop(y2, W, v)
# f = theano.function([v,x2], VJ)
# print(f([2, 2], [0, 1]))


#########################


# from theano import tensor as T
# from theano.ifelse import ifelse
# import theano, time, numpy
#
# a,b = T.scalars('a', 'b')
# x,y = T.matrices('x', 'y')
#
# z_switch = T.switch(T.lt(a, b), T.mean(x), T.mean(y))
# z_lazy = ifelse(T.lt(a, b), T.mean(x), T.mean(y))
#
# f_switch = theano.function([a, b, x, y], z_switch,
#                            mode=theano.Mode(linker='vm'))
# f_lazyifelse = theano.function([a, b, x, y], z_lazy,
#                                mode=theano.Mode(linker='vm'))
#
# val1 = 0.
# val2 = 1.
# big_mat1 = numpy.ones((10000, 1000))
# big_mat2 = numpy.zeros((10000, 1000))
#
# n_times = 10
#
# tic = time.clock()
# for i in range(n_times):
#     f_switch(val1, val2, big_mat1, big_mat2)
# print('time spent evaluating both values %f sec' % (time.clock() - tic))
# print(f_switch(val1, val2, big_mat1, big_mat2))
#
# tic = time.clock()
# for i in range(n_times):
#     f_lazyifelse(val2, val1, big_mat1, big_mat2)
# print('time spent evaluating one value %f sec' % (time.clock() - tic))
# print(f_lazyifelse(val2, val1, big_mat1, big_mat2))


####################
import numpy
import theano
import theano.tensor as T

k = T.iscalar("k")
A = T.vector("A")

# Symbolic description of the result
result, updates = theano.scan(fn=lambda prior_result, A: prior_result * A,
                              outputs_info=T.ones_like(A),
                              non_sequences=A,
                              n_steps=k)

# We only care about A**k, but scan has provided us with A**1 through A**k.
# Discard the values that we don't care about. Scan is smart enough to
# notice this and not waste memory saving them.
final_result = result[-1]

# compiled function that returns A**k
power = theano.function(inputs=[A,k], outputs=final_result, updates=updates)

print(power(range(10),2))
print(power(range(10),4))


''''''''''''

coefficients = theano.tensor.vector("coefficients")
x = T.scalar("x")

max_coefficients_supported = 10000

# Generate the components of the polynomial
components, updates = theano.scan(fn=lambda coefficient, power, free_variable: coefficient * (free_variable ** power),
                                  outputs_info=None,
                                  sequences=[coefficients, theano.tensor.arange(max_coefficients_supported)],
                                  non_sequences=x)
# Sum them up
polynomial = components.sum()

# Compile a function
calculate_polynomial = theano.function(inputs=[coefficients, x], outputs=polynomial)

# Test
test_coefficients = numpy.asarray([1, 0, 2], dtype=numpy.float32)
test_value = 3
print(calculate_polynomial(test_coefficients, test_value))
print(1.0 * (3 ** 0) + 0.0 * (3 ** 1) + 2.0 * (3 ** 2))



