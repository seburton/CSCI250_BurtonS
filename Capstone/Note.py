import DataProcessing

class Note:
    
    def __init__(self, noteDistances, typeDistances):
        note, frequency = DataProcessing.discretizeNote(noteDistances)

        type = DataProcessing.discretizeType(typeDistances)

        if type == True:
            self.pitch = frequency
        else:
            self.pitch = 0
        
        self.duration = 0.5
