from bonus.converters14 import convert
from parsers14 import parse_feet_inches

feet, inches = parse_feet_inches("3 12")
meters = convert(feet, inches)

print(f"{feet} feet and {inches} inches is equal to {meters} meters")
if meters < 1:
    print("kid too small")
else:
    print("kid can use the slide")


