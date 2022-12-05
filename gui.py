import functions
import PySimpleGUI as sg

label = sg.Text("Enter a TODO:")
inputbox = sg.InputText(tooltip="enter a TODO")
addbutton = sg.Button("Add")
window = sg.Window(
    title='My ToDo app',
    layout=[                    # layout rows
        [label],                # row #1
        [inputbox, addbutton]   # row #2
    ]
)
window.read()
window.close()
