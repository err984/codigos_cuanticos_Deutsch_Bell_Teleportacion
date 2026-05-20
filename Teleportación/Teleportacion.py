from qiskit import QuantumCircuit, transpile
from numpy import pi
from qmiotools.integrations.qiskitqmio import QmioBackend


backend=QmioBackend() # loads the last calibration file from the directory $QMIO_CALIBRARTIONS

# Circuito pequeñito solo para preparar el estado final teorico
qc = QuantumCircuit(3,3)

#preparar estado para teletransportar
qc.ry(pi/2,0)
qc.rz(pi/2,0)

qc.barrier(0,1,2)

#Creamos el par de Bell entre q1 y q2
qc.h(1)
qc.cx(1,2)

#Medimos Ball
qc.cx(0,1)
qc.h(0)

#Medimos el qubit a enviar
qc.cx(1,2)
qc.cz(0,2)

#medimos qubit objetivo
qc.barrier(0,1,2)

#Deshacemos rotacion
qc.rz(-pi/2,2)
qc.ry(-pi/2,2)

qc.barrier(0,1,2)

#Medimos
qc.measure([0,1,2],[0,1,2])

#Transpile the circuit using the optimization_level equal to 2
qct=transpile(qc,backend)


#Execute the circuit with 4096 shots. Must be executed from a node with a QPU.
job=backend.run(qct,shots=4096)

#Return the results

print("Job enviado... esperando resultados")

result = job.result()

counts = result.get_counts(qc)
print("Teleportation Counts:", counts)
