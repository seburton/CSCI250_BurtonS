import numpy as np

def medianFilter(dataset):
    '''this function removes some noise from a dataset'''
    #the window is 0.75 seconds long
    windowSize = 15
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

def discretizeNote(dataset):
    '''takes a smooth dataset and discretizes into notes in octave 4. Each note is approximately 0.05 seconds long. returns two arrays: data notes and data frequencies, respectively'''
    #make dictionary of notes
    notes = {
        'A' : 220,
        'As' : 233,
        'B' : 247,
        'C' : 262,
        'Cs' : 277,
        'D' : 294,
        'Ds' : 311,
        'E' : 330,
        'F' : 349,
        'Fs' : 370,
        'G' : 392,
        'Gs' : 415,
    }
    noteNames = ['A', 'As', 'B', 'C', 'Cs', 'D', 'Ds', 'E', 'F', 'Fs', 'G', 'Gs']
    
    #discretize distances accordingly
    minimumDist = 1.0
    maximumDist = 50.0
    #each section represents a note corresponding with dictionary order
    distanceDiscretizations = np.arange(minimumDist, maximumDist, (maximumDist-minimumDist)/len(notes))

    #set data to be median of dataset
    data = np.median(dataset)
    
    for j in range(len(distanceDiscretizations)-1):
        #if the distance is between the current and previous distance discretizations, record note
        if data > distanceDiscretizations[j] and data < distanceDiscretizations[j+1]:
            dataNotes = noteNames[j]
            dataFrequencies = notes[noteNames[j]] 

        elif data > distanceDiscretizations[-1]:
            dataNotes = noteNames[-1]
            dataFrequencies = notes[noteNames[-1]]
            break

    return dataNotes, dataFrequencies

def discretizeType(dataset):
    '''this function discretizes distance sensor data into two sound types depending on distance reading. Returns one array of bools which represent each sound type (normal or quiet..'''
    types = {
        'Normal' : True,
        'Quiet' : False
    }
    typeNames = ['Normal', 'Quiet']
    #discretize distances accordingly
    minimumDist = 1.0
    maximumDist = 50.0
    #each section represents a note corresponding with dictionary order
    distanceDiscretizations = np.arange(minimumDist, maximumDist, (maximumDist-minimumDist)/len(types))

    data = np.median(dataset)
    
    for j in range(len(distanceDiscretizations)-1):
        #if the distance is between the current and previous distance discretizations, record type
        if data > distanceDiscretizations[j] and data < distanceDiscretizations[j+1]:
            dataTypes = types['Normal'] 
        elif data > distanceDiscretizations[-1]:
            dataTypes = types['Quiet']
            break

    return dataTypes
    