def collision_cursor(a, b):
    if a.x - 10 < b.pos[
        0] < a.x + a.text.get_width() + 10 and a.y - 10 < b.pos[1] < a.y + a.text.get_height() + 10:
        return True
    else:
        return False
