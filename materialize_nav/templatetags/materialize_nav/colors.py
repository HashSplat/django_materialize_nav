import colorsys

from .base import register


COLORS = {
    "red lighten-5": "#ffebee", "red lighten-4": "#ffcdd2", "red lighten-3": "#ef9a9a", "red lighten-2": "#e57373",
    "red lighten-1": "#ef5350", "red": "#f44336", "red darken-1": "#e53935", "red darken-2": "#d32f2f",
    "red darken-3": "#c62828", "red darken-4": "#b71c1c", "red accent-1": "#ff8a80", "red accent-2": "#ff5252",
    "red accent-3": "#ff1744", "red accent-4": "#d50000",

    "pink lighten-5": "#fce4ec", "pink lighten-4": "#f8bbd0", "pink lighten-3": "#f48fb1", "pink lighten-2": "#f06292",
    "pink lighten-1": "#ec407a", "pink": "#e91e63", "pink darken-1": "#d81b60", "pink darken-2": "#c2185b",
    "pink darken-3": "#ad1457", "pink darken-4": "#880e4f", "pink accent-1": "#ff80ab", "pink accent-2": "#ff4081",
    "pink accent-3": "#f50057", "pink accent-4": "#c51162",

    "purple lighten-5": "#f3e5f5", "purple lighten-4": "#e1bee7", "purple lighten-3": "#ce93d8",
    "purple lighten-2": "#ba68c8", "purple lighten-1": "#ab47bc", "purple": "#9c27b0", "purple darken-1": "#8e24aa",
    "purple darken-2": "#7b1fa2", "purple darken-3": "#6a1b9a", "purple darken-4": "#4a148c",
    "purple accent-1": "#ea80fc", "purple accent-2": "#e040fb", "purple accent-3": "#d500f9",
    "purple accent-4": "#aa00ff",

    "deep-purple lighten-5": "#ede7f6", "deep-purple lighten-4": "#d1c4e9", "deep-purple lighten-3": "#b39ddb",
    "deep-purple lighten-2": "#9575cd", "deep-purple lighten-1": "#7e57c2", "deep-purple": "#673ab7",
    "deep-purple darken-1": "#5e35b1", "deep-purple darken-2": "#512da8", "deep-purple darken-3": "#4527a0",
    "deep-purple darken-4": "#311b92", "deep-purple accent-1": "#b388ff", "deep-purple accent-2": "#7c4dff",
    "deep-purple accent-3": "#651fff", "deep-purple accent-4": "#6200ea",

    "indigo lighten-5": "#e8eaf6", "indigo lighten-4": "#c5cae9", "indigo lighten-3": "#9fa8da",
    "indigo lighten-2": "#7986cb", "indigo lighten-1": "#5c6bc0", "indigo": "#3f51b5", "indigo darken-1": "#3949ab",
    "indigo darken-2": "#303f9f", "indigo darken-3": "#283593", "indigo darken-4": "#1a237e",
    "indigo accent-1": "#8c9eff", "indigo accent-2": "#536dfe", "indigo accent-3": "#3d5afe",
    "indigo accent-4": "#304ffe",

    "blue lighten-5": "#e3f2fd", "blue lighten-4": "#bbdefb", "blue lighten-3": "#90caf9", "blue lighten-2": "#64b5f6",
    "blue lighten-1": "#42a5f5", "blue": "#2196f3", "blue darken-1": "#1e88e5", "blue darken-2": "#1976d2",
    "blue darken-3": "#1565c0", "blue darken-4": "#0d47a1", "blue accent-1": "#82b1ff", "blue accent-2": "#448aff",
    "blue accent-3": "#2979ff", "blue accent-4": "#2962ff",

    "light-blue lighten-5": "#e1f5fe", "light-blue lighten-4": "#b3e5fc", "light-blue lighten-3": "#81d4fa",
    "light-blue lighten-2": "#4fc3f7", "light-blue lighten-1": "#29b6f6", "light-blue": "#03a9f4",
    "light-blue darken-1": "#039be5", "light-blue darken-2": "#0288d1", "light-blue darken-3": "#0277bd",
    "light-blue darken-4": "#01579b", "light-blue accent-1": "#80d8ff", "light-blue accent-2": "#40c4ff",
    "light-blue accent-3": "#00b0ff", "light-blue accent-4": "#0091ea",

    "cyan lighten-5": "#e0f7fa", "cyan lighten-4": "#b2ebf2", "cyan lighten-3": "#80deea", "cyan lighten-2": "#4dd0e1",
    "cyan lighten-1": "#26c6da", "cyan": "#00bcd4", "cyan darken-1": "#00acc1", "cyan darken-2": "#0097a7",
    "cyan darken-3": "#00838f", "cyan darken-4": "#006064", "cyan accent-1": "#84ffff", "cyan accent-2": "#18ffff",
    "cyan accent-3": "#00e5ff", "cyan accent-4": "#00b8d4",

    "teal lighten-5": "#e0f2f1", "teal lighten-4": "#b2dfdb", "teal lighten-3": "#80cbc4", "teal lighten-2": "#4db6ac",
    "teal lighten-1": "#26a69a", "teal": "#009688", "teal darken-1": "#00897b", "teal darken-2": "#00796b",
    "teal darken-3": "#00695c", "teal darken-4": "#004d40", "teal accent-1": "#a7ffeb", "teal accent-2": "#64ffda",
    "teal accent-3": "#1de9b6", "teal accent-4": "#00bfa5",

    "green lighten-5": "#e8f5e9", "green lighten-4": "#c8e6c9", "green lighten-3": "#a5d6a7",
    "green lighten-2": "#81c784", "green lighten-1": "#66bb6a", "green": "#4caf50", "green darken-1": "#43a047",
    "green darken-2": "#388e3c", "green darken-3": "#2e7d32", "green darken-4": "#1b5e20", "green accent-1": "#b9f6ca",
    "green accent-2": "#69f0ae", "green accent-3": "#00e676", "green accent-4": "#00c853",

    "light-green lighten-5": "#f1f8e9", "light-green lighten-4": "#dcedc8", "light-green lighten-3": "#c5e1a5",
    "light-green lighten-2": "#aed581", "light-green lighten-1": "#9ccc65", "light-green": "#8bc34a",
    "light-green darken-1": "#7cb342", "light-green darken-2": "#689f38", "light-green darken-3": "#558b2f",
    "light-green darken-4": "#33691e", "light-green accent-1": "#ccff90", "light-green accent-2": "#b2ff59",
    "light-green accent-3": "#76ff03", "light-green accent-4": "#64dd17",

    "lime lighten-5": "#f9fbe7", "lime lighten-4": "#f0f4c3", "lime lighten-3": "#e6ee9c", "lime lighten-2": "#dce775",
    "lime lighten-1": "#d4e157", "lime": "#cddc39", "lime darken-1": "#c0ca33", "lime darken-2": "#afb42b",
    "lime darken-3": "#9e9d24", "lime darken-4": "#827717", "lime accent-1": "#f4ff81", "lime accent-2": "#eeff41",
    "lime accent-3": "#c6ff00", "lime accent-4": "#aeea00",

    "yellow lighten-5": "#fffde7", "yellow lighten-4": "#fff9c4", "yellow lighten-3": "#fff59d",
    "yellow lighten-2": "#fff176", "yellow lighten-1": "#ffee58", "yellow": "#ffeb3b", "yellow darken-1": "#fdd835",
    "yellow darken-2": "#fbc02d", "yellow darken-3": "#f9a825", "yellow darken-4": "#f57f17",
    "yellow accent-1": "#ffff8d", "yellow accent-2": "#ffff00", "yellow accent-3": "#ffea00",
    "yellow accent-4": "#ffd600",

    "amber lighten-5": "#fff8e1", "amber lighten-4": "#ffecb3", "amber lighten-3": "#ffe082",
    "amber lighten-2": "#ffd54f", "amber lighten-1": "#ffca28", "amber": "#ffc107", "amber darken-1": "#ffb300",
    "amber darken-2": "#ffa000", "amber darken-3": "#ff8f00", "amber darken-4": "#ff6f00", "amber accent-1": "#ffe57f",
    "amber accent-2": "#ffd740", "amber accent-3": "#ffc400", "amber accent-4": "#ffab00",

    "orange lighten-5": "#fff3e0", "orange lighten-4": "#ffe0b2", "orange lighten-3": "#ffcc80",
    "orange lighten-2": "#ffb74d", "orange lighten-1": "#ffa726", "orange": "#ff9800", "orange darken-1": "#fb8c00",
    "orange darken-2": "#f57c00", "orange darken-3": "#ef6c00", "orange darken-4": "#e65100",
    "orange accent-1": "#ffd180", "orange accent-2": "#ffab40", "orange accent-3": "#ff9100",
    "orange accent-4": "#ff6d00",

    "deep-orange lighten-5": "#fbe9e7", "deep-orange lighten-4": "#ffccbc", "deep-orange lighten-3": "#ffab91",
    "deep-orange lighten-2": "#ff8a65", "deep-orange lighten-1": "#ff7043", "deep-orange": "#ff5722",
    "deep-orange darken-1": "#f4511e", "deep-orange darken-2": "#e64a19", "deep-orange darken-3": "#d84315",
    "deep-orange darken-4": "#bf360c", "deep-orange accent-1": "#ff9e80", "deep-orange accent-2": "#ff6e40",
    "deep-orange accent-3": "#ff3d00", "deep-orange accent-4": "#dd2c00",

    "brown lighten-5": "#efebe9", "brown lighten-4": "#d7ccc8", "brown lighten-3": "#bcaaa4",
    "brown lighten-2": "#a1887f", "brown lighten-1": "#8d6e63", "brown": "#795548", "brown darken-1": "#6d4c41",
    "brown darken-2": "#5d4037", "brown darken-3": "#4e342e", "brown darken-4": "#3e2723",

    "grey lighten-5": "#fafafa", "grey lighten-4": "#f5f5f5", "grey lighten-3": "#eeeeee", "grey lighten-2": "#e0e0e0",
    "grey lighten-1": "#bdbdbd", "grey": "#9e9e9e", "grey darken-1": "#757575", "grey darken-2": "#616161",
    "grey darken-3": "#424242", "grey darken-4": "#212121",

    "blue-grey lighten-5": "#eceff1", "blue-grey lighten-4": "#cfd8dc", "blue-grey lighten-3": "#b0bec5",
    "blue-grey lighten-2": "#90a4ae", "blue-grey lighten-1": "#78909c", "blue-grey": "#607d8b",
    "blue-grey darken-1": "#546e7a", "blue-grey darken-2": "#455a64", "blue-grey darken-3": "#37474f",
    "blue-grey darken-4": "#263238",


    "black": "#000000", "white": "#ffffff", "A transparent": "N",
}


