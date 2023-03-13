from azure.quantum.qiskit import AzureQuantumProvider
from qiskit.primitives import BackendSampler
provider = AzureQuantumProvider(resource_id="MY_RESOURCE_ID",location="MY_LOCATION")
backend = provider.get_backend("ionq.simulator")
sampler = BackendSampler(backend)

# Build circuit
from qiskit import QuantumCircuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1], [0,1])

# Run the circuit and get result distribution
job = sampler.run(circuit)
quasi_dist = job.result().quasi_dists[0]
print(quasi_dist)