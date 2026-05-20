from qiskit import QuantumCircuit, transpile
from qmiotools.integrations.qiskitqmio import QmioBackend


backend=QmioBackend() # loads the last calibration file from the directory $QMIO_CALIBRARTIONS

# Circuito pequeñito solo para preparar el estado final teorico
qc = QuantumCircuit(2)

#Creo superposicion en q0
qc.h(0)

#Estado entrelazado de Bell phi+
qc.cx(0,1)

#Cambiamos fase en q0 para crear phi-
qc.z(0)

#Cambiamos el estado de q1 para crear psi-
qc.x(1)

#Mediciones
qc.measure_all()
qc.draw()

#Transpile the circuit
qct=transpile(qc,backend)

#Execute the circuit with 4096 shots. Must be executed from a node with a QPU.
job=backend.run(qct,shots=4096)

#Return the results
print("Job enviado... esperando resultados")

result = job.result()

counts = result.get_counts(qc)
print("QmioBackend Counts:", counts)
