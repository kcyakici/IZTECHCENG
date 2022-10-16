from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

circuit = Circuit("Circuit 1")

V = circuit.V("input", "c", circuit.gnd, 5@u_V)
R1 = circuit.R("R1", "c", "b", 1@u_kOhm)
R2 = circuit.R("R2", "b", "a", 1@u_kOhm)
R3 = circuit.R("R3", "a", circuit.gnd, 1@u_kOhm)

simulator = circuit.simulator(temperature=25)
analysis = simulator.operating_point()

for node in analysis.nodes.values():
    print(f"Node: {str(node)} Value: {float(node):4.3} V")

for node in analysis.branches.values():
    print(f"Branch: {str(node)} Value: {float(node):4.6} A")