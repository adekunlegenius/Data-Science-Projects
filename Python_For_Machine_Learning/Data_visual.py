
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,100)
y= x*2
z = x**2

#print(x)

fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,.8,.8])
#fig, ax1 = plt.subplots()
ax1.plot(x,y)
ax1.set(xlabel="X axis", ylabel='Y axis', title='Plot of X against Y')
ax1.grid()

plt.show()

# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()