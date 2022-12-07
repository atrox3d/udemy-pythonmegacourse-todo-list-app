import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w"):
        pass

sg.theme("Black")

clock = sg.Text(time.strftime("%b %d, %Y %H:%M:%S"), key="clock")
label = sg.Text("Enter a TODO:")
inputbox = sg.InputText(tooltip="enter a TODO", key="todo")
addbutton = sg.Button("Add")
completebutton = sg.Button("Complete")
editbutton = sg.Button("Edit")
exitbutton = sg.Button("Exit")


listbox = sg.Listbox(
    values=functions.get_todos(),
    key='todos',
    enable_events=True,
    size=(45, 10)
)

window = sg.Window(
    title='My ToDo app',
    layout=[                                    # layout rows
        [clock],                                # row 1
        [label],                                # row 2
        [inputbox, addbutton],                  # row 3
        [listbox, editbutton, completebutton],  # row 5
        [exitbutton]                            # row 6
    ],
    font=('Helvetica', 20)
)

while True:
    event, values = window.read(timeout=1000, timeout_key="clock")
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    if event != "clock":
        print(f"INFO | event          : {event}")
        print(f"INFO | values         : {values}")
        try:
            print(f"INFO | values['todos']: {values['todos']}")
        except TypeError:
            pass

    match event:
        case "clock":
            pass
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
            try:
                todos = functions.get_todos()

                todo = values['todos'][0]
                new_todo = values['todo'] + "\n"
                index = todos.index(todo)
                todos[index] = new_todo

                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("helvetica", 20))

        case 'Complete':
            try:
                todos = functions.get_todos()

                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)

                functions.write_todos(todos)

                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first", font=("helvetica", 20))
        case "Exit":
            break

        case 'todos':
            value = values['todos'][0]
            window['todo'].update(value=value)

        case _:
            print("default")

window.close()
