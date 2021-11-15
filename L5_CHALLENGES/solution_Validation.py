def validate(code):
    lines = code.split("\n")
    firstLine = lines[0]

    i = 0
    for line in lines:
        if line == "":
            lines.pop(i)
        i += 1

    print(lines)

    if not firstLine.startswith("def"):
        return "Missing function definition"

    if not firstLine.startswith("def validate"):
        return "Wrong Name"

    firstParamIndex = 0
    arguments = []
    
    for lineIndex in range(len(firstLine)):
        if firstLine[lineIndex] == "(":
            firstParamIndex = lineIndex
            if firstLine[lineIndex+1] == ")":
                return "Missing Paren"

        elif firstLine[lineIndex] == ")":
            argumentString = firstLine[firstParamIndex+1:lineIndex]
            arguments = argumentString.split(",")

            if lineIndex+1 >= len(firstLine) or not firstLine[lineIndex+1] == ":":
                return "Missing :"

    print(arguments)

    newLineIndex = 0

    for line in lines:
        if newLineIndex > 0:
            if not line.startswith("    "):
                print(line)
                return "Missing Indentation on line "+str(newLineIndex)
        newLineIndex += 1

    retFound = False
    
    for line in lines:
        if "return" in line:
            retFound = True

    if not retFound:
        return "Missing Return"

    return "Code Valid"

string = """def validate(a,b):
    print(one + two)
    newVar = one + two * 3
    return newVar
"""

print(validate(string))

    
