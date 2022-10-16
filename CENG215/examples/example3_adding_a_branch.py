from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("Circuit 1")

# print(circuit) # prints the title of the circuit

V = circuit.V("input", "a", circuit.gnd, 5@u_V) # refers to the voltage source
R1 = circuit.R(1, "a", "b", 1@u_kOhm) # means it is connected to positive, ground is connected to ground
R2 = circuit.R(2, "b", "c", 2@u_kOhm) # means it is connected to positive, ground is connected to ground
R3 = circuit.R(3, "c", circuit.gnd, 1@u_kOhm) # means it is connected to positive, ground is connected to ground
R4 = circuit.R(4, "a", circuit.gnd, 5@u_kOhm) # means it is connected to positive, ground is connected to ground

circuit.R1.plus.add_current_probe(circuit)
circuit.R2.plus.add_current_probe(circuit) # we expect the same current flowing through
circuit.R3.plus.add_current_probe(circuit) # we expect the same current flowing through
circuit.R4.plus.add_current_probe(circuit)

simulator = circuit.simulator(temperature=25)
analysis = simulator.operating_point() # simulates the circuit
# analysis = simulator.dc() # simulates the circuit, needs range of voltage
# analysis = simulator.transient() # simulates the circuit, needs frequency range

for node in analysis.nodes.values():
    print((f"Node {str(node)}: {float(node):4.3} V"))

for node in analysis.branches.values():
    print((f"Branch {str(node)}: {float(node):4.6} A"))