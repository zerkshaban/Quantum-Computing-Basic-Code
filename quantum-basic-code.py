%matplotlib inline
# Importing standard Qiskit libraries and configuring account
from qiskit import QuantumCircuit, execute, Aer, IBMQ
from qiskit.compiler import transpile, assemble
from qiskit.tools.jupyter import *
from qiskit.visualization import *
# Loading your IBM Q account(s)
provider = IBMQ.load_account()
from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit, execute, Aer
import numpy as np
import math as m
S_simulator = Aer.backends(name='statevector_simulator')[0]
M_simulator = Aer.backends(name='qasm_simulator')[0]

q = QuantumRegister(1)
test_qubit = QuantumCircuit(q)
# Got a minus/zero vector by default.
# q6_0: |0>
test_qubit.iden(q[0])
# Applying identity matrix on zero vector.
#          ┌────┐
# q6_0: |0>┤ Id ├
#          └────┘
# Passing the circuit that we want to execute that is Identy gate on zero vector.
# Parameter#1 The circuit that is identity vector applied on zero vector.
# Parameter#2 statevector_simulator

# Applying x gate on zero vector.
#           ┌───┐
# q10_0: |0>┤ X ├
#           └───┘
# Passing the circuit that we want to execute that is Identy gate on zero vector.
# Parameter#1 The circuit that is X vector applied on zero vector.
# Parameter#2 statevector_simulator

# Applying Y gate on zero vector.
#           ┌───┐
# q15_0: |0>┤ Y ├
#           └───┘
# Passing the circuit that we want to execute that is Identy gate on zero vector.
# Parameter#1 The circuit that is Y vector applied on zero vector.
# Parameter#2 statevector_simulator
job = execute(test_qubit, S_simulator)
result = job.result()
# Following is the reposne that we will get on running the command
# Result(backend_name='statevector_simulator', backend_version='0.4.1',
#      date=datetime.datetime(2020, 3, 20, 12, 27, 31, 575995),
#      header=Obj(backend_name='statevector_simulator', backend_version='0.4.1'),
#      job_id='956cdf59-ffdc-4385-a208-9033c89f331c', metadata={'max_memory_mb': 16081,
#      'omp_enabled': True, 'parallel_experiments': 1, 'time_taken': 0.000132988},
#      qobj_id='cd81a242-f88c-4845-87ae-8534dd73e8b1', results=
#      [ExperimentResult(data=ExperimentResultData(statevector=array([1.+0.j, 0.+0.j])),
#      header=Obj(clbit_labels=[], creg_sizes=[], memory_slots=0, n_qubits=1, name='circuit17',
#      qreg_sizes=[['q9', 1]], qubit_labels=[['q9', 0]]), meas_level=<MeasLevel.CLASSIFIED: 2>,
#      metadata={'parallel_shots': 1, 'parallel_state_update': 8}, seed_simulator=1975505491, shots=1,
#      status='DONE', success=True, time_taken=6.3988e-05)],
#      status='COMPLETED', success=True, time_taken=0.0022821426391601562)

# Following is the reposne that we will get on running the command
# Result(backend_name='statevector_simulator', backend_version='0.4.1',
#     date=datetime.datetime(2020, 3, 20, 13, 2, 31, 918120),
#     header=Obj(backend_name='statevector_simulator', backend_version='0.4.1'),
#     job_id='4dcd8a6f-76c1-4183-939b-72166ad86d96', metadata={'max_memory_mb': 16081,
#     'omp_enabled': True, 'parallel_experiments': 1, 'time_taken': 0.000139388},
#     qobj_id='976216bc-6e10-4f26-8d5f-a86c63b51b39', results=[ExperimentResult
#     (data=ExperimentResultData(statevector=array([0.+0.j, 1.+0.j])),
#     header=Obj(clbit_labels=[], creg_sizes=[], memory_slots=0, n_qubits=1, name='circuit21',
#     qreg_sizes=[['q11', 1]], qubit_labels=[['q11', 0]]), meas_level=<MeasLevel.CLASSIFIED: 2>,
#     metadata={'parallel_shots': 1, 'parallel_state_update': 8}, seed_simulator=934961638, shots=1,
#     status='DONE', success=True, time_taken=6.9183e-05)], status='COMPLETED', success=True,
#     time_taken=0.0023148059844970703)

# Following is the reposne that we will get on running the command
#     Result(backend_name='statevector_simulator', backend_version='0.4.1', date=datetime.datetime
#     (2020, 3, 20, 13, 28, 18, 130506), header=Obj(backend_name='statevector_simulator',
#     backend_version='0.4.1'), job_id='212dcc53-73cf-4300-a6da-1a8c74ccb1aa', metadata=
#     {'max_memory_mb': 16081, 'omp_enabled': True, 'parallel_experiments': 1, 'time_taken': 0.000131965},
#     qobj_id='b1be8783-a487-48b8-bb39-b4c2f057829e', results=[ExperimentResult
#     (data=ExperimentResultData(statevector=array([0.-0.j, 0.+1.j])), header=Obj(clbit_labels=[],
#     creg_sizes=[], memory_slots=0, n_qubits=1, name='circuit29', qreg_sizes=[['q15', 1]],
#     qubit_labels=[['q15', 0]]), meas_level=<MeasLevel.CLASSIFIED: 2>, metadata=
#     {'parallel_shots': 1, 'parallel_state_update': 8}, seed_simulator=1207216432, shots=1, status='DONE',
#     success=True, time_taken=6.530900000000001e-05)], status='COMPLETED', success=True,
#     time_taken=0.002366781234741211)

# Iden Gate Result
# result.get_statevector()
# array([1.+0.j, 0.+0.j]) Is the result on excuting the circuit.

# X-Gate Result
# result.get_statevector()
# array([0.+0.j, 1.+0.j]) Is the result on excuting the circuit.

# Y-Gate Result
# result.get_statevector()
# array([0.+0.j, 0.+1.j]) Is the result on excuting the circuit.
