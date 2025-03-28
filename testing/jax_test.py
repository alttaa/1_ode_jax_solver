import jax.numpy as jnp
import numpy as np

def sys(x,a,b):
    return b*a*jnp.arcsinh(x)

ans = sys(jnp.array([0, 10]), 1.5, 3)

#-----------------------------------------------------------------

z = np.array([0,5, 10, 20])
print(z)



