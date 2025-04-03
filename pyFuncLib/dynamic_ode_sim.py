import numpy as np
from scipy.integrate import odeint


def simulate(dyn, x0, dt, N=3):  # simulate one step from given x0
    """
    simulate one step from given x0 using the ODE solver
    -> dyn: function to be simulated (dynamics)
    -> x0: initial state (1D or 2D array)
    -> dt: time step for simulation
    -> N: number of steps to simulate (default: 3)

    <- x1: simulated state after N steps
    """
    if x0.ndim == 1:
        x0 = x0.reshape(1, -1)
    assert x0.ndim == 2

    def ode_fx(x, t):
        x = x.reshape(x0.shape)
        y = dyn(*x.T).squeeze(axis=1).T
        return y.flatten()

    x1 = odeint(ode_fx, x0.flatten(), np.linspace(0, dt, N))[-1].reshape(x0.shape)

    return x1
