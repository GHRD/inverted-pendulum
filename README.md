# inverted-pendulum
Simulation of an inverted pendulum controlled by sliding mode control (SMC). It defines two classes, "InvertedPendulum" and "SlidingModeControl". 


The code is an implementation of a simulation for an inverted pendulum using sliding mode control (SMC).

It starts by importing the required libraries: matplotlib.pyplot for plotting and numpy for numerical operations.

Then, it defines two classes: InvertedPendulum and SlidingModeControl.

The InvertedPendulum class is responsible for representing an inverted pendulum with a certain mass, length and gravity. The class has attributes mass, length, gravity, theta (the angle between the pendulum and the vertical axis), and omega (the angular velocity). The update method updates the omega and theta given a control input u and a time step dt.

The SlidingModeControl class represents a sliding mode controller. It has attributes k and alpha. The update method updates the control input u given the error between the setpoint and the current state, the current angular velocity, and a time step dt. The control input u is calculated based on the sliding surface s, which is defined as s = alpha * error - omega.

Finally, the code defines a main function that creates an instance of the InvertedPendulum class, sets the setpoint to 0, creates an instance of the SlidingModeControl class, and then runs a loop for 100 time steps (10 seconds). At each time step, the error between the setpoint and the current angular velocity is calculated and used to update the control input. Then, the control input is used to update the pendulum. The angular velocity at each time step is recorded and saved to a list. After the loop, the angular velocity over time is plotted using matplotlib.pyplot and saved as an .svg file.
