# System Dependent Model Testing
### Objective and Rationale
Machine learning models and the systems into which they are integrated must be functional in their desired context, as well as robust to an array of potential circumstances.  
This section lists properties that should be considered for model and system requirements and how those are prioritized, including weighing tradeoffs ([Ribeiro et al. 2020](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf)).  

TODO(Kyle): Add your definition of property here   

Model and system teams should select the subset of these properties that are most relevant for your application. Ensure that you track the values of the metrics associated with these properties; we recommend existing experiment tracking services such as [MlFlow Tracking](https://mlflow.org/docs/latest/tracking.html) or [Weights and Biases Experiments](https://wandb.ai/site/experiment-tracking). 

## System Dependent Model Testing (SDMT) Properties

**Structure**

The properties are organized into four categories: 
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
- Implementation: Start by identifying the protected attribute in your dataset, and then determine what fairness measure the model and system should prioritize. Depending on those two priorities and their respective tradeoffs, see the [fairness & interpretability section](appendix/appendix_SDMT_s2.md) of the [appendix](appendix/appendix_index.md) for more resources on fairness.

**Interpretability**
- Objective: Some systems necessitate an ability to be explained or presented in understandable terms to a human ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)). 
- Metric: Interpretability is difficult to measure; it can be considered from an end-user perspective or from a developer perspective by observing and evaluating the interactions of these teams with the system, or having a domain expert explain model outputs in context ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)).
- Rationale: Depending on the system purpose, it may be critical for the system to be explainable and understandable.
- Implementation: Options include, among others: intrinsic interpretability in which a model is self explanatory, and post-hoc interpretability where another model is created to explain outputs from the first ([Du et al. 2019](https://arxiv.org/pdf/1808.00033.pdf)). For more resources on interpretability, see the [fairness & interpretability section](appendix/appendix_SDMT_s2.md) of the [appendix](appendix/appendix_index.md).

### Robustness

**Robustness to Naturally Occurring Data Challenges**
- Objective: Ensure that the model is robust to naturally occurring data challenges that it will encounter in the ambient conditions of the system ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).
- Metric: Depending on the identified data challenges and the task specific properties, model robustness can be measured by a robustness score across the perturbation parameter space. This is a metric that calculates the fraction of correctly identified robust samples in the dataset. Reassessing the model accuracy with augmented datasets is also a common metric for robustness ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).
- Rationale: Models implemented in a system will experience common data challenges like illumination, motion blue, occlusion, changes in perspective, and weather impacts. These perturbations affect the data and can have significant impacts on the quality of the model prediction which must be addressed before deployment ([Russell & Norivg](http://aima.cs.berkeley.edu)). For more metrics and information on general robustness, see [this](https://thirdeyedata.io/robustness-measurement-of-machine-learning-models-with-examples-in-python/) blog post.
- Implementation: Dependent on the identified data challenges; see references section at the bottom of this page for more resources on dataset augmentation. The AutoAugment data augmentation policy proposed in ([Yin et. al 2019](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf)) is a recommended starting point. The ([CheckList](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf)) paper is also a useful tool to identify necessary capabilities of the model to promote robustness. For more resources on robustness, see the [robustness section](appendix/appendix_SDMT_s3.md) of the [appendix](appendix/appendix_index.md).  

**Robustness to Adversarial Attack**
- Objective: Ensure that the model is robust to synthetic manipulation or targeted adversarial attacks ([Hendrycks et al.](https://arxiv.org/pdf/2109.13916.pdf) and [McGraw et al. 2020](https://berryvilleiml.com/docs/ara.pdf)).
- Metric: There are performance metrics for adversarial robustness ([Buzhinsky et al. 2020](https://arxiv.org/pdf/2003.01993.pdf)) and existing benchmarked adversarial robustness tools such as ([CleverHans](https://github.com/cleverhans-lab/cleverhans), [FoolBox](https://github.com/bethgelab/foolbox), [ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox)) that may be used. 
- Rationale: A model deployed in a system may face different vulnerabilities (data pollution, physical infrastructure, etc.) and attacks (poisoning, extraction, inference, etc.) that can significantly degrade the performance, security, or safety of the model. 
- Implementation: Dependent on the identified adversary most likely course of action (MLCOA) and most dangerous course of action (MDCOA); see the [robustness section](appendix/appendix_SDMT_s3.md) of the [appendix](appendix/appendix_index.md) for more resources on adversarial robustness. 

**Robustness to Device-Generated Perturbations**  
- Objective: Ensure that the model and the system are robust to perturbations resulting from devices that are part of the system. An example of a device-generated perturbation would be a camera taking unfocused video or pictures, making it impossible for the computer vision model to detect objects.
- Metric: If sensor redundancy is determined necessary, establish a common representation of the input, and evaluate the system with simulated sensor failures. If robustness to single sensor noise is acceptable, determine the most likely sensor degradations and evaluate the mAP to a simulated degraded dataset.
- Rationale: Models are often evaluated with full sensor availability. However, in a safety critical system, unexpected scenarios like sensor degradation or failure must be accounted for. 
- Implementation: Depending on the system in which the model will be deployed, an option is to implement sensor redundancy. An architecture that uses multiple sensors to perform object detection jointly can provide robustness to sensor failure [Berntsson & Tonderski 2019](https://odr.chalmers.se/bitstream/20.500.12380/300780/1/master-thesis-report_berntsson-tonderski.pdf). Alternatively, if typical sensor degradation patterns are known or possible to predict, robustness tests specific to the sensor can be designed. [Seals 2019](https://trace.tennessee.edu/cgi/viewcontent.cgi?article=6960&context=utk_gradthes). For example, evaluating the mAP of the model against speckle noise, salt and pepper noise, contrast alterations, or Gaussian noise to determine robustness. 

**Security**
- Objective: Ensure that the model is insulated to compromise from internal error.
- Metric: The metric by which security is measured will depend on what risks are most likely for your given model. Areas of focus could include adversarial attacks (as described above), reproducibility, overfitting, and output integrity among others. See [McGraw et al. 2020](https://berryvilleiml.com/docs/ara.pdf) for a comprehensive list of risks and recommended methods of addressing them.
- Rationale: A model and the system in which it is encased have numerous risk areas that can be traced back to intrinsic design flaws [McGraw et al. 2020](https://berryvilleiml.com/docs/ara.pdf).
- Implementation: Prioritize risks based on your model and system, and address them in order of probability that they occur.  

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

**Training Energy Consumption**
- Objective: Measure the energy consumption of the model training process.
- Metric: The energy consumed by the training process in joules (total power consumption over a time interval).
- Rationale: For large-scale machine learning applications, energy consumption may be a major driver in the total cost of development and maintenance. The model training process is frequently the most energy-intensive stage of the machine learning pipeline.
- Implementation: Energy consumption and power requirements are a relatively-new consideration in the field of machine learning. Accordingly, methods for convenient and accurate measurement are limited.

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

**Inference Memory Consumption**
- Objective: Measure the peak and average memory consumption during model inference.
- Metric: The volume of memory consumed in bytes or some multiple thereof (kilobytes, megabytes, etc.). This metric is absolute. 
- Rationale: The memory requirements of model inference determine the load that is places on the system during inference. This is a key determinant in the memory resources required for model deployment. For example, a model for which inference is not memory-intensive may be deployed to an instance with relatively light memory resources. This might allow for investment in other resources, such as core count, for the instance to which the model is deployed. 
- Implementation: Measure the memory consumption of the process during the inference procedure.

**Inference Energy Consumption**
- Objective: Measure the energy consumption of the model inference process.
- Metric: The energy consumed by the inference process in joules (total power consumption over a time interval).
- Rationale: For large-scale machine learning applications, energy consumption may be a major driver in the total cost of development and maintenance.
- Implementation: Energy consumption and power requirements are a relatively-new consideration in the field of machine learning. Accordingly, methods for convenient and accurate measurement are limited.

### Scalability
- Model size as a function of data size
- Training time as a function of data size
- Training cost (CPU, memory) as a function of data size

### Next Steps
* Meet with the system team and discuss each property result.
    * The results of each portion of SDMT along with your list of model inputs, outputs, and requirements should be discussed in the context of the system.
    * Determine if changes need to be made to the model or the system.
    * Consider the tradeoffs inherent in your requirements, and consider that you might need to get feedback from customers and iterate through these properties with their requirements in mind. 
    * Do not continue to model production and system integration until your team and the system team have agreed that the model and system are synchronized and requirements are satisfied at both the model and the system levels.

#### References and additional materials can be found in the [Appendix](appendix/appendix_index.md).
