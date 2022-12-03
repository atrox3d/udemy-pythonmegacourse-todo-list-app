def parse_feet_inches(feet_inches):
    parts = feet_inches.split(" ")
    feet, inches = [float(n) for n in parts]
    return feet, inches


def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters


feet, inches = parse_feet_inches("3 12")
meters = convert(feet, inches)

print(f"{feet} feet and {inches} inches is equal to {meters} meters")
if meters < 1:
    print("kid too small")
else:
    print("kid can use the slide")


