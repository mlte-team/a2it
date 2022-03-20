# Internal Model Testing
### Objective and Rationale
Determining model performance and ensuring that it could add value is a critical step in building a machine learning tool or system ([Raschka 2018](https://arxiv.org/pdf/1811.12808.pdf)).  
This section is dedicated to ensuring that a team building a machine learning model understands and can articulate their model requirements in order to prepare them for the next step of the process, which is system integration “[Machine Learning in Production: From Models to Systems](https://ckaestne.medium.com/machine-learning-in-production-from-models-to-systems-e1422ec7cd65)”).  
## Internal Model Testing (IMT) Procedure
1. This testing procedure makes several assumption of the preparation required for a model to be tested, meaning that it expects your team to have conducted a machine learning process, including (but not limited to):
    * Making a preliminary list of model requirements ranked in order of priority (if unsure how to rank your requirements, consider Case-Based Ranking from [Perini et al](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6249686)).
    * Ensuring that representative training and test data is available or provided for the problem you're trying to solve, and handling the data appropriately based on any associated permissions or authorities that are required.
    * Splitting the data for training, validation, and testing.
    * Appropriately selecting a model and then fine-tuning it.  
    If you are unsure that your team and model are ready for internal model testing, reference a checklist such as Chapter 2 of [Hands-On Machine Learning](https://learning.oreilly.com/library/view/hands-on-machine-learning/9781492032632/) or a similar guide (like [Raschka 2018](https://arxiv.org/pdf/1811.12808.pdf)); you can also see [section 1](appendix/appendix_section_1.md) of the [appendix](appendix/appendix_index.md) for more information.  
2. Determine one or more appropriate baseline tests for your model. Below are some suggestions; if no example works for your system, then justify the baseline that you select. **Please note that this step is the most time and resource-intensive of the IMT procedure, but if done right will ensure your model is appropriately evaluated.**  
    * Some datasets and methods already have an accepted baseline that can be used (for instance, [PASCAL VOC](http://host.robots.ox.ac.uk/pascal/VOC/pubs/everingham10.pdf) is an object category recognition and detection benchmark).
    * Classify everything as the majority (as described by Chapter 7.2 of [Hvitfeldt & Silge 2021](https://smltar.com/mlclassification.html#classnull)).
    * If this model implements a task that is currently performed manually, conduct a test in which humans perform the task and use their performance as the baseline.
3. While selecting a baseline, a performance metric must also be stipulated. The choice of metric depends on the exact nature of the computer vision system being created; following are some examples to consider.  
    * Classification:
        * Receiver Operating Characteristics ([ROC](https://scikit-learn.org/stable/auto_examples/model_selection/plot_roc.html?highlight=roc)) curves and the Area Under the Curve ([AUC](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.roc_auc_score.html#sklearn.metrics.roc_auc_score)): Evaluation metrics for standard classification tasks. 
        * Precision Recall Curves and Area Under the Precision Recall Curve ([AUPRC](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.PrecisionRecallDisplay.html#sklearn.metrics.PrecisionRecallDisplay)): Used when there are class imbalances.
    * Object Detection:
        * Average Precision ([AP](https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html?highlight=precision%20recall)) is the weighted mean of precisions achieved at each recall threshold.
        * [mAP50](https://arxiv.org/abs/2112.02814): Used when detecting multiple classes. The precision accumulated over different levels of recall under the intersection over union (IOU) threshold of 0.50. 
        * [mAP](https://arxiv.org/abs/2112.02814): Extension of mAP50 that is averaged over ten IOU thresholds
4. Import the functions for your selected metrics from [ml-te](https://github.com/turingcompl33t/mlte) (pronounced 'melt'). Using your test dataset, conduct a test measuring the model with the selected metric against the chosen baseline. If it is possible for multiple test sets to be generated, using different ones for each evaluation in this module and for [SDMT](1_SDMT.md) will produce the best results. However, that is often not possible for practitioners, and there is data to support that substantial overfitting does not occur even if a single test set is used multiple times ([Roelofs et al. 2019](https://proceedings.neurips.cc/paper/2019/file/ee39e503b6bedf0c98c388b7e8589aca-Paper.pdf)).
6. If performance exceeds the baseline, stop here and go to “next steps”.
7. If performance does not exceed the baseline, return to the machine learning process referenced in part i and iterate through potential changes to the model to improve performance.
### Next Steps
* Meet with the team or individual in charge of designing and implementing the computer vision system of which your model is a part. 
    * The results of your IMT along with your list of model inputs, outputs, and requirements should be discussed in the context of the system.
    * Determine if changes need to be made to the model or the system. 
    * Do not continue to [System Dependent Model Testing](1_SDMT.md) (SDMT) until your team and the system team have agreed that the model and system are synchronized and requirements are satisfied at both the model and the system levels.
