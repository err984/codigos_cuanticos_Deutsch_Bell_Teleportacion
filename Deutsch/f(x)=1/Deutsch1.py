from qiskit import QuantumCircuit, transpile

backend=QmioBackend() # loads the last calibration file from the directory $QMIO_CALIBRARTIONS

# Circuito
qc = QuantumCircuit(2)

#Preparar el estado inicial (qubit 1 en |1>)
qc.x(1) 

# Aplicar barrera y puertas Hadamard para crear superposicion
qc.barrier()  
qc.h(0)
qc.h(1)

#El "Oraculo" f(x)=1
qc.x(1) 

#Generamos interferencia
qc.barrier()
qc.h(0)

#Medimos
qc.measure_all()
qc.draw()

#Transpile the circuit using the optimization_level equal to 2
qct=transpile(qc,backend)

#Execute the circuit with 4096 shots. Must be executed from a node with a QPU.
job=backend.run(qct,shots=4096)

#Return the results
print("Job enviado... esperando resultados")

result = job.result()

counts = result.get_counts(qc)
print("QmioBackend Counts:", counts)
