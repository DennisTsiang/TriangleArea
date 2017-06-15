from sys import argv

def calculateArea(base, height):
	print("Calculating area...")
    return (base*height)/2


if __name__ == "__main__":
     script, base_str, height_str = argv
     base = int(base_str)
     height = int(height_str)
     print("You enter base: %d height: %d" % (base, height))
     print("Area: %d" % (calculateArea(base, height)))
