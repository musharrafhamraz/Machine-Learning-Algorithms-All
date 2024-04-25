**Decision Tree**

Decision Tree is a non-parametric supervised machine learning alogorithm that can be used for both classification and regression tasks. It has a heirarchical, tree structure that consists of root node, branches, internal nodes and leaf nodes.**It works by recursively partitioning the data into subsets based on the most significant attribute at each node.**

**Example**

Let's say we have a dataset of fruits with two features: color and shape, and we want to classify them as either "apple" or "orange".

    ->Start: Initially, the entire dataset is considered at the root node of the tree.

    ->Splitting Criteria: The decision tree algorithm selects the most significant attribute to split the data. This is often done using measures like Gini impurity or entropy. Let's say for our example, it selects "color" as the most significant attribute.

    ->Partitioning: Based on the selected attribute, the data is partitioned into subsets. For example, if the split is based on the "color" attribute:
If color is "Red": [Apple, Apple, Red]
If color is "Green": [Apple, Green]
If color is "Orange": [Orange, Orange, Orange, Orange]

    ->Recurse: The process is then applied recursively to each subset until a stopping criterion is met. The algorithm continues splitting the subsets based on the most significant attribute at each node until certain conditions are met, such as reaching a maximum tree depth, achieving a minimum number of samples at a node, or until further splitting does not improve the classification significantly.
    
    ->Leaf Nodes: Eventually, each subset becomes a leaf node in the decision tree, representing a class label (e.g., "Apple" or "Orange").