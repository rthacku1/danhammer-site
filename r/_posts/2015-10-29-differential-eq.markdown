---
layout: post
title: "Differential equations in Python"
---

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

There is often no analytical solution to systems with nonlinear, interacting dynamics.  We can, however, examine the dynamics using numerical methods.  Consider the predator-prey system of equations, where there are fish ($$x$$) and fishing boats ($$y$$):

$$
\begin{align*}
\frac{dx}{dt} &= x(2 - y - x) \\
\frac{dy}{dt} &= -y(1 - 1.5x)
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

Then, we define the state-space and intital conditions, so that we can solve the system of linear equations.  The result is animated below.  (The code for some of the graphical bells and whistles is omitted for the sake of exposition.)

{% highlight python %}
t = arange(0, 20, 0.1)
init_state = [1, 1]
state = odeint(BoatFishSystem, init_state, t)

fig = figure()
xlabel('number of fish')
ylabel('number of boats')
plot(state[:, 0], state[:, 1], 'b-', alpha=0.2)

def animate(i):
    plot(state[0:i, 0], state[0:i, 1], 'b-')

ani = animation.FuncAnimation(fig, animate, interval=1)
show()
{% endhighlight %}

![](/images/differential-animated-dual.gif)

The red, dashed lines indicate the nullclines, derived from the first-order conditions of the equation system.  These lines delineate the phase space of the top graph; and the lines intersect at the equilibrium levels of fish and boats.

$$
\begin{align*}
\frac{dx}{dt} = 0 &\implies y = 2 - x \\
\frac{dy}{dt} = 0 &\implies x = 2/3
\end{align*}
$$  

It is easy to break this result by messing with the solver parameters or the size of the time steps (relative to the total time), demonstrating the fragility of the result for real-world applications.  If, for example, we increase the step size from 0.1 to 5, we lose most of the dynamics that characterize the system.  The same goes for fiddling with the iteration parameters of the ODE solver.

Suppose we wanted to figure out the behavior of this system near the equilibrium *before* going through the numerical estimation.  First, we linearize the system near the equilibrium, yielding the Jacobian.  Let $$f(x, y) = dx/dt$$ and $$g(x, y) = dy/dt$$, then the nonlinear system can be approximated by the following linear system near the equilibrim $$(\bar{x}, \bar{y})$$:

$$
\begin{align*}
f(x, y) &\approx f(\bar{x}, \bar{y}) + \frac{\partial f(\bar{x}, \bar{y})}{\partial x}\left(x - \bar{x}\right) + \frac{\partial f(\bar{x}, \bar{y})}{\partial y}\left(y - \bar{y}\right)\\
g(x, y) &\approx g(\bar{x}, \bar{y}) + \frac{\partial g(\bar{x}, \bar{y})}{\partial x}\left(x - \bar{x}\right) + \frac{\partial g(\bar{x}, \bar{y})}{\partial y}\left(y - \bar{y}\right)
\end{align*}
$$

Noting that $$f(\bar{x}, \bar{y}) = g(\bar{x}, \bar{y}) = 0$$ by definition of the equilibrium, the nonlinear system is approximated by the linear system defined by the Jacobian, evaluated at the equilibrium:

$$
\left( 
\begin{array}{cc} 
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\
\frac{\partial g}{\partial x} & \frac{\partial g}{\partial y}
\end{array}
\right)
= 
\left( 
\begin{array}{cc} 
2 - y - 2x & -x \\
1.5y & 1 - 1.5x
\end{array}
\right)
= 
\left( 
\begin{array}{cc} 
-\frac{2}{3} & -\frac{2}{3} \\
2 & 0
\end{array}
\right)
$$

Then the eigenvalues $$\lambda$$ are given by:

$$
\left|
\begin{array}{cc} 
-\frac{2}{3} - \lambda & -\frac{2}{3} \\
2 & -\lambda
\end{array}
\right| 
= 0 
\implies 
\lambda^{2} + \frac{2}{3}\lambda + \frac{4}{3} 
= 0
\implies
\lambda = -\frac{2}{3} \pm i\sqrt{\frac{44}{9}}
$$

The real part is negative and there is an imaginary component, such that the system will oscillate around the equilibrium tending inward.  This behavior is reflected in the animation.  I guess we didn't really have to go through all this work; but whatever, it's useful for other problems.

---

## Schaefer model

[Bjorndal and Conrad (1987)](http://cahnrs-cms.wsu.edu/_layouts/downloadFile.aspx?file=/ses/people/galinato_g/Documents/EconS431/bjorndal%20and%20%20conrad.pdf) modelled open-access exploitation of North Sea herring between 1963 - 1977.  Their model is similar to the one above, except slightly more complicated.  Let fish stock ($$x$$) and fishing effort ($$y$$) be modelled by the following system:

$$
\begin{align*}
\frac{dx}{dt} &= gx\left(1 - \frac{x}{K}\right) - kxy \\
\frac{dy}{dt} &= kpx - c,
\end{align*}
$$  

where $$k$$ is a catchability constant, $$g$$ is the intrinsic growth rate of the fish stock, $$K$$ is the carrying capacity, $$p$$ is the fish price, and $$c$$ is the marginal cost of one unit of effort.  Then, through the same process as above, we find that the equilibrium point (at the intersection of the nullclines) is:

$$
\left( \frac{c}{pk}, \frac{g}{k}\left( 1 - \frac{c}{pkK}\right) \right)
$$

Using the constants in Bjorndal and Conrad (1987) we model the system similarly:

{% highlight python %}
price = 735
effort_scale = 2e-6
marginal_cost = 556380
carrying_capacity = 3.2e6
intrinsic_growth = 0.08
catchability = marginal_cost / (price * 0.25e6)

def BoatFishSystem(state, t, time_scale=0.1):
    stock, effort = state
    net_growth = intrinsic_growth * stock * (1 - (stock/carrying_capacity))
    harvest = catchability * stock * effort
    d_stock = net_growth - harvest
    d_effort = effort_scale * (price * catchability * stock - marginal_cost)
    return [d_stock * time_scale, d_effort * time_scale]
{% endhighlight %}

![](/images/differential-animated-schaefer.gif)

The Jacobian for this system evaluated at the equilibrium is:

$$
\left( 
\begin{array}{cc} 
-\frac{gc}{pkK} & -kx \\
pk & 0
\end{array}
\right)
$$

I don't want to solve this by hand, so I plug it into Python.

{% highlight python %}
from numpy import linalg
values, vectors = linalg.eig(J_equil)
print values
>>> [-0.003125+41.01820462j -0.003125-41.01820462j]
{% endhighlight %}

The eigenvalues are $$\lambda = -0.0031 \pm 41.0182i$$.  Once again, the behavior seen in the numerical approximation is confirmed by math.  The system oscillates and tends inward.

Shit can get weird.  The numerical approximations, while very good in Python, can misrepresent the system of equations, given certain parameters.  Specifically, the system is solved through an iterative process of calculating the linear change at each interval, approximating the continuous system.  Choosing certain step sizes and tolerances will send Python or Matlab into a tailspin.  Although, the checks and balances within `odeint` are really quite good, such that it's way easier to break the numerical approximation if you try to write it explicitly in a for-loop.












