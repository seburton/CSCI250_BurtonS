import DataProcessing

class Note:
    
    def __init__(self, distance):
        note, frequency = DataProcessing.discretizeNote(distance)
        
        self.pitch = frequency
        self.duration = 0.05
