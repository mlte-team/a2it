# A2IT Appendix
# SDMT Section 3: Robustness

## Robustness to naturally occuring data challenges
Robustness to naturally occuring data challenges that the model encounters in the ambient conditions of the system ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).  

#### Questions:
* What data challenges may occur when your model is deployed to the system? Could your model face: 
*   Significant changes in iIllumination or color transformations? (Brightness, contrast, saturation, hue, gray-scale, color-depth)
*   Motion blur or other pixel perturbations?
*   Occlusion of the target object?
*   Changes in perspective? (Rotation, translation, scaling, shearing, blurring, sharpening, flipping)
*   Weather impacts? ([Russell & Norvig 2003](http://aima.cs.berkeley.edu), Ch. 25)
*   Other system specific conditions? (For example, stickers on objects or damaged objects)
* What are the typical and atypical system conditions in which your model will be deployed?
* How may data collection processes or physical sensors be degraded with time, use, or damage?
* Are there any extreme distribution shifts or long tail events that could cause large accuracy drops? ([Hendrycks et al. 2021](https://arxiv.org/pdf/2109.13916.pdf))

#### Considerations and Methods:
* If there are known specific data challenges the model will face, consider prioritizing robustness to those perturbations. (For example, Gaussian data augmentation improves robustness to noise and blurring but degrades performance on fog and contrast ([Yin et al. 2019](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf))). Generate a list of task specific properties and plot the model robustness (measured by robustness score, or fraction of correctly identified robust samples in the dataset) across the perturbation parameter space ([Berghoff et al. 2021](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)).   
* Otherwise, to achieve the most generally robust model the AutoAugment data augmentation policy proposed in [Yin et al. 2019](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf) achieves the most generalizable robustness to data augmentation. 
* You might also consider tying into the system-level framework in order to build in feedback loops that could influence the environment.

## Robustness to synthetic image modifications
Robustness to synthetic image modifications: Ensure the model can handle images that have been modified synthetically (for instance, a filter has been applied).  

#### Questions:
* Are there critical computer vision capabilities that would allow the model to generalize robustly beyond controlled training settings?
* How may a human approach the task in the face of synthetic modifications? Is edge detection necessary to complete the task?
* Is there existing knowledge or theories about the task that can be leveraged?

#### Considerations and Methods:
* Identify critical computer vision capabilities of the model to evaluate. See the [CheckList paper](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf) on identifying capabilities and developing task tests. Favor the model that has learned the most relevant capabilities better. Computer vision capabilities to consider testing include: 
*   Identifying shape
*   Robustness to altered texture
*   Robustness to novel backgrounds
*   Segmentation into Regions
* Test types include minimum functionality, invariance, and directional expectation
* Curate test data through mutating existing inputs, generating new inputs, or obtaining new inputs.  
TODO(Kate and Jenny): rephrase or rewrite this section to be more appropriate for image modifications  

## Robustness to adversarial attack
Robustness to adversarial attack: If applicable, determine an adversary’s most likely method of attack and most dangerous method of attack for how your system could be targeted. Create adversarial test cases and evaluate expected versus actual results. Some hostile methods of a nefarious actor have already been covered above in robustness to synthetic image modifications.

#### Questions:
* What is an adversary most likely going to attempt to break your model?
* What would be the most dangerous thing an adversary could do to break your model?
* Did you consider different types and natures of vulnerabilities, such as data pollution, physical infrastructure, and cyber attacks? ([Hendrycks et al. 2021](https://arxiv.org/pdf/2109.13916.pdf))
* What is the threat of evasion attacks, poisoning attacks, extraction attacks, and inference attacks, and does the model need to be prepared to address these? ([ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox))
* Did you consult with the systems team to put measures in place to ensure integrity and resilience of the system against attacks?

#### Considerations and Methods:
* Consider using performance metrics for adversarial robustness like in [Buzhinsky et al. 2020](https://arxiv.org/pdf/2003.01993.pdf). Adversarial robustness in the latent space is the “resilience” to the worst-case noise additions. Metrics include local latent adversarial robustness, generation severity, reconstructive severity, and reconstructive accuracy. 
* Generate simulations for possible adversarial attacks to predict behavior in settings that preclude practical testing of the system itself ([Pezzementi et al. 2021](https://www.journalfieldrobotics.org/Field_Robotics/Papers_files/10_Pezzementi.pdf)). Evaluate model performance based on a metric like a robustness receiver operating curve (ROC). 
* Consider using a benchmarked adversarial robustness tool like [CleverHans](https://github.com/cleverhans-lab/cleverhans), [FoolBox](https://github.com/bethgelab/foolbox), or Adversarial Robustness Tool ([ART](https://github.com/Trusted-AI/adversarial-robustness-toolbox)).
* If it would be beneficial to detect adversarial anomalies or assign low confidence values to potential adversarial inputs, this is another section to tie into the system framework. 
  
  
#### References
- Identifying model capabilites and generated test cases based on these capabilites helps ensure a robust model [Behavioral Testing](https://homes.cs.washington.edu/~wtshuang/static/papers/2020-acl-checklist.pdf)
- Practical examination of methods and metrics for robustness with case studies and scenarios [Robustness Testing of AI Systems](https://link.springer.com/chapter/10.1007/978-3-030-79150-6_21)
- Specific to computer vision and dataset augmentation [Model Robustness in Computer Vision](https://proceedings.neurips.cc/paper/2019/file/b05b57f6add810d3b7490866d74c0053-Paper.pdf)
- Performance measures for adversarial deep learning robustness [Metrics and Methods for Robustness Evaluation](https://arxiv.org/pdf/2003.01993.pdf)
- Proposed novel robustness ROC metric [Perception Robustness Testing](https://www.journalfieldrobotics.org/Field_Robotics/Papers_files/10_Pezzementi.pdf)
  
  
**Navigation Links:**  
[Appendix Index](appendix_index.md)  
[Internal Model Testing (IMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/0_IMT.md)  
[System Dependent Model Testing (SDMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/1_SDMT.md)  
[Army Artificial Intelligence Testing (A2IT)](https://github.com/turingcompl33t/a2it)  
