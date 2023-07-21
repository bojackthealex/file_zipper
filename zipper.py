import PySimpleGUI as gui
import zip_creator


#------------- GUI --------------
# GUI Elements
label_to_compress = gui.Text("Select files to Zip:")
input_to_compress = gui.Input()
browse_to_compress = gui.FilesBrowse("Choose Files", key="filepath")

label_destination = gui.Text("Select the target folder:")
input_destination = gui.Input()
browse_destination = gui.FolderBrowse("Choose Directory", key="directory")

button_compress = gui.Button("Zip my files")
# Arranging the layout
window_layout = [[label_to_compress],
                 [input_to_compress, browse_to_compress],
                 [label_destination],
                 [input_destination, browse_destination],
                 [button_compress]]

window = gui.Window("File Zipper by MediaLex", layout=window_layout)

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["filepath"]
    filepaths = filepaths.split(";")
    folderpath = values["directory"]
    print(filepaths)
    print(folderpath)

window.close()
