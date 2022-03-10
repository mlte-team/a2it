# System Dependent Model Testing
### Objective and Rationale
Machine learning models and the systems into which they are integrated must be functional in their desired context, as well as robust to an array of potential circumstances.  
This section lists properties that should be considered for model and system requirements and how those are prioritized, including weighing tradeoffs ([Ribeiro et al. 2020](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf)). We recommend selecting the subset of these properties that are most relevant for your application. Ensure that you track the values of the metrics associated with these properties; we recommend existing experiment tracking services such as [MlFlow Tracking](https://mlflow.org/docs/latest/tracking.html) or [Weights and Biases Experiments](https://wandb.ai/site/experiment-tracking). 

## System Dependent Model Testing (SDMT) Properties

**Structure**

The properties are organized into four categoris: 
- Functionality
- Robustness
- Costs
- Scalability   

Each of the properties is organized as follows:
- Objective: A brief, one-sentence summary of the property in question.
- Metric: How the property is measured.
- Rationale: The reason that the property is included in this enumeration; why it may be an important consideration for your project. 
- Implementation: Proposals for methods by which you might evaluate the metric in your system.

### Functionality

**Prediction Accuracy / Error Rate**
- Objective: Assess the ability of the model to perform the task for which it is designed.
- Metric: See task-appropriate model quality module.
- Rationale: Prediction accuracy is self-evident.
- Implementation: See task-appropriate model quality module.

**Fairness**
- Objective: Data and models should be free of bias to avoid unfair treatment of certain groups, to ensure a fair distribution of benefits and costs, and to offer those affected an opportunity to seek redress against adverse decisions made by the system or the humans operating it ([Chouldechova & Roth 2018](https://arxiv.org/pdf/1810.08810.pdf)). 
- Metric: Statistical metrics of fairness include raw positive classification rate ([Feldman et al. 2015](https://arxiv.org/pdf/1412.3756v3.pdf)), false positive and false negative rates, or positive predictive value ([Chouldechova 2017](https://arxiv.org/pdf/1703.00056.pdf)). However, every fairness metric includes tradeoffs, so if this is important to the system then the model and system teams must have a conversation about the overall effects and the appropriate tradeoffs to ensure fairness.
- Rationale: Biased models result in a degraded user experience for certain sub-populations, and can damage user trust in a system.
- Implementation: Dependent on the chosen metric or tradeoff; see references section at the bottom of this page for more resources on fairness.

**Interpretability**
- Objective: Some systems necessitate an ability to be explained or presented in understandable terms to a human ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)). 
- Metric: Interpretability is difficult to measure; it can be considered from an end-user perspective or from a developer perspective by observing and evaluating the interactions of these teams with the system, or having a domain expert explain model outputs in context ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)).
- Rationale: Depending on the system purpose, it may be critical for the system to be explanable and understandable.
- Implementation: Options include, among others: intrinsic interpretability in which a model is self explanatory, and post-hoc interpretability where another model is created to explain outputs from the first ([Du et al. 2019](https://arxiv.org/pdf/1808.00033.pdf)).

### Robustness

**Robustness to Naturally Occuring Data Challenges**
- Objective: Ensure that the model is robust to naturally occuring data challenges that it will encounter in the ambient conditions of the system ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).
- Metric: 
- Rationale: Models implemented to a system will experience common data challenges like illumination, motion blue, occlusion, changes in perspective, and weather impacts. These peturbations affect the data and can have significant impacts on the quality of the model prediction which must be addressed before deployment. ([Russell & Norivg](http://aima.cs.berkeley.edu))
- Implementation: Dependent on the identified data challenges; see references section at the bottom of this page for more resources on this type of robustness

**Robustness to Adversarial Attack**
- Objective: Ensure that the model is robust to sythentic manipulation or targeted adversarial attacks ([Hendrycks et al.](https://arxiv.org/pdf/2109.13916.pdf)).
- Metric: 
- Rationale: 
- Implementation: Dependent on the identified adversary MLCO and MDCOA; see references section at the bottom of this page for more resources on this type of robustness

### Costs

**Model Size (Static)**
- Objective: Measure the static size of a trained model.
- Metric: The storage requirement for the model in bytes or some multiple thereof (e.g. kilobytes, megabytes, etc.). This metric is absolute.
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

Programmatically measuring the file size may be the most useful when automating this procedure in an ML pipeline. The `mlte` package provides functionality for measuring the size of models stored on the local filesystem:

```python
from mlte.measurement import model_size

path = # the path to model on local filesystem
size = model_size(path)
print(size)
```
	
**Model Size (Dynamic)**
- Objective: Measure the dynamic size of a trained model in terms of its storage requirements.
- Metric: The storage requirement for the model in bytes or some multiple thereof (e.g. kilobytes, megabytes, etc.). This metric is absolute.
- Rationale: A model’s dynamic size is its size in a serialized form that is appropriate for transport (e.g. via removable media, or over the network). The dynamic size of the model determines the difficulty (time requirement) of transporting the model. This concern manifests both internally during development of an automated training pipeline as well as externally during deployment. The dynamic size of a model may depend on the choice of serialization format, compression, and encryption, among other factors.
- Implementation: See implementation for _Model Size (Static)_.

**Training Time**
- Objective: Measure the total time required to train the model.
- Metric: The wall-clock time required to run the model training process in seconds or some multiple thereof (e.g. minutes, hours, etc.). This metric is relative.
- Rationale: Training time is a critical constraint on the machine learning pipeline. Long-training times limit the ability of the ML engineer to iterate on the model and make improvements during development. Long-training times also limit the frequency with which new models may be deployed to production. 
- Implementation: The wall-clock time required to train a machine learning model is highly-dependent upon the system on which training occurs. A system with better hardware properties (e.g. CPU cores, clock frequency, cache capacity, RAM capacity) trains faster than a weaker one. Whether or not a GPU is available, and the quality thereof, is another consideration. When the input dataset is large, storage system performance may become the bottleneck. For models that require distributed training, cluster properties confound these measurements. This variability necessitates a common benchmark infrastructure for model training time.

**Training CPU Consumption**
- Objective: Measure the peak and average CPU utilization during model training. 
- Metric: The percentage of compute resources utilized by the training process as a percentage of the total compute available to the system on which it is evaluated. This metric is _relative_.
- Rationale: The computational requirements of model training determine the load that it places on the system during the training procedure. Typically, we are not concerned with the efficiency of other jobs that run concurrently on the same machine during model training. Therefore, the peak and average CPU consumption of the training process are primarily relevant because they determine the resource requirements necessary to train efficiently. This metric is not directly applicable to a distributed training procedure.
- Implementation: Measure the CPU utilization of the process running the training procedure. The measurement procedure will vary depending on the training environment.

Measure the CPU utilization of the training procedure with the `mlte` package:

```python
from mlte.monitoring import cpu_utilization

pid = # identifier of training process 

stats = cpu_utilization(pid)
print(stats)
```

**Training Memory Consumption**
- Objective: Measure the peak and average memory consumption during model training.
- Metric: The volume of memory consumed in bytes or some multiple thereof (kilobytes, megabytes, etc.). This metric is absolute. 
- Rationale: The memory requirements of model training determine the load that is places on the system during the training procedure. Typically, we are not concerned with the efficiency of other jobs that run concurrently on the same machine during model training. Therefore, the peak and average memory consumption of the training process are primarily relevant because they determine the resource requirements necessary to train efficiently.  This metric is not directly applicable to a distributed training procedure.
- Implementation: Measure the memory consumption of the process running the training procedure. The measurement procedure will vary depending on the training environment.

Measure the memory consumption of the training procedure with the `mlte` package:

```python
from mlte.monitoring import memory_consumption

pid = #  identifier of training process

stats = memory_consumption(pid)
print(stats)
```

TODO(Kyle): Write a more accurate wrapper with a simple heap profiler.

**Training Energy Consumption**
- Objective: Measure the energy consumption of the model training process.
- Metric: The energy consumed by the training process in joules (total power consumption over a time interval).
- Rationale: For large-scale machine learning applications, energy consumption may be a major driver in the total cost of development and maintenance. The model training process is frequently the most energy-intensive stage of the machine learning pipeline.
- Implementation: Energy consumption and power requirements are a relatively-new consideration in the field of machine learning. Accordingly, methods for convenient and accurate measurement are limited.

TODO(Kyle): Baseline energy measurements with PMC.

**Inference Latency (Mean)**
- Objective: Measure the mean inference latency of a trained model.
- Metric: The time required to complete a single inference request, in milliseconds. This metric is relative.
- Rationale: Inference latency refers to the time required for a trained model to make a single prediction given some input data. While the machine learning model is likely only a small part of the intelligent system in which it is integrated, it may contribute substantially to the overall latency of the service.
- Implementation: Measure the latency of the model across many inference requests and compute the mean. The measurement procedure will vary based on the development environment.

Measure the mean latency of model inference with the `mlte` package:

```python
from mlte.measurement import mean_latency

model = # trained model that implements __call__()
d_gen = # input generator that implements __call__()

latency = mean_latency(model, d_gen)
print(f"Mean latency: {latency}ms")
```

**Inference Latency (Tail)**
- Objective: Measure the tail inference latency of a trained model.
- Metric: The time required to complete a single inference request, in milliseconds. This metric is relative.
- Rationale: Tail latency refers to the latency of model inference at the (right) tail of the latency distribution. In many production environments, mean latency does not adequately reflect the production viability of model in terms of its runtime requirements. Instead, tail latency provides a more informative measure of the guarantees we can provide about model runtime performance.
- Implementation: Measure the latency of the model across many inference requests and compute the desired tail percentile. The measurement procedure will vary based on the development environment.

Measure the tail latency of model inference with the `mlte` package. By default, the `tail_latency()` function computes the 99th percentile latency, but this value may be changed via a keyword argument.

```python
from mlte.measurement import tail_latency

model = # trained model that implements __call__()
d_gen = # input generator that implements __call__()

latency = tail_latency(model, d_gen)
print(f"Tail latency: {latency}ms")
```

**Inference Throughput**
- Objective: Measure the inference throughput of a trained model.
- Metric: The number of inference requests completed in one second. This metric is relative.
- Rationale: For some applications, service throughput is a more important metric than service latency. In such cases, we may be unconcerned with the latency of inference requests to the model and more concerned with its throughput.
- Implementation: Measure the throughput of the model by providing it with a stream of many inference requests, computing the time required to complete all of these requests, and dividing the number of completed requests by this duration. The measurement procedure will vary based on the 

Measure the throughput of model inference with the `mlte` package.

```python
from mlte.measurement import throughput

model = # trained model that implements __call__()
d_gen = # input generator that implements __call__()

t_put = throughput(model, d_gen)
print(f"Throughput: {t_put} requests per second")
```

**Inference CPU Consumption**
- Objective: Measure the peak and average CPU utilization during model inference.
- Metric: The percentage of compute resources utilized by the inference service as a percentage of the total compute available to the system on which it is evaluated. This metric is relative.
- Rationale: The computational requirements of model inference determine the load that it places on the system when performing inference. This is a key determinant in the compute resources required for model deployment. For example, a model for which inference is computationally inexpensive may be deployed to an instance with relatively light computational resources. This might allow for investment in other resources, such as memory capacity, for the instance to which the model is deployed.
- Implementation: Measure the CPU utilization of the inference service. The setup for inference measurement may be more involved than training measurement because inference is often not run as a standalone process. 

TODO(Kyle): How to measure CPU utilization in inference-relevant environment?

**Inference Memory Consumption**
- Objective: Measure the peak and average memory consumption during model inference.
- Metric: The volume of memory consumed in bytes or some multiple thereof (kilobytes, megabytes, etc.). This metric is absolute. 
- Rationale: The memory requirements of model inference determine the load that is places on the system during inference. This is a key determinant in the memory resources required for model deployment. For example, a model for which inference is not memory-intensive may be deployed to an instance with relatively light memory resources. This might allow for investment in other resources, such as core count, for the instance to which the model is deployed. 
- Implementation: Measure the memory consumption of the process during the inference procedure.

TODO(Kyle): How to measure memory consumption in inference-relevant environment?

**Inference Energy Consumption**
- Objective: Measure the energy consumption of the model inference process.
- Metric: The energy consumed by the inference process in joules (total power consumption over a time interval).
- Rationale: For large-scale machine learning applications, energy consumption may be a major driver in the total cost of development and maintenance.
- Implementation: Energy consumption and power requirements are a relatively-new consideration in the field of machine learning. Accordingly, methods for convenient and accurate measurement are limited.

TODO(Kyle): Baseline energy measurements with PMC.

### Scalability

TODO:
- Model size as a function of data size
- Training time as a function of data size
- Training cost (CPU, memory) as a function of data size

### References

Requirement Selection
- [Requirements Engineering for Machine Learning](https://arxiv.org/pdf/1908.04674.pdf)
- [Towards Guidelines for Assessing Qualities of Machine Learning Systems](https://arxiv.org/ftp/arxiv/papers/2008/2008.11007.pdf)

Model Property Definition
- [Model Quality: Defining Correctness and Fit](https://ckaestne.medium.com/model-quality-defining-correctness-and-fit-a8361b857df)
- [Model Quality: Measuring Prediction Accuracy](https://ckaestne.medium.com/model-quality-measuring-prediction-accuracy-38826216ebcb)
- [Model Quality: Slicing, Capabilities, Invariant, and Other Testing Strategies](https://ckaestne.medium.com/model-quality-slicing-capabilities-invariants-and-other-testing-strategies-27e456027bd)
- [Quality Attributes of ML Components](https://ckaestne.medium.com/quality-drivers-in-architectures-for-ml-enabled-systems-836f21c44334)
- [The Tail at Scale](https://research.google/pubs/pub40801/)
- [Estimation of Energy Consumption in Machine Learning](https://www.sciencedirect.com/science/article/pii/S0743731518308773)

Fairness  
- Metrics of statistical fairness: [Certifying and Removing Disparate Impact](https://arxiv.org/pdf/1412.3756v3.pdf) and [Fair Prediction with Disparate Impact](https://arxiv.org/pdf/1703.00056.pdf)
- Tradeoffs of individual versus statistical fairness: [The Frontiers of Fairness in Machine Learning](https://arxiv.org/pdf/1810.08810.pdf) 
- Testing/measuring individual fairness: [On Formalizing Fairness in Prediction with Machine Learning](https://arxiv.org/pdf/1710.03184.pdf)
- How to consider the dynamic effects of decisions on a system: [Downstream Effects of Affirmative Action](https://arxiv.org/pdf/1808.09004.pdf) and [Delayed Impact of Fair Machine Learning](http://proceedings.mlr.press/v80/liu18c/liu18c.pdf)
- If you are familiar with the bias or skew of the data, an option is to use rank-preserving procedures for repairing features to reduce or remove pairwise dependence with the protected attribute: [Certifying and Removing Disparate Impact](https://arxiv.org/pdf/1412.3756v3.pdf)

Interpretability
- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/pdf/1702.08608.pdf)
- [Techniques for Intepretable Machine Learning](https://arxiv.org/pdf/1808.00033.pdf)