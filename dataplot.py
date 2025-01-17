import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,100)
print(x)

y=2*x
z=x**2
fig = plt.figure()
ax = fig.add_axes(x,y)
ax.set_xlabel("x")
ax.set_ylabel("2x")
ax.set_title