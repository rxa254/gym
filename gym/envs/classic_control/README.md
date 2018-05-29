### some info about these environments

- they use Euler's method for the integration, which is error prone. Should check if we can fix it with RK4 or some simple leapfrog. Rumor is that scipy.odeint is not fast enough


#### Suspended Fabry-Perot Cavity
1. The mirrors at the end are pendula.
1. The power in the cavity is determined by the cavity length.
1. There should be some seismic noise.
1. The laser has no frequency noise.
1. Maybe the mirror-suspension position sensors have some noise? e.g. 0.1 nm/rHz.


##### CartPole
This is a moving cart with a pole attached to it. By applying 1D forces to the massive cart, the pole can be swung up.

The condition for "winning" is to have the pole stand up and the cart not hit the 'edges' of the space.

Differentional equations for the cart-pole problem:
http://www.matthewpeterkelly.com/tutorials/cartPole/cartPoleEqns.pdf
