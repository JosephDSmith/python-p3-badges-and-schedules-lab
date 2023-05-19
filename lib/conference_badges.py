def badge_maker(name):
    return f'Hello, my name is {name}.'


def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(f'Hello, my name is {name}.')
    return badge_messages

def assign_rooms(names):
    rooms = range(1, 9)
    room_assignments = []
    for room in rooms:
        room_assignments.append(f"Hello, {names[room -1]}! You'll be assigned to room {room}!")
           
    return room_assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    for greeting in assign_rooms(names):
        print(greeting)


    

