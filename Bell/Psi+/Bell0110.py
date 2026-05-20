#Creo superposicion en q0
qc.h(0)

#Estado entrelazado de Bell phi+
qc.cx(0,1)

q.z(0)

#Mediciones
qc.measure_all()
qc.draw()

#Transpile the circuit
qct=transpile(qc,backend)
