import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("black")

label1 = sg.Text("select archive:")
input1 = sg.Input()
choose1 = sg.FileBrowse("choose", key="archive")

label2 = sg.Text("select dest dir:")
input2 = sg.Input()
choose2 = sg.FolderBrowse("choose", key="folder")

extract = sg.Button("extract")
output = sg.Text(key="output", text_color="green")

layout = [
    [label1, input1, choose1],
    [label2, input2, choose2],
    [extract, output]
]


window = sg.Window("File Extractor", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            break

        case "extract":
            archive = values['archive']
            folder = values['folder']
            extract_archive(archive, folder)
            window['output'].update("archive extracted")
window.close()
