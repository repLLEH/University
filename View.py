import Controller
class DiaryView:
    def __init__(self):
        self.regScreen = RegistrationScreen()
        self.authScreen = AuthScreen()
        self.profileModifyingScreen = ProfileModScreen()
        self.profileScreen = ProfileScreen()
        self.noteCreationScreen = NoteCreationScreen()
        self.noteDeletionScreen = NoteDeletionScreen
class RegistrationScreen:
    def __init__(self):
        pass
    def showRegForm(self):
        pass
    def data_check(self):
        pass

class AuthScreen:
    def __init__(self):
        pass
    def showRegForm(self):
        pass
    def data_check(self):
        pass
class ProfileModScreen:
    def __init__(self):
        pass
    def showModForm(self):
        pass
    def showProfile(self):
        pass
class ProfileScreen:
    def __init__(self):
        pass
    def showProfile(self):
        pass

class NoteCreationScreen:
    def __init__(self):
        pass
    def showCreationForm(self):
        pass
    def showNote(self):
        pass
class NoteDeletionScreen:
    def __init__(self):
        pass
    def showDeletionForm(self):
        pass
    def showDeletionNotification(self):
        pass

