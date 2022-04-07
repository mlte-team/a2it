# A2IT Appendix
# SDMT Section 3: Robustness

## Robustness to Naturally Occurring Data Challenges
This section includes questions, considerations, and methods for addressing the potential naturally occurring data challenges that might arise from the ambient conditions of the system ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).  

#### Questions:
* What data challenges may occur when your model is deployed to the system? Could your model face: 
*   Significant changes in illumination or color transformations (brightness, contrast, saturation, hue, grayscale, color-depth)?
*   Motion blur or other pixel perturbations?
*   Occlusion of the target object?
*   Changes in perspective (rotation, translation, scaling, shearing, blurring, sharpening, flipping)?
*   Weather impacts? ([Russell & Norvig 2003](http://aima.cs.berkeley.edu), Ch. 25)
*   Other system specific conditions? (For example, stickers on objects or damaged objects)
* What are the typical and atypical system conditions in which your model will be deployed?
* How may data collection processes or physical sensors be degraded with time, use, or damage?
* Are there any extreme distribution shifts or long tail events that could cause large accuracy drops? ([Hendrycks et al. 2021](https://arxiv.org/pdf/2109.13916.pdf))

#### Considerations and Methods:
* If there are known specific data challenges the model will face, consider prioritizing robustness to those perturbations. (For example, Gaussian data augmentation improves robustness to noise and blurring but degrades performance on fog and contrast ([Yin et al. 2019](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf))). Generate a list of task specific properties and plot the model robustness (measured by robustness score, or fraction of correctly identified robust samples in the dataset) across the perturbation parameter space ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).   
* Otherwise, to achieve the most generally robust model the AutoAugment data augmentation policy proposed in [Yin et al. 2019](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf) achieves the most generalizable robustness to data augmentation. 
* You might also consider tying into the system-level framework in order to build in feedback loops that could influence the environment.

## Robustness to Synthetic Image Modifications
This section includes questions, considerations, and methods for addressing synthetic image modifications, which will allow the model to handle images that have been modified synthetically (for instance, a filter has been applied).  

#### Questions:
* Are there critical computer vision capabilities that would allow the model to generalize robustly beyond controlled training settings?
* How may a human approach the task in the face of synthetic modifications? Is edge detection necessary to complete the task?
* Is there existing knowledge or theories about the task that can be leveraged?

#### Considerations and Methods:
* Identify critical computer vision capabilities of the model to evaluate. See [Ribeiro et al.](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf) for content on identifying capabilities and developing task tests. Favor the model that has best learned the most relevant capabilities. Computer vision capabilities to consider testing include: 
*   Identifying shape
*   Robustness to altered texture
*   Robustness to novel backgrounds
*   Segmentation into regions
* Test types include minimum functionality, invariance, and directional expectation
* Curate test data through mutating existing inputs, generating new inputs, or obtaining new inputs.  

## Robustness to Adversarial Attack
This section includes questions, considerations, and methods for determining how an adversary may target a machine learning system. Ensuring robustness in this domain includes creating adversarial test cases and evaluating expected versus actual results.

#### Questions:
* How is an adversary most likely going to attempt to break your model?
* What would be the most dangerous method an adversary could use to break your model?
* Did you consider different types and natures of vulnerabilities such as data pollution, physical infrastructure, and cyber attacks? ([Hendrycks et al. 2021](https://arxiv.org/pdf/2109.13916.pdf))
* What is the threat of evasion attacks, poisoning attacks, extraction attacks, and inference attacks, and does the model need to be prepared to address these? ([ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox))
* Did you consult with the systems team to put measures in place to ensure integrity and resilience of the system against attacks?

#### Considerations and Methods:
* Consider using performance metrics for adversarial robustness like in [Buzhinsky et al. 2020](https://arxiv.org/pdf/2003.01993.pdf). Adversarial robustness in the latent space is the “resilience” to the worst-case noise additions. Metrics include local latent adversarial robustness, generation severity, reconstructive severity, and reconstructive accuracy. 
* Generate simulations for possible adversarial attacks to predict behavior in settings that preclude practical testing of the system itself ([Pezzementi et al. 2021](https://www.journalfieldrobotics.org/Field_Robotics/Papers_files/10_Pezzementi.pdf)). Evaluate model performance based on a metric like a robustness receiver operating curve (ROC). 
* Consider using a benchmarked adversarial robustness tool like [CleverHans](https://github.com/cleverhans-lab/cleverhans), [Foolbox](https://github.com/bethgelab/foolbox), or the Adversarial Robustness Tool ([ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox)).
* If it would be beneficial to detect adversarial anomalies or assign low confidence values to potential adversarial inputs, that is something that should be tied into the system framework. 
  
  
#### Further Robustness References
- Identifying model capabilities and generating test cases based on those capabilities helps ensure a robust model: [Behavioral Testing](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf)
- Practical examination of methods and metrics for robustness with case studies and scenarios: [Robustness Testing of AI Systems](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)
- Specific information about computer vision dataset augmentation: [Model Robustness in Computer Vision](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf)
- Performance measures for adversarial deep learning robustness: [Metrics and Methods for Robustness Evaluation](https://arxiv.org/pdf/2003.01993.pdf)
- Proposed novel robustness ROC metric: [Perception Robustness Testing](https://www.journalfieldrobotics.org/Field_Robotics/Papers_files/10_Pezzementi.pdf)
  
**Navigation Links:**  
[Appendix Index](appendix_index.md)  
[Internal Model Testing (IMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/0_IMT.md)  
[System Dependent Model Testing (SDMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/1_SDMT.md)  
[Army Artificial Intelligence Testing (A2IT)](https://github.com/turingcompl33t/a2it)  
