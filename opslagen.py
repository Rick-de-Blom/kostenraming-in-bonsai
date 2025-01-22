markups = [
    {"description": "Algemene bedrijfskosten", "percentage": 9},
    {"description": "Garanties", "percentage": 2},
    {"description": "Werkvoorbereiding", "percentage": 2},
    {"description": "Winst", "percentage": 7},
    {"description": "Risico", "percentage": 5},
    {"description": "CAR", "percentage": 0.5}
]

def calculate_markups(total_building_cost):
    total_markup = 0
    markup_values = []

    # Bereken de waarde van de markups tot en met Werkvoorbereiding
    for markup in markups:
        if markup["description"] in ["Winst", "Risico", "CAR"]:
            # Stop met de berekening voor deze markups
            break
        value = total_building_cost * (markup["percentage"] / 100)
        markup_values.append({"description": markup["description"], "percentage": markup["percentage"], "value": value})
        total_markup += value

    # Bereken de totaalsom na Werkvoorbereiding
    total_after_preparation = total_building_cost + total_markup

    # Bereken de waarde van Winst, Risico en CAR
    for markup in markups:
        if markup["description"] in ["Winst", "Risico", "CAR"]:
            value = total_after_preparation * (markup["percentage"] / 100)
            markup_values.append({"description": markup["description"], "percentage": markup["percentage"], "value": value})
            total_markup += value

    return markup_values, total_markup