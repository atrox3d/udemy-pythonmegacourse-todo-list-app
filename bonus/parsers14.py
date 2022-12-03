def parse_feet_inches(feet_inches):
    parts = feet_inches.split(" ")
    feet, inches = [float(n) for n in parts]
    return feet, inches
