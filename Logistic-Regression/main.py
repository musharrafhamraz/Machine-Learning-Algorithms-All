data_dict = {
    'cap-diameter': None,
    'cap-shape': None,
    'gill-attachment': None,
    'gill-color': None,
    'stem-height': None,
    'stem-width': None,
    'stem-color': None,
    'season': None
}

# Prompt the user to input values for each key
for key in data_dict:
    value = input(f"Enter value for {key}: ")
    
    # Convert numeric inputs to float
    try:
        value = float(value)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        value = input(f"Enter value for {key}: ")
    
    # Assign the input value to the corresponding key in the dictionary
    data_dict[key] = value

print("Data dictionary:", data_dict)
