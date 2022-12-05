import functions
import PySimpleGUI as sg

label = sg.Text("Enter a TODO:")
inputbox = sg.InputText(tooltip="enter a TODO", key="todo")
addbutton = sg.Button("Add")
window = sg.Window(
    title='My ToDo app',
    layout=[                    # layout rows
        [label],                # row #1
        [inputbox, addbutton]   # row #2
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case sg.WIN_CLOSED:
            break

        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
window.close()
