from projectq import MainEngine
from projectq.ops import H, Measure, CNOT, All
from projectq.meta import Compute, Uncompute
from projectq.backends import CircuitDrawer

draw_bnd = CircuitDrawer()
eng = MainEngine(draw_bnd)

q0 = eng.allocate_qubit()
q1 = eng.allocate_qubit()

H | q0

with Compute(eng):
    q3 = eng.allocate_qubit()
    H | q1
    CNOT | (q1, q3)

CNOT | (q0, q1)

Uncompute(eng)

All(Measure) | [q0, q1]

eng.flush()

print(int(q0))
print(int(q1))
