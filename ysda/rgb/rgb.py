import re
from math import floor


def parse_color(color: str) -> [int]:
    color = color.replace(' ', '')
    if re.match("\\d+,\\d+,\\d+$", color):
        rgb_components = [int(component) for component in re.split(',', color)]

        for component in rgb_components:
            if component > 255 or len(rgb_components) > 3:
                return None
        return rgb_components

    elif re.match('#([a-f]|[A-F]|[1-9]){6}$', color):
        return [int(color[i + 1:i + 3], 16) for i in range(0, len(color) - 2, 2)]

    elif re.match('[rgb]{3}\\(\\d+,\\d+,\\d+\\)$', color):
        colors, numbers = re.split('\\(', color[:-1])
        numbers = [int(component) for component in re.split(',', numbers)]

        for component in numbers:
            if component > 255:
                return None

        components = dict(zip(colors, numbers))
        return [components['r'], components['g'], components['b']]

    elif re.match('[rgb]{3}\\((\\d{1,2}|100)%,(\\d{1,2}|100)%,(\\d{1,2}|100)%\\)$', color):
        colors, numbers = re.split('\\(', color[:-1])
        numbers = numbers.replace(',', '')
        numbers = [floor(int(component) * 255 / 100.0) for component in re.split('%', numbers)[:-1]]
        components = dict(zip(colors, numbers))
        return [components['r'], components['g'], components['b']]

    return None
