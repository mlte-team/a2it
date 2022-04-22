# A2IT Appendix
# SDMT Section 2: Fairness & Interpretability

## Fairness  
- Metrics of statistical fairness: [Certifying and Removing Disparate Impact](https://arxiv.org/pdf/1412.3756v3.pdf) and [Fair Prediction with Disparate Impact](https://arxiv.org/pdf/1703.00056.pdf)
- Tradeoffs of individual versus statistical fairness: [The Frontiers of Fairness in Machine Learning](https://arxiv.org/pdf/1810.08810.pdf) 
- Testing/measuring individual fairness: [On Formalizing Fairness in Prediction with Machine Learning](https://arxiv.org/pdf/1710.03184.pdf)
- How to consider the dynamic effects of decisions on a system: [Downstream Effects of Affirmative Action](https://arxiv.org/pdf/1808.09004.pdf) and [Delayed Impact of Fair Machine Learning](http://proceedings.mlr.press/v80/liu18c/liu18c.pdf)
- If you are familiar with the bias or skew of the data, an option is to use rank-preserving procedures for repairing features to reduce or remove pairwise dependence with the protected attribute: [Certifying and Removing Disparate Impact](https://arxiv.org/pdf/1412.3756v3.pdf)
- A general discussion of bias and fairness in machine learning: [Ch 8 Bias and Fairness](http://ciml.info/dl/v0_99/ciml-v0_99-ch08.pdf) from [A Course in Machine Learning](http://ciml.info)
- Different definitions and examples of bias, discrimination, and fairness, as well as examples of fair versions of a number of types of machine learning models: [A Survey on Bias and Fairness in Machine Learning](https://arxiv.org/pdf/1908.09635.pdf)
- Understanding, mitigating, and accounting for bias: [Bias in Data-driven AI Systems - An Introductory Survey](https://arxiv.org/pdf/2001.09762v1.pdf)
- Consider and articulate explicitly the assumptions about the circumstances and data being modeled: [The
(Im)possibility of Fairness: Different Value Systems Require Different Mechanisms For Fair Decision Making](https://dl.acm.org/doi/pdf/10.1145/3433949)
- The importance of having procedures, policies, and monitoring methods in place for machine learning: [Towards a Standard for Identifying and Managing Bias in Artificial Intelligence](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf)

#### Questions:
* Are subsets or groups within your dataset equally likely to be classified or predicted?
* If your model is being used on demographic groups, does your predictor produce similar outputs for similar individuals across demographic groups ([Gajane & Pechenizkiy 2018](https://arxiv.org/pdf/1710.03184.pdf))? 
* If your model feeds into a socio-technical system, will it dynamically affect the environment and the incentives of human actors who interact with the system?
* Is your dataset potentially biased or skewed in some way?

#### Considerations and Methods:
* Consider using metrics of statistical fairness (a small number of protected demographic groups should have parity of some statistical measure across all groups) such as raw positive classification rate ([Feldman et al. 2015](https://arxiv.org/pdf/1412.3756v3.pdf)), false positive and false negative rates, or positive predictive value (last two from [Chouldechova 2017](https://arxiv.org/pdf/1703.00056.pdf)).
*   Note that there are tradeoffs to individual versus statistical fairness, see [Chouldechova & Roth 2018](https://arxiv.org/pdf/1810.08810.pdf).
* If there is a reliable and non-discriminating distance metric, see [Gajane & Pechenizkiy's](https://arxiv.org/pdf/1710.03184.pdf) definition 4 for a test by which individual fairness can be measured.
* [Kannan et al.](https://arxiv.org/pdf/1808.09004.pdf) and [Liu et al.](http://proceedings.mlr.press/v80/liu18c/liu18c.pdf) demonstrate how to consider the dynamic effects of decisions on a system; using the context of your system, identify ways in which downstream effects might modify the social fabric and determine if those parts of the model or the system need to be modified accordingly.
* Depending upon your knowledge of bias or skew in the data, consider using rank-preserving procedures for repairing features to reduce or remove pairwise dependence with the protected attribute from [Feldman et al. 2015](https://arxiv.org/pdf/1412.3756v3.pdf).

## Interpretability
- [Towards A Rigorous Science of Interpretable Machine Learning](https://arxiv.org/pdf/1702.08608.pdf)
- [Techniques for Interpretable Machine Learning](https://arxiv.org/pdf/1808.00033.pdf)

#### Questions:
* Is it important that the model is explainable to the user? Some machine learning systems do not require explainability because “(1) there are no significant consequences for unacceptable results or (2) the problem is sufficiently well-studied and validated in real applications that we trust the system’s decision, even if the system is not perfect” ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)).
* Can interpretability be done at the model-agnostic level and simply analyze outputs with respect to their context?

#### Considerations and Methods:
* If interpretability is important, consider using intrinsic interpretability (in which the model is self-explanatory) or post-hoc interpretability (create another model to explain outputs from the first) from [Du et al. 2019](https://arxiv.org/pdf/1808.00033.pdf).
A domain expert can also be called upon to explain model outputs in their proper context ([Doshi-Velez & Kim 2017](https://arxiv.org/pdf/1702.08608.pdf)).

**Navigation Links:**  
[Appendix Index](appendix_index.md)  
[Internal Model Testing (IMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/0_IMT.md)  
[System Dependent Model Testing (SDMT)](https://github.com/turingcompl33t/a2it/blob/master/framework/1_SDMT.md)  
[Army Artificial Intelligence Testing (A2IT)](https://github.com/turingcompl33t/a2it)  
