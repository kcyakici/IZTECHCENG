def fatCalories(fat):

    calories = 9 * fat
    return calories

def carbohydrateCalories(carbohydrate):

    calories = carbohydrate * 4
    return calories


def main():

    fatGrams = float(input("Enter the fat eaten in grams: "))
    carbohydrateGrams = float(input("Enter the carbohydrate in grams: "))
    
    fatCal = fatCalories(fatGrams)
    carboCal = carbohydrateCalories(carbohydrateGrams)

    print(f"Calories gained with fat: {fatCal}\nCalories gained by carbohydrates: {carboCal}")


if __name__ == "__main__":
    main()