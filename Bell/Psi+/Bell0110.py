from qiskit import QuantumCircuit, transpile
from qmiotools.integrations.qiskitqmio import QmioBackend


backend=QmioBackend() # loads the last calibration file from the directory $QMIO_CALIBRARTIONS

# Circuito pequeñito solo para preparar el estado final teorico
qc = QuantumCircuit(2)

#Creo superposicion en q0
qc.h(0)

#Estado entrelazado de Bell phi+
qc.cx(0,1)

#Cambiamos el estado de q1 para crear psi+
qc.x(1)

#Mediciones
qc.measure_all()
qc.draw()

#Transpile the circuit
qct=transpile(qc,backend)
