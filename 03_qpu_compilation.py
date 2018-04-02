from pyquil.api import CompilerConnection, QVMConnection, get_devices
from pyquil.quil import Program
from pyquil.gates import H, X, CNOT

devices = get_devices(as_dict=True)
print(devices)

acorn = devices['19Q-Acorn']
compiler = CompilerConnection(acorn)

prog = Program()
prog.inst(H(0))
prog.inst(H(2))
prog.inst(CNOT(0,1))
prog.inst(CNOT(1,2))

job_id = compiler.compile_async(prog)
job = compiler.wait_for_job(job_id)

print('program fidelity', job.program_fidelity())
