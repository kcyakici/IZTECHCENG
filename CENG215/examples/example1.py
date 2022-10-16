from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

def print_voltage(analysis):

    for node in analysis.nodes.values():
        print((f"Node {str(node)}: {float(node)} V"))

def print_current(analysis):

    for node in analysis.branches.values():
        print((f"Branch {str(node)}: {float(node)} A")) 

circuit = Circuit("Circuit 1")

# print(circuit) # prints the title of the circuit

V = circuit.V("input", "a", circuit.gnd, 5@u_V) # refers to the voltage source
R = circuit.R(1, "a", circuit.gnd, 1@u_kOhm) # means it is connected to positive, ground is connected to ground

print(V)
print(R)

simulator = circuit.simulator(temperature=25)
analysis = simulator.operating_point() # simulates the circuit
# analysis = simulator.dc() # simulates the circuit, needs range of voltage
# analysis = simulator.transient() # simulates the circuit, needs frequency range

for node in analysis.nodes.values():
    print((f"Node {str(node)}: {float(node):4.3} V"))

for node in analysis.branches.values():
    print((f"Branch {str(node)}: {float(node):4.6} A"))    