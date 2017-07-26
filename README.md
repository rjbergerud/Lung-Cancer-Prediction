# Lung-Cancer-Prediction
Predicting Lung Cancer incidences by county.  See `cancer.ipynb` to see the implementation of the supervised learner, and `Capstone_MLND_Cancer.pdf` to see the report.

### Use conda or an alternative version control/package manager to install python 3.6

```
conda create --name lungCancer python=3
```

To run the `.ipynb` notebook, make sure you have the dependencies in the `requiments.txt`.

```pip install -r requirements.txt```

Dot file can be generated using the package graphviz

```sudo apt-get install graphviz```
```dot -Tpng tree.dot -o tree.png```
