import json

def dump_json_files():

    code= {}

    code['bell'] = """# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Run the circuit and get result distribution
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
print(quasi_dist)
""".splitlines()

    code['vqe'] = """# Create H2 molecule 
from qiskit.quantum_info import SparsePauliOp

H2_op = SparsePauliOp.from_list([
    ("II", -1.052373245772859),
    ("IZ", 0.39793742484318045),
    ("ZI", -0.39793742484318045),
    ("ZZ", -0.01128010425623538),
    ("XX", 0.18093119978423156)
])

# Calculate ground state energy using VQE
from qiskit.circuit.library import TwoLocal
from qiskit.algorithms.optimizers import SLSQP
from qiskit.algorithms.minimum_eigensolvers import VQE

ansatz = TwoLocal(2, "ry", "cz")
optimizer = SLSQP(maxiter=1000)
vqe = VQE(estimator, ansatz, optimizer)
result = vqe.compute_minimum_eigenvalue(operator=H2_op)
print(result.eigenvalue)
""".splitlines()

    with open("algorithms.json", "w") as f:
        json.dump(code, f, sort_keys=True, indent=4)


if __name__ == '__main__':
    dump_json_files()