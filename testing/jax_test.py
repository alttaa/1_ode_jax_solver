import jax.numpy as jnp
import numpy as np
from jax import jit
from jax import grad


def sys(x,a,b):
    return b*a*jnp.arcsinh(x)

ans = sys(jnp.array([0, 10]), 1.5, 3)

#-----------------------------------------------------------------

z = np.array([0,5, 10, 20])
print(z)

#-----------------------------------------------------------------

# def sum_logistic(x):
#   return jnp.sum(1.0 / (1.0 + jnp.exp(-x)))
# x_small = jnp.arange(3.)
# derivative_fn = grad(sum_logistic)
# print(derivative_fn(x_small))


start, stop = sorted(np.random.uniform(0,10,size =2 ))
x = jnp.arange(start, stop, .1)
print(start, stop)
print(x)
