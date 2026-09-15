import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """ serialize animal output """
    name = animal.get('name', 'Unbekannt')
    locations = animal.get('locations', [])[0]
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'N/A')
    animal_type = characteristics.get('type', 'N/A')
    animal_temperament = characteristics.get('temperament', 'N/A')
    animal_skin_type = characteristics.get('skin_type', 'N/A')

    output = '<li class="cards__item">'
    output += f"<div class=\"card__title\">{name}</div>"
    output += f"<div class =\"card__text\" >"
    output += f"<ul>"
    output += f"<li><strong>Diet:</strong> {diet}</li>"
    output += f"<li><strong>Location:</strong> {locations}</li>"
    output += f"<li><strong>Type:</strong> {animal_type}</li>"
    output += f"<li><strong>Temperament:</strong> {animal_temperament}</li>"
    output += f"<li><strong>Skin type:</strong> {animal_skin_type}</li>"
    output += f"</ul>"
    output += "</div>"
    output += '</li>'

    return output


animals_data = load_data('animals_data.json')

output = ''
for animal in animals_data:
    output += serialize_animal(animal)

with open('animals_template.html', 'r') as file:
    template = file.read()

template = template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as file:
    file.write(template)
