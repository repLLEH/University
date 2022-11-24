import Model
import Controller
import View

model = Model.Diary_model()
controller=Controller.DiaryController()
view=View.DiaryView()
auth=View.AuthScreen()
reg=View.RegistrationScreen()
profile=View.ProfileScreen()
profileMod=View.ProfileModScreen()
noteCr=View.NoteCreationScreen()
noteDel=View.NoteDeletionScreen()
controller.start()