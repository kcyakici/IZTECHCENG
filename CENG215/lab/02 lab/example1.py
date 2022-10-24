from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("Circuit1")

V = circuit.V("input", "a", circuit.gnd, 50@u_V)
I = circuit.I("input", circuit.gnd, "b", 3@u_A)
R1 = circuit.R(1, "a", "b", 12@u_Ohm)
R2 = circuit.R(2, "b", "c", 2@u_Ohm)
R3 = circuit.R(3, "a", "c", 10@u_Ohm)
R4 = circuit.R(4, "c", circuit.gnd, 5@u_Ohm)

for resistance in (circuit.R1, circuit.R2, circuit.R3, circuit.R4):
    resistance.minus.add_current_probe(circuit) # to get positive value

simulator = circuit.simulator(temperature = 25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f"Node: {str(node)} Values: {float(node):4.3} V")

for node in analysis.branches.values():
    print(f"Branch: {str(node)} Values: {float(node):4.6} A")
