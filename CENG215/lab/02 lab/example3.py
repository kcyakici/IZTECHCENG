from PySpice.Unit import *
from PySpice.Spice.Netlist import Circuit

circuit = Circuit("circuit 1")

V1 = circuit.V("input1", "a", circuit.gnd, 28@u_V)
V2 = circuit.V("input2", "e", circuit.gnd, 32@u_V)
R1 = circuit.R("1", "a", "c", 8@u_Ohm)
R2 = circuit.R("2", "a", "b", 6@u_Ohm)
R3 = circuit.R("3", "c", "b", 5@u_Ohm)
R4 = circuit.R("4", "e", "c", 12@u_Ohm)
R5 = circuit.R("5", "b", circuit.gnd, 2@u_Ohm)

for resistance in (circuit.R1, circuit.R2, circuit.R3, circuit.R4, circuit.R5):
    resistance.plus.add_current_probe(circuit)

simulator = circuit.simulator(temperature=25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f"Node: {str(node)} Value: {float(node):4.3} V")

for node in analysis.branches.values():
    print(f"Node: {str(node)} Value: {float(node):4.3} A")

