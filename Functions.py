def collision_cursor(a_x, a_y, a_width, a_height, b_x, b_y):
    if a_x - 10 < b_x < a_x + a_width + 10 and a_y - 10 < b_y < a_y + a_height + 10:
        return True
    else:
        return False
