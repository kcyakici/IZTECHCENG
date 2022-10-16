from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *
import matplotlib.pyplot as plt

circuit = Circuit("Circuit 1")

# print(circuit) # prints the title of the circuit

V = circuit.SinusoidalVoltageSource("input", "a", circuit.gnd, amplitude=2@u_V, frequency=50@u_Hz) # refers to the voltage source
R1 = circuit.R(1, "a", "b", 1@u_kOhm) # means it is connected to positive, ground is connected to ground
R2 = circuit.R(2, "b", "c", 2@u_kOhm) # means it is connected to positive, ground is connected to ground
R3 = circuit.R(3, "c", circuit.gnd, 1@u_kOhm) # means it is connected to positive, ground is connected to ground
R4 = circuit.R(4, "a", circuit.gnd, 5@u_kOhm) # means it is connected to positive, ground is connected to ground

circuit.R1.plus.add_current_probe(circuit)
circuit.R4.plus.add_current_probe(circuit)

simulator = circuit.simulator(temperature=25)
analysis = simulator.transient(step_time = 100@u_us, end_time = 40@u_ms) # simulates the circuit, needs frequency range

figure, ax = plt.subplots(figsize=(10, 5))
ax.grid()
ax.plot(analysis["a"])
ax.plot(analysis["b"])
ax.plot(analysis["c"])
plt.show()
