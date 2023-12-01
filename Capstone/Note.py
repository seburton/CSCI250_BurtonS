import DataProcessing

class Note:
    
    def __init__(self, distances):
        note, frequency = DataProcessing.discretizeNote(distances)
        
        self.pitch = frequency
        self.duration = 0.5
