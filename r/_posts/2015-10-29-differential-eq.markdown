---
layout: post
title: "Differential equations in Python"
---

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

There is often no analytical solution to systems with nonlinear interacting dynamics.  We can, however, examine the dynamics using numerical methods.  Consider the predator-prey system of equations, where there are fish ($$x$$) and fishing boats ($$y$$):

$$
\begin{align*}
\frac{dx}{dt} &=& x(2 - y - x) \\
\frac{dy}{dt} &=& -y(1 - 1.5x)
\end{align*}
$$  

We use the built-in SciPy function `odeint` to solve the system of ordinary differential equations, which relies on `lsoda` from the FORTRAN library `odepack`.  First, we define a callable function to compute the time derivatives for a given state, indexed by the time period.  We also load libraries that we'll use later to animate the results.

{% highlight python %}
import matplotlib.animation as animation
from scipy.integrate import odeint
from numpy import arange
from pylab import *

def BoatFishSystem(state, t):
    fish, boat = state
    d_fish = fish * (2 - boat - fish)
    d_boat = -boat * (1 - 1.5 * fish)
    return [d_fish, d_boat]
{% endhighlight %}

Then, we define the state-space and intital conditions, so that we can solve the system of linear equations.  The result is animated with respect to time.

{% highlight python %}
t = arange(0, 1000, 0.05)
init_state = [1, 1]
state = odeint(BoatFishSystem, init_state, t)

fig = figure()
xlabel('number of fish')
ylabel('number of boats')
plot(state[:, 0], state[:, 1], 'b-', alpha=0.2)

def animate(i):
    plot(state[0:i, 0], state[0:i, 1], 'b-')

ani = animation.FuncAnimation(fig, animate, interval=2)
show()
{% endhighlight %}

![](/images/differential-animated.gif)

It is easy to break this result by messing with the solver parameters or the size of the time steps (relative to the total time), demonstrating the fragility of the result for real-world applications.  If, for example, we increase the step size from 0.5 to 10, we lose most of the dynamics that characterize the system.

![](/images/diff-direct.png)