def get_rgb(color):
    if isinstance(color, str):
        if not color.startswith("#"):
            if color not in COLORS:
                raise ValueError("Invalid color name given!")
            color = COLORS[color]
        color = color[1:]
        length = len(color)
        if length == 3 or length == 4:
            color = tuple(int(c*2, 16) for c in color)
        elif length == 6 or length == 8:
            color = tuple(int(color[i:i+2], 16) for i in range(0, len(color), 2))
        else:
            raise ValueError("Invalid hex color given!")

    color = tuple(color)
    length = len(color)
    if length < 3:
        raise ValueError("Invalid color given! Color must be 3 RGB values.")
    elif length == 3:
        color = color + (255, )
    return color[:4]


def modify_val(val, modify_by=0.0, should_modify=True, upper_lim=1, lower_lim=0):
    """Modify a value and check its range."""
    if should_modify:
        val = val + modify_by
    if val > upper_lim:
        return upper_lim
    elif val < lower_lim:
        return lower_lim
    else:
        return val


def lighten(color, amount):
    """Lighten a color by a percentage and return the color in Hex.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float/int): Number between 0 and 100

    Return:
        new_color (str): New color as a hex value.
    """
    percent = amount/100  # Convert to a percentage
    color = get_rgb(color)
    hls = colorsys.rgb_to_hls(*(c/255 for c in color))

    new_hls = (modify_val(c, percent, i == 1) for i, c in enumerate(hls))

    new_rgb = colorsys.hls_to_rgb(*new_hls)
    new_rgb = (int(c * 255) for c in new_rgb)

    return "#{:02x}{:02x}{:02x}{:02x}".format(*new_rgb)


def darken(color, amount):
    """Darken a color by a percentage and return the color in Hex.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float/int): Number between 0 and 100

    Return:
        new_color (str): New color as a hex value.
    """
    return lighten(color, -amount)


def saturate(color, amount):
    """Saturate a color by a percentage and return the color in Hex.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float/int): Number between 0 and 100

    Return:
        new_color (str): New color as a hex value.
    """
    percent = amount/100  # Convert to a percentage
    color = get_rgb(color)
    hls = colorsys.rgb_to_hls(*(c/255 for c in color))

    new_hls = (modify_val(c, percent, i == 2) for i, c in enumerate(hls))

    new_rgb = colorsys.hls_to_rgb(*new_hls)
    new_rgb = (int(c * 255) for c in new_rgb)

    return "#{:02x}{:02x}{:02x}{:02x}".format(*new_rgb)


def desaturate(color, amount):
    """Desaturate a color by a percentage and return the color in Hex.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float/int): Number between 0 and 100

    Return:
        new_color (str): New color as a hex value.
    """
    return saturate(color, -amount)


def opacify(color, amount):
    """Increase the opacity of a color.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float): Number between 0 and 1

    Return:
        new_color (str): New color as a hex value.
    """
    color = get_rgb(color)
    new_color = (modify_val(c, amount, i == 4) for i, c in enumerate(color))
    return "#{:02x}{:02x}{:02x}{:02x}".format(*new_color)


