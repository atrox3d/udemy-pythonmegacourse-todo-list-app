import functions
import PySimpleGUI as sg

label = sg.Text("Enter a TODO:")
inputbox = sg.InputText(tooltip="enter a TODO", key="todo")
addbutton = sg.Button("Add")

listbox = sg.Listbox(
    values=functions.get_todos(),
    key='todos',
    enable_events=True,
    size=(45, 10)
)
editbutton = sg.Button("Edit")

window = sg.Window(
    title='My ToDo app',
    layout=[                    # layout rows
        [label],                # row #1
        [inputbox, addbutton],  # row #2
        [listbox, editbutton]
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read()
    print(f"INFO | event : {event}")
    print(f"INFO | values: {values}")
    match event:
        case sg.WIN_CLOSED:
            print("INFO | WIN_CLOSED event detected, closing...")
            break

        case 'Add':
            todos = functions.get_todos()

            new_todo = values['todo'] + "\n"
            todos.append(new_todo)

            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'Edit':
            todos = functions.get_todos()

            if not len(values['todos']):
                print(f"INFO | ignoring Edit event because values['todos'] is empty")
                continue
            todo = values['todos'][0]
            new_todo = values['todo'] + "\n"
            index = todos.index(todo)
            todos[index] = new_todo

            functions.write_todos(todos)

            window['todos'].update(values=todos)

        case 'todos':
            value = values['todos'][0]
            window['todo'].update(value=value)

window.close()
