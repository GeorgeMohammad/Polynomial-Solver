import numpy

coefficients = []
exitStr = ""
while (exitStr.lower() != "q"):
    errorFlag = True
    while (errorFlag):
        coefficientVal = input("Enter a coefficient. If a term is missing," \
"put a zero. ie. the exponent decreases by more than 1: ")
        try:
            int(coefficientVal)
        except:
            print ("Try Again")
        else:
            errorFlag = False
    coefficients.append(coefficientVal)
    exitStr = input("Enter q to quit or anything else to continue")

solution = numpy.roots(coefficients)
print(solution)

