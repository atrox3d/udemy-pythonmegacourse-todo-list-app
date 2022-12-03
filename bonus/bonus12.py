def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet, inches = [float(n) for n in parts]

    meters = feet * 0.3048 + inches * 0.0254
    return meters


result = convert("3 12")
if result < 1:
    print("kid too small")
else:
    print("kid can use the slide")


