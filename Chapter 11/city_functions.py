def citycountry(city, country, population=''):
    """Generates a grammatical formatted City, Country, & population."""
    if population:
        name = f"{city.title()}, {country.title()} - population {population}"
        # return name.title()
        return name
    else:    
        name = f"{city}, {country}"
        return name.title()


# print(citycountry('daygo', 'united states', 500000))