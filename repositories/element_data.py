from rest.models import Element
import json

with open('repositories/elements.json') as f:
    elements = json.load(f)
    print(elements)

    for i in elements:
        Element.objects.create(**i)
