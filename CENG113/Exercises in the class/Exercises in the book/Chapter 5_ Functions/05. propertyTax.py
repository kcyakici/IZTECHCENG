def assessmentValue(actualValue):

    assessmentValue = 0.6 * actualValue
    return assessmentValue

def propertyTax(assessmentValue):

    propertyTax = assessmentValue / 100 * 0.72
    return propertyTax


def main():

    actualValue = float(input("Enter the actual value of the property: "))
    assessment = assessmentValue(actualValue)
    tax = propertyTax(assessment)

    print(assessment, tax)


if __name__ == "__main__":
    main()