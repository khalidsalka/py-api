import requests
import json

print("Available categories:")
available_categories = ["animal", "career", "celebrity", "dev", "fashion"]
for i in range(len(available_categories)):
    print(f"{i+1}){available_categories[i]}")

categories_chosen = {}


def intro():
    try:
        if len(categories_chosen) > 0:
            print(
                f"Categories you already selected: {categories_chosen}")
        categoryNumber = int(
            input("Enter the number of your joke category of choice: "))
        NoJ = int(
            input("How many jokes you want in this category (Only numbers are accepted): "))
        if (categoryNumber > 5 or categoryNumber < 1):
            raise Exception(
                f"Sorry, choose a valid category number (1-{len(available_categories)})")
        if available_categories[categoryNumber-1] in categories_chosen:
            raise Exception(
                f"You already selected that category, please select a different one.")
        categories_chosen[available_categories[categoryNumber-1]] = NoJ
    except ValueError:
        print("Only Numbers are excepted")
        intro()
    except Exception as error:
        print(error)
        intro()


def second():
    try:
        decision = str(input(
            "Do you want to add another category to your selection? Valid options are (y/n): ")).lower()
        if (decision != "y" and decision != "n"):
            raise Exception(
                f"Sorry, enter 'n' for No or 'y' for Yes")
        if (decision == 'y'):
            intro()
            second()

    except Exception as error:
        print(error)
        second()


def main():
    intro()
    second()

    data = {}
    for key in categories_chosen:
        category = []
        for j in range(categories_chosen[key]):
            url = f"https://api.chucknorris.io/jokes/random?category={key}"

            response = requests.get(url).json()
            joke = {"Joke": response["value"],
                    "Number of Characters": len(response["value"])}
            category.append(joke)
        data[key] = category
    print(data)


main()


# print(available_categories)
#     continue_or_not = input("Do you want to add another category to your selection? (y/n): ")
#     categories.append = int(input("Enter the number of the category of choice: "))

# categories_chosen = [Category1, Category2]
# NoJ = int(input("How many jokes: "))

# for i in range(NoJ):
#   url = f"https://api.chucknorris.io/jokes/random?category={categories_chosen[i]}"

#   response = requests.get(url).json()
#   print(f'\n{categories_chosen[i]} joke: {response["value"]}\n')

#   # url2 = f"https://api.chucknorris.io/jokes/random?category={categories_chosen[i]}"

#   # response = requests.get(url2).json()
#   # print(f'{Category2} joke: {response["value"]}')


# arr = []

# while(True):
#   x = input("Enter your joke category of choice: ")
#   arr.append(x)
#   res = input("Would you like to select another category? select Y for yes and N for no")
#   if (res == "Y"):
#     continue
#   elif (res == "N"):
#     break
#   else:
#     print("Invalid Input")
#     input("Would you like to select another category? select Y for yes and N for no")

# print("Available categories:\n 1)animal\n 2)career\n 3)celebrity\n 4)dev\n 5)explicit\n 6)fashion\n 7)food\n 8)history\n 9)money\n 10)movie\n 11)music\n 12)political\n 13)religion\n 14)science\n 15)sport\n 16)ravel\n")
