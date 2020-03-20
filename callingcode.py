#Jake Eaton
#Call Characters and Items

def Call():
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        for person in inhabitant:
            person.describe()

    items = current_room.get_item()
    if items is not None:
        for item in items:
            item.describe()

    print("")
