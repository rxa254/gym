from __future__ import division
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path
pi = np.pi

class PendulumEnv(gym.Env):
    metadata = {
        'render.modes' : ['human', 'rgb_array'],
        'video.frames_per_second' : 5
    }

    def __init__(self):
        self.max_speed  = 8       # units ? (should be SI)
        self.max_torque = 10
        self.dt         = 0.05
        self.viewer = None

        high = np.array([1., 1., self.max_speed])
        self.action_space = spaces.Box(low  = -self.max_torque,
                                       high =  self.max_torque,
                                      shape = (1,))
        self.observation_space = spaces.Box(low = -high, high = high)

        self._seed()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, u):
        th, thdot = self.state # th := theta
        
        g  = 9.81       # gravity ?
        m  = 1.0        # mass ?
        L  = 1.0        # pendulum length ?
        dt = self.dt

        u           = np.clip(u, -self.max_torque, self.max_torque)
        self.last_u = u # for rendering
        # this is the cost function (x + v + F)
        costs       = (angle_normalize(th)**2 +
                           0.1*thdot**2 +
                           0.001*(u**2))

        # v = v + a*dt
        newthdot  = thdot
        thddot    = -3*g/(2*L) * np.sin(th + np.pi)
        thddot   +=  3/(m*L**2) * u
        newthdot += thddot * dt
        
        newth    = th + (newthdot * dt)
        #pylint: disable=E1111
        newthdot = np.clip(newthdot, -self.max_speed, self.max_speed) 

        self.state = np.array([newth, newthdot])
        return self._get_obs(), -costs, False, {}

    def _reset(self):
        high = np.array([np.pi, 1])
        self.state = self.np_random.uniform(low=-high, high=high)
        self.last_u = None
        return self._get_obs()

    def _get_obs(self):
        theta, thetadot = self.state
        return np.array([np.cos(theta), np.sin(theta), thetadot])

    def _render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(400, 400)
            vb = 3
            self.viewer.set_bounds(-vb, vb, -vb, vb)
            rod = rendering.make_capsule(1, .2)
            rod.set_color(0.58, 0.3, 0.73)
            self.pole_transform = rendering.Transform()
            rod.add_attr(self.pole_transform)
            self.viewer.add_geom(rod)
            axle = rendering.make_circle(0.05)
            axle.set_color(0.5, 0.95, 0.5)
            self.viewer.add_geom(axle)
            fname = path.join(path.dirname(__file__), "assets/clockwise.png")
            self.img = rendering.Image(fname, 1., 1.)
            self.imgtrans = rendering.Transform()
            self.img.add_attr(self.imgtrans)

        self.viewer.add_onetime(self.img)
        self.pole_transform.set_rotation(self.state[0] + np.pi/2)
        if self.last_u:
            self.imgtrans.scale = (-self.last_u/2, np.abs(self.last_u)/2)

        return self.viewer.render(return_rgb_array = mode=='rgb_array')

# this keeps us from going to crazy angles;
# it wraps back to zero at +/- 2*pi
def angle_normalize(x):
    return (((x + np.pi) % (2*np.pi)) - np.pi)
