from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("Circuit1")

I1 = circuit.I("input1", circuit.gnd, "a", 12@u_V)
I2 = circuit.I("input2", "d", "c", 3@u_A)
R1 = circuit.R(1, "a", "d", 5@u_Ohm)
R2 = circuit.R(2, "a", "b", 2@u_Ohm)
R3 = circuit.R(3, "b", circuit.gnd, 3@u_Ohm)
R4 = circuit.R(4, "c", circuit.gnd, 20@u_Ohm)
R5 = circuit.R(5, "b", "c", 10@u_Ohm)

for resistance in (circuit.R1, circuit.R2, circuit.R3, circuit.R4, circuit.R5):
    resistance.minus.add_current_probe(circuit) # to get positive value

simulator = circuit.simulator(temperature = 25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f"Node: {str(node)} Values: {float(node):4.3} V")

for node in analysis.branches.values():
    print(f"Branch: {str(node)} Values: {float(node):4.6} A")
