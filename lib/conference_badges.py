def badge_maker(name):
    badge = f"Hello, my name is {name}."
    return badge

def batch_badge_creator(names):
    badges = list()
    for n in range(0, len(names)):
        badges.append(badge_maker(names[n]))
    return badges

def assign_rooms(names):
    rooms = list()
    for n in range(0, len(names)):
        rooms.append(f"Hello, {names[n]}! You'll be assigned to room {n+1}!")
    return rooms

def printer(names):
    print(*batch_badge_creator(names), sep = "\n")
    print(*assign_rooms(names), sep = "\n")
