def convert_to_amps(reading):
    if reading == 4095:
        return None
    return round(10 * reading / 4094)


def convert_to_current(adc_reading):
    current = (adc_reading / 1023) * 30 - 15
    return round(abs(current))