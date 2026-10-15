import json

def read_file(note_list, file_oject) -> None:
    for note in file_oject:
        if note.strip():
            note_line = json.loads(note)
            note_list.append(note_line)

def add_note() -> None:
    """This Method Will Add New Note To notes.json File."""

    note_file = "note.json"
    note_list = []

    print("Enter 'q' To Exit From This Section.\n")

    note_title = input("Enter note title: ").strip().capitalize()

    if note_title == 'q':
        return
    
    note_content = input("Enter note content: ").strip()

    if note_content == 'q':
        return
    
    try:
        with open(note_file, 'r', encoding="utf-8") as read_mood:
            read_file(note_list, read_mood)
            
            # note_id = note_list[-1].get("id") + 1
            # note_id = max(note_list, key=lambda item: item["id"])["id"] + 1
            note_id = max((item["id"] for item in note_list), default=0) + 1
            # note_id = len(note_list) + 1

    except FileNotFoundError:
        note_id = 1

    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file.")
        return

    note_structure = {

        "id": note_id,
        "title": note_title,
        "content": note_content,
    
    }
    
    with open(note_file, 'a', encoding="utf-8") as write_mood:
        # if note_list:
            # note_list.append(note_structure)

            # for note in note_list:
            #     json.dump(note, write_mood)
            #     write_mood.write("\n")

        # else:
        json.dump(note_structure, write_mood)
        write_mood.write("\n")

    print('-' * 50)
    print("Add New Note Has Successfully.")
    
    return

def display_notes() -> None:
    """This Method Will Display All Note From note.json File."""

    note_file = "note.json"
    note_list = []

    try:
        with open(note_file, 'r', encoding="utf-8") as read_mood:
            read_file(note_list, read_mood)

    except FileNotFoundError:
        print("No notes found.\nPlease add a note first.")

    else:
        if note_list:
            for note in note_list:
                print(f"[{note.get('id')}] {note.get('title')}")
                print(f"  {note.get('content')}\n")

        else:
            print("No notes found.\nPlease add a note first.")
    
    return

def delete_note() -> None:
    """This Method Will Delete Note From note.json File."""

    note_file = "note.json"
    note_list = []

    try:
        with open(note_file, 'r', encoding="utf-8") as read_mood:
            read_file(note_list, read_mood)

    except FileNotFoundError:
        print("No notes found.\nPlease add a note first.")
        return

    if note_list:
        for note in note_list:
            print(f"[{note.get('id')}] {note.get('title')}")
            print(f"  {note.get('content')}\n")

    else:
        print("No notes found.\nPlease add a note first.")
        return

    print('-' * 50)

    try:
        print("Enter '0' To Exit From This Section.\n")

        note_id_delete = int(input("Enter note ID: "))

        if note_id_delete < 0:
            raise ValueError
    
    except ValueError:
        print("Enter Valid Number In The Next Time.")
        return

    if note_id_delete == 0:
        return

    flag = True

    for index, search_note in enumerate(note_list):
        if search_note.get("id") == note_id_delete:
            index_note = index
            flag = False

    if flag:
        print("There is no note with this ID.")
        return

    print('-' * 50)
    print(f"[{note_list[index_note].get('id')}] {note_list[index_note].get('title')}")
    print(f"  {note_list[index_note].get('content')}")
    print('-' * 50)

    note_list.pop(index_note)

    with open(note_file, 'w', encoding="utf-8") as write_mood:
        for note in note_list:
            json.dump(note, write_mood)
            write_mood.write("\n")

    print("\nNote Has Been Deleted Successfully.")

    return
