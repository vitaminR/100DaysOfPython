def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    while front_is_clear():
        if not wall_on_right():
            turn_right()
            move()
        elif wall_on_right() and front_is_clear():
            move()    
    while wall_in_front() and not at_goal():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
            move()
        