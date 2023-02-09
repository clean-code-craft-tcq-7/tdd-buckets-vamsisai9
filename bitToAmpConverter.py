def convert_to_amps(reading):
    if reading == 4095:
        return None
    return round(10 * reading / 4094)


def convert_to_current(a2d_reading):
    current = (a2d_reading / 1023) * 30 - 15
    return round(abs(current))