---
layout: post
title: "Exceptional control"
---

<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

Admittedly this isn't the most interesting post.  It is likely _only_
interesting to [Peter Berck](http://are.berkeley.edu/~peter/).  But, honestly,
that's the only person I care about for this post, since he has the power of
the (red) pen.  It may also be interesting to [Tamma
Carleton](https://are.berkeley.edu/users/tamma-carleton), but only because I
worked with her to figure out how to model the difference between exceptional
control and open access fisheries.

The objective of this post is to directly demonstrate how optimal management
of a fishery where the owner controls total fishing effort differs from the
extraction in open access.  Formerly, we are looking for a solution to the
following constrained optimization problem:

$$
\max_{E} \int_{0}^{\infty} e^{-rz} E (pkx - c) \, dz \quad \text{ subject to } \quad \dot{x} = f(x) - kEx,
$$  

where $$E$$ is aggregate fishing effort normalized to number of trips, $$x$$
is the fish stock, $$f(x)$$ is the biological growth for a given fish stock,
and $$k$$ is a "catchability" constant.  Note that $$pkx - c$$ is a boat's
profits, catch less cost.  For the open access problem, boats enter when
profits are positive and exit when profits are negative, implying that profits
must be zero in equilibrium.  Our current problem is to maximize the present
value of resource extraction by controlling the number of boat trips.  To do
this, note that the associated Hamiltonian is:

$$
H(x, E, \lambda) = E(pkx - c) + \lambda (f(x) - kEx)
$$

Let $$x^{*}$$ be the optimal stock for this problem and $$x^{\text{open}}$$ be
the optimal stock for open access. Then, there are four equations to compare
the dynamics for the two regimes.

$$
\begin{align}
    \dot{\lambda} - r\lambda = -\frac{\partial H}{\partial x} = 0 - pkE - \lambda f^{\prime}(x) + \lambda k E && \qquad \text{[costate] (1)} \\
    \dot{x} = f(x) - kEx && \qquad \text{[costate] (2)} \\
    \frac{\partial H}{\partial E} = pkx − c −\lambda k x = 0 && \qquad \text{[max Hamiltonian] (3)} \\
    \frac{d}{dx}\frac{\partial H}{\partial E} = pk\dot{x} − \lambda k \dot{x} - \dot{\lambda} k x = 0 && \qquad \text{[stable for some time] (4)} \\
\end{align}
$$

The following is a recipe, of sorts, to find a closed-form solution for
$$x^{*}$$ in terms of given parameters.

1. Solve for $$\dot{\lambda}$$ from Eqn. (4): $$\dot{\lambda} = \frac{\dot{x}}{x}(p - \lambda)$$
2. Solve for $$(p - \lambda)$$ from Eqn. (3): $$(p - \lambda) = \frac{c}{kx}$$
3. Combine the previous two steps: $$\dot{\lambda} = \frac{\dot{x}}{x}\frac{c}{kx}$$
4. Note that $$r - f^{\prime}(x) = 0$$ in open access.  How does optimal
control compare?  The result requires some algebraic acrobatics.\\

    a. Isolate $$r - f^{\prime}(x)$$ in Eqn. (1): $$\dot{\lambda} - (r - f^{\prime}(x))\lambda = - (p - \lambda)kE $$\\
    b. Solve for $$kE$$ from Eqn. (2): $$kE = \frac{f(x) - \dot{x}}{x}$$\\
    c. Use Step 3 to find the control expression for $$r - f^{\prime}(x)$$

    $$
    \begin{equation*}
        r - f^{\prime}(x) = \frac{cf(x)}{x(pxk - c)}
    \end{equation*}
    $$

Note that there is just one unknown in the final expression, namely $$x$$
which will be our optimal stock.  Actually finding the optimal stock is a
heroic effort in algebra, since it can involve somewhat complicated
expressions for $$f(x)$$, like the logistic growth function $$f(x) = gx(1 -
x/\kappa)$$.  However, there are some accessible insights from the existing
expressions.  Note that $$r - f^{\prime}(x) > 0$$ when $$pkx - c > 0$$, i.e.,
when $$x > c/(pk)$$.  As such, when $$x^{*} > c/(pk) = x^{\text{open}}$$, $$r
> f^{\prime}(x)$$.  When the optimal stock is greater than the open access
stock, then the interest rate is greater than stock growth; and when the
optimal stock is less than the open access stock, the interest rate is less
than stock growth.  With this, we have adequately constructed the exceptional
control and sort of compared it to the open access solution.













