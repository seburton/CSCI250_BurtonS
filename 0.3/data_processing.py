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

def discretizeNotes(data):
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

    dataNotes = []
    dataFrequencies = []
    for i in range(len(data)):
        for j in range(len(distanceDiscretizations)-1):
            #if the distance is between the current and previous distance discretizations, record note
            if data[i] > distanceDiscretizations[j] and data[i] < distanceDiscretizations[j+1]:
                dataNotes.append( noteNames[j] )
                dataFrequencies.append( notes[noteNames[j]] )
            elif data[i] > distanceDiscretizations[-1]:
                dataNotes.append(noteNames[-1])
                dataFrequencies.append(notes[noteNames[-1]])

    return dataNotes, dataFrequencies

def discretizeType(dataset):
    '''this function discretizes distance sensor data into two sound types depending on distance reading. Returns one array of frequencies which represent each sound. Note lengths are ~0.05 seconds.'''
    types = {
        'Normal' : 50,
        'Vibrato' : 6
    }
    #discretize distances accordingly
    minimumDist = 1.0
    maximumDist = 50.0
    #each section represents a note corresponding with dictionary order
    distanceDiscretizations = np.arange(minimumDist, maximumDist, (maximumDist-minimumDist)/len(types))
    
    dataTypes = []
    for i in range(len(data)):
        for j in range(len(distanceDiscretizations)-1):
            #if the distance is between the current and previous distance discretizations, record type
            if data[i] > distanceDiscretizations[j] and data[i] < distanceDiscretizations[j+1]:
                dataTypes.append( types[j] )
            elif data[i] > distanceDiscretizations[-1]:
                dataTypes.append(typeNames[-1])

    return dataTypes
    