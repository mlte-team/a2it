## System Framework: Modeling

This component of the framework considers the quality attributes of machine learning models in the context of the system into which they are integrated.

We decompose modeling considerations into two components:
- System agnostic model qualities. These are qualities of the machine learning model that can be adequately evaluated outside the context of the remainder of the system.
- System dependent model qualities. These are qualities of the machine learning model that cannot be adequately evaluated outside the context of the remainder of the system.

### Algorithm and Model Qualities (General)

**Prediction Accuracy / Error Rate**
- Objective: Assess the ability of the model to perform the task for which it is designed.
- Rationale: Prediction accuracy is self-evident.
- Implementation: See task-appropriate model quality module.

**Fairness**
- Objective: Ensure the model is free of bias.
- Rationale: Biased models result in a degraded user experience for certain sub-populations.
- Implementation: See task-appropriate model quality module.

**Model Size (Static)**
- Objective: Assess the static size of a trained model.
- Rationale: A model’s static size is its size at rest, when it is ready to perform inference. The static size of the model may limit the infrastructure on which it may be deployed. 
- Implementation: Measure the on-disk size of the model static format. The exact implementation may vary based on the development platform and environment available. Examples of potential implementations are provided below.

On UNIX-like systems, use the `du` ("disk usage") command to measure model size:

```bash
# For models stored statically as a single file
$ du --bytes model

# For models stored statically as a directory
$ du --bytes model/*
```

On Windows systems, the Explorer GUI displays file and directory size. Alternatively, use the following commands in a Powershell interpreter to measure model size:

```powershell
# For models stored statically as a single file
Get-Item model | Measure-Object -Property Length -Sum

# For models stored statically as a directory
Get-ChildItem model/ | Measure-Object -Property Length -Sum
```

Programmatically measuring the file size may be the most useful when automating this procedure in an ML pipeline. In Python, use the `os` module to compute model size:

```python
def file_size(path: str) -> int:
    return os.stat(path).st_size
```
	
**Model Size (Dynamic)**
- Objective: Measure the dynamic size of a trained model.
- Rationale: A model’s dynamic size is its size in a serialized form that is appropriate for transport over the network. The dynamic size of the model determines the difficulty (time requirement) of transporting the model. This concern manifests both internally during development of an automated training pipeline as well as externally during deployment. The dynamic size of a model may depend on the choice of serialization format, compression, and encryption, among other factors.
- Implementation: See implementation for _Model Size (Static)_.


### Algorithm and Model Qualities (Training Costs)

**Training Time**
- Objective: Measure the total (wall-clock) time required to train the model.
- Rationale: Training time is a critical constraint on the machine learning pipeline. Long-training times limit the ability of the ML engineer to iterate on the model and make improvements during development. Long-training times also limit the frequency with which new models may be deployed to production. 
- Implementation: The wall-clock time required to train a machine learning model is highly-dependent upon the system on which training occurs. A system with better hardware properties (e.g. CPU cores, clock frequency, cache capacity, RAM capacity) trains faster than a weaker one. Whether or not a GPU is available, and the quality thereof, is another consideration. When the input dataset is large, storage system performance may become the bottleneck. For models that require distributed training, cluster properties confound these measurements. This variability necessitates a common benchmark infrastructure for model training time. TODO

**Training CPU Consumption**
- Objective: Measure the peak and average CPU utilization during model training.
- Rationale: The computational requirements of model training determine the load that it places on the system during the training procedure. Typically, we are not concerned with the efficiency of other jobs that run concurrently on the same machine during model training. Therefore, the peak and average CPU consumption of the training process are primarily relevant because they determine the resource requirements necessary to train efficiently. This metric is not directly applicable to a distributed training procedure.
- Implementation: Measure the CPU consumption of the process running the training procedure. The measurement procedure will vary depending on the training environment.

Measure the CPU utilization of the training procedure with the `mlte` package:

```python
from mlte.monitoring import monitor_cpu

pid = # identifier of training process 

stats = monitor_cpu(pid)
print(stats.min, stats.max, stats.avg)
```

**Training Memory Consumption**
- Objective: Measure the peak and average memory consumption during model training.
- Rationale: The memory requirements of model training determine the load that is places on the system during the training procedure. Typically, we are not concerned with the efficiency of other jobs that run concurrently on the same machine during model training. Therefore, the peak and average memory consumption of the training process are primarily relevant because they determine the resource requirements necessary to train efficiently.  This metric is not directly applicable to a distributed training procedure.
- Implementation: Measure the memory consumption of the process running the training procedure. The measurement procedure will vary depending on the training environment.

Measure the memory consumption of the training procedure with the `mlte` package:

```python
from mlte.monitoring import monitor_memory

pid = #  identifier of training process

stats = monitor_memory(pid)
print(stats.min, stats.max, stats.avg)
```

**Training Data Requirements**
- Objective:
- Rationale:
- Implementation:

### Algorithm and Model Qualities (Inference Costs)

Inference Latency
- Objective:
- Rationale:
- Implementation:

Inference Throughput
- Objective:
- Rationale:
- Implementation:

Inference CPU Consumption
- Objective:
- Rationale:
- Implementation:

Inference Memory Consumption
- Objective:
- Rationale:
- Implementation:

### Algorithm and Model Qualities (Scalability)

Notes:
- Is it really realistic to talk about system-agnostic model qualities? Doesn’t every model quality ultimately depend on the system in which it is integrated, or should at least be informed by it?
- I feel like Christian would not like this distinction…
- Privacy (?)
- Security (?)

Resources:
- Quality Attributes of ML Components
