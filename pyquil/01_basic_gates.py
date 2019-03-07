from pyquil.api import QVMConnection
from pyquil import Program, get_qc
from pyquil.gates import H, X, CNOT

qvm = get_qc('2q-qvm')

p = Program()
out = p.declare('ro', 'BIT', 2)

p.inst(H(0))

p.inst(CNOT(0,1))

p.measure(0,out[0])

exe = qvm.compile(p)
res = qvm.run(exe)

print(res)
