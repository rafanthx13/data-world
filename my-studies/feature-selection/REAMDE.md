# Featreu Selection

## Com métodos Statisticos

Melhores sites:
+ BEST NOTEBOOK: https://www.kaggle.com/code/prashant111/comprehensive-guide-on-feature-selection/comments
+ https://machinelearningmastery.com/calculate-feature-importance-with-python/
+ https://machinelearningmastery.com/feature-selection-with-real-and-categorical-data/
+ https://machinelearningmastery.com/feature-selection-with-categorical-data/

## chi-2

 the chi square is designed to compare frequencies, so it is better suited for categorical data: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html. In practice, you can apply it to non-negative features, but in sklearn docs it mentions example features like boolean or counts, the first ones are categorical, the latter are at least discrete: https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.chi2.html