from searcher import search_directory
from appJar import gui

app = 0

def perform_search(button_name):
    dir_name = app.getEntry("dir_area")
    print dir_name
    app.stop()
    search_directory(dir_name)

# top slice - CREATE the GUI
app = gui()

### fillings go here ###
app.addLabel("prompt", "Please enter the path of the directory you want searched for duplicate images:", 0, 0)
app.addEntry("dir_area", 1, 0)
app.addButton("Go", perform_search, 1, 1)

# bottom slice - START the GUI
app.go()

print "Hello world"