def transparentize(color, amount):
    """Increase the transparency of a color.

    Args:
        color(str/tuple): Hex or rgb color values
        amount (float): Number between 0 and 1

    Return:
        new_color (str): New color as a hex value.
    """
    return opacify(color, -amount)

def set_opacity(color, amount):
    color = get_rgb(color)[:3] + (amount, )
    new_color = (modify_val(c, 0, False) for i, c in enumerate(color))
    return "#{:02x}{:02x}{:02x}{:02x}".format(*new_color)


def to_rgb(color):
    color = get_rgb(color)
    return "rgb" + str(color)[:3]

def to_rgba(color):
    color = get_rgb(color)
    return "rgba" + str(color)[:4]


@register.inclusion_tag("materialize_nav/colors/dynamic_css.html")
def include_custom_color(primary_color=None, primary_color_light=None, primary_color_dark=None,
                         secondary_color=None, success_color=None, error_color=None, link_color=None):
    change = {}
    if primary_color:
        if primary_color_light is None:
            primary_color_light = lighten(primary_color, 15)
        if primary_color_dark is None:
            primary_color_dark = darken(primary_color, 15)

        # ===== Primary Color =====
        change["primary_color"] = primary_color
        change["tabs_text_color"] = primary_color
        change["tabs_text_color_active"] = to_rgba(get_rgb(primary_color)[:3] + (0.7,))
        change["tabs_text_color_disabled"] = to_rgba(get_rgb(primary_color)[:3] + (0.4,))
        change["footer_bg_color"] = primary_color

        # ===== Lighten =====
        change["primary_color_light"] = primary_color_light
        change["tabs_underline_color"] = primary_color_light

        # ===== Darken =====
        change["primary_color_dark"] = primary_color_dark

    if secondary_color:
        change["secondary_color"] = secondary_color

        change["badge_bg_color"] = secondary_color

        change["button_background_focus"] = lighten(secondary_color, 4)
        change["button_raised_background"] = lighten(secondary_color, 5)
        change["button_raised_background_hover"] = lighten(change["button_raised_background"], 5)
        change["button_floating_background"] = secondary_color
        change["button_floating_background_hover"] = change["button_floating_background"]

        change["datepicker_weekday_bg"] = darken(secondary_color, 7)
        change["datepicker_date_bg"] = secondary_color
        change["datepicker_selected"] = secondary_color
        change["datepicker_selected_outfocus"] = desaturate(lighten(secondary_color, 35), 15)
        change["datepicker_day_focus"] = transparentize(desaturate(secondary_color, 5), .75)

        change["dropdown_color"] = secondary_color

        change["input_focus_color"] = secondary_color

        change["radio_fill_color"] = secondary_color
        change["radio_border"] = "2px solid " + change["radio_fill_color"]

        change["select_focus"] = "1px solid " + lighten(secondary_color, 47)

        change["switch_bg_color"] = secondary_color
        change["switch_checked_lever_bg"] = desaturate(lighten(change["switch_bg_color"], 25), 25)

        change["spinner_default_color"] = secondary_color

        change["collection_active_bg_color"] = secondary_color
        change["collection_active_color"] = lighten(secondary_color, 55)
        change["collection_link_color"] = secondary_color

        change["progress_bar_color"] = secondary_color

    if success_color:
        change["success_color"] = success_color
        change["input_success_color"] = success_color

    if error_color:
        change["error_color"] = error_color
        change["input_error_color"] = error_color
        change["input_invalid_border"] = "1px solid " + error_color

    if link_color:
        change["link_color"] = link_color

    return change


"""
Notes:
primary_color:
    tabs-text-color
    footer-bg-color

primary_color_light:
    tabs-underline-color
    
primary_color_dark:

secondary_color:
    badge-bg-color
    
    button-background-focus -> lighten(4)
    button-raised-background -> lighten(5)
        button-raised-background-hover -> lighten(5)
    button-floating-background
    
    datepicker-weekday-bg -> darken(7)
    datepicker-date-bg
    datepicker-selected
    datepicker-selected-outfocus -> desaturate(lighten(35), 15)
    datepicker-day-focus  transparentize(desaturate(5), .75)
    
    dropdown-color
    
    input-focus-color

    radio-fill-color
    
    select-focus -> 1px solid lighten($secondary-color, 47%) !default;
    
    switch-bg-color
    switch-checked-lever-bg -> desaturate(lighten($switch-bg-color, 25%), 25%) !default;
    
    spinner-default-color
    
    collection-active-bg-color
    collection-active-color: lighten($secondary-color, 55%)
    collection-link-color
    
    progress-bar-color

success_color:
    input-success-color
    
error_color:
    input-error-color

link_color:


"""
