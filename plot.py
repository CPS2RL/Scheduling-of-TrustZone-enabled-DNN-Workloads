

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline


def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)

x=[0,10,20,30,40,50,60,70,75,80,85,87,90,92,94,96,98,100]
#y1 is the feasible taskset using vanila rm scheduling
y1=[100,100,100,100,100,100,100,100,100,100,100,100,87,66,42,10,0,0]

#y2 is the feasible taskset using our proposed model
y2=[100,100,100,100,100,100,100,100,100,100,100,100,98,89,85,45,12,4]


X_Y_Spline1 = make_interp_spline(x, y1)
X_Y_Spline2 = make_interp_spline(x, y2)
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(0,100, 100)
Y1_ = X_Y_Spline1(X_)
Y2_ = X_Y_Spline2(X_)


x_zoom=[85,87,90,92,94,96,98,100]
y1_zoom=[100,100,87,66,42,10,0,0]
y2_zoom=[100,100,98,89,85,45,12,4]

fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.imshow(data)
#ax.set_aspect('equal')
plt.xlabel("Utilization (%)")
plt.ylabel("Percentage of Feasible Taskset")
#plt.plot(X_,Y1_,linestyle='--',color='b',label="Vanilla RM Scheduling")
#plt.plot(X_,Y2_,linestyle='-',label="Proposed Work")

plt.plot(x,y1,"^",markersize=4,linestyle='-',color='b',label="Vanilla RM Scheduling")
plt.plot(x,y2,"s",markersize=4,linestyle='--',label="Proposed Work")

#plt.grid()
#ax.set_aspect('auto')
axes=plt.gca()
axes.set_aspect(1)

axes.plot(x_zoom,y1_zoom,c='green',lw=1,label="zoomed curve")

plt.savefig("taskscheduling.pdf", format="pdf", bbox_inches="tight")
plt.show()

