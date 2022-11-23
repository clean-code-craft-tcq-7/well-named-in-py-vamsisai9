def printEventColorCode(MINOR_COLORS,MAJOR_COLORS):

    colorCodeCount = 1

    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            print(f"Color Code for {major_color}/{minor_color} is : {colorCodeCount}")
            colorCodeCount+=1
