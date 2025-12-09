spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(foods):
    """
    Return a list of names from the list of foods.
    """
    return [food["name"] for food in foods]


def get_spiciest_foods(foods):
    """
    Return foods with heat_level greater than 5.
    """
    return [food for food in foods if food["heat_level"] > 5]


def print_spicy_foods(foods):
    """
    Print each food in the format:
    Name (Cuisine) | Heat Level: 🌶🌶🌶
    """
    for food in foods:
        heat = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat}')


def get_spicy_food_by_cuisine(foods, cuisine):
    """
    Return a single food whose cuisine matches.
    """
    for food in foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(foods):
    """
    Print only foods with heat_level > 5.
    """
    spicy = get_spiciest_foods(foods)
    print_spicy_foods(spicy)


def get_average_heat_level(foods):
    """
    Return the average heat level as an integer.
    """
    total = sum(food["heat_level"] for food in foods)
    return total // len(foods)


def create_spicy_food(foods, new_food):
    """
    Add a new spicy food to the list and return the list.
    """
    foods.append(new_food)
    return foods
