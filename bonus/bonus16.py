import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress", key="compress")
output = sg.Text(key="output")

layout = [
    [label1, input1, choose_button1],
    [label2, input2, choose_button2],
    [compress_button, output]
]

window = sg.Window("File Compressor", layout=layout)

while True:
    event, values = window.read()
    print("INFO | event : ", event)
    print("INFO | values: ", values)

    match event:
        case sg.WIN_CLOSED:
            print("INFO | WIN_CLOSED event detected, closing...")
            break
        case "compress":
            window["output"].update(value="compressing...")
            # print("INFO | compress ", values["files"], "into ", values["folder"])
            files = values["files"].split(";")
            folder = values["folder"]
            # print("INFO | files | ", files)
            # print("INFO | folder| ", folder)
            # continue
            for file in files:
                print("INFO | COMPRESS | FILE | ", file)
            print("INFO | COMPRESS | DEST | ", folder)
            make_archive(files, folder)
            window["output"].update(value="compression complete")
window.close()
