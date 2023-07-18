def scale_font_size(font_size):
    if font_size > 30:
        return 30
    elif font_size < 10:
        return 10
    else:
        return font_size
