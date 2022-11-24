class Calendar:
    def __init__(self):
        self.date=[]
class NoteCreation:
    def __init__(self):
        self.noteType=False
        calendar=Calendar()
        self.date=calendar.date
    def create(self):
        pass
class Diary_model:
    def __init__(self):
        self.profileID=[]
        calendar=Calendar()
        self.Calendar=calendar.date
        self.note=[]
        self.noteType=[]
    def Auth(self):
        pass
    def noteCreation(self,note):
        note_creation=NoteCreation()
        note_creation.create()
    def noteDeletion(self,id:int):
        pass
    def noteModification(self,id:int):
        pass