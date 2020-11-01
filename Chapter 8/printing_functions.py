# Start with some designs that need to be printed.
def printfx(*design):
    unprinted_designs = [*design]
    complete_models = []

    # Simulating printing each design, until none are left.
    # Move each design to completed_models after printing.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        complete_models.append(current_design)

    # Display all completed models.
    print("\nThe following models have been printed:" )
    for complete_model in complete_models:
        print(complete_model)

