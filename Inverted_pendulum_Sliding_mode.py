import matplotlib.pyplot as plt
import numpy as np

class InvertedPendulum:
    def __init__(self, mass, length, gravity):
        self.mass = mass
        self.length = length
        self.gravity = gravity
        self.theta = 0
        self.omega = 0

    def update(self, u, dt):
        # update angular velocity
        self.omega += (-3 * self.gravity / (2 * self.length) * np.sin(self.theta + np.pi) + 3. / (self.mass * self.length ** 2) * u) * dt
        # update angle
        self.theta += self.omega * dt

class SlidingModeControl:
    def __init__(self, k, alpha):
        self.k = k
        self.alpha = alpha

    def update(self, error, omega, dt):
        # calculate sliding surface
        s = self.alpha * error - omega
        # calculate control input
        u = self.k * np.sign(s)
        return u

if __name__ == '__main__':
    # create an inverted pendulum
    pendulum = InvertedPendulum(mass=3, length=1.5, gravity=9.8)
    # create a sliding mode controller
    smc = SlidingModeControl(k=1, alpha=0.1)
    # set the setpoint
    setpoint = 0
    # initialize time and angular velocity
    t = 0
    omega_list = []
    time_list = []
    # loop for 10 seconds
    while t <= 100:
        # get the error
        error = setpoint - pendulum.omega
        # update the control input
        u = smc.update(error, pendulum.omega, dt=0.01)
        # update the pendulum
        pendulum.update(u, dt=0.01)
        # append the angular velocity to the list
        omega_list.append(pendulum.omega)
        time_list.append(t)
        # increment time
        t += 0.01

    # plot the angular velocity
    plt.plot(time_list, omega_list)
    plt.xlabel('Time (s)')
    plt.ylabel('Angular Velocity (rad/s)')
    plt.savefig("inverted_pendulum_sliding_mode_control.svg")
    plt.show()
