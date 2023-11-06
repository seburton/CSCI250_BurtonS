
import numpy as np
import matplotlib.pyplot as plt
from math import *
import scipy as sp

import numpy.random as rng


def myOtherMedianFilter(dataset, windowSize):
    filteredSet = dataset.copy()
    for i in range(len(dataset)):
        if i < windowSize/2 :
            filteredSet[i] = (np.median(dataset[:windowSize]))
        elif i > len(dataset)-windowSize/2:
            filteredSet[i] = (np.median(dataset[-windowSize:]))
        else:
            workingSet = dataset[i-int(windowSize/2) : i+int(windowSize/2)]
            filteredSet[i] = (np.median(workingSet))
    return filteredSet


def myMedianFilter(dataset, windowSize):
    filteredSet = []
    for i in range(len(dataset)):
        if i < windowSize/2 :
            filteredSet.append(np.median(dataset[:windowSize]))
        elif i > len(dataset)-windowSize/2:
            filteredSet.append(np.median(dataset[-windowSize:]))
        else:
            workingSet = dataset[i-int(windowSize/2) : i+int(windowSize/2)]
            filteredSet.append(np.median(workingSet))
    return filteredSet


def myMeanFilter(dataset, windowSize):
    filteredSet = []
    for i in range(len(dataset)):
        if i < windowSize/2 :
            filteredSet.append(np.mean(dataset[:windowSize]))
        elif i > len(dataset)-windowSize/2:
            filteredSet.append(np.mean(dataset[-windowSize:]))
        else:
            workingSet = dataset[i-int(windowSize/2) : i+int(windowSize/2)]
            filteredSet.append(np.mean(workingSet))
    return filteredSet