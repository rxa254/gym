### some info about these environments

- they use Euler's method for the integration, which is error prone. Should check if we can fix it with RK4 or some simple leapfrog. Rumor is that scipy.odeint is not fast enough


##### CartPole
This is a moving cart with a pole attached to it. By applying 1D forces to the massive cart, the pole can be swung up.

The condition for "winning" is to have the pole stand up and the cart not hit the 'edges' of the space.

Differentional equations for the cart-pole problem:
http://www.matthewpeterkelly.com/tutorials/cartPole/cartPoleEqns.pdf
