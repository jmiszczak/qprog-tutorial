from pyquil.api import QVMConnection
from pyquil.quil import Program
from pyquil.gates import H, X, CNOT

qvm = QVMConnection() # use the simulator
cregs = [0, 1, 2] # three classical registers

# add instructions to the program
prog = Program()
prog.inst(H(0))
prog.inst(CNOT(0,1))

# run/simulate
print("Before the measurement")
qres = qvm.wavefunction(prog)
print(qres)

prog.measure(0,0)
prog.measure(1,1)

print("After the measurement")
qres = qvm.wavefunction(prog)
print(qres)

print("Result of the measurement")
cres = qvm.run(prog, cregs)
print(cres)
