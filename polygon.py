class Polygon:
    pass

    def __init__(self, sides, color='piros'):  # önmagára mutató pointer
        self.sides = sides
        self.color = color
        self.oldalszelesseg = 2
        print('This is a polygon')


class Triangle:
    pass


my_polygon = Polygon(4, 'zöld')
print(f"Ennek a polygonnak {my_polygon.sides} oldala van és a színe {my_polygon.color}")
print(id(my_polygon))

your_polygon = Polygon(6, 'kék')
print(f"Ennek a polygonnak {your_polygon.sides} oldala van és a színe {your_polygon.color}")
print(id(your_polygon))

third_polygon = Polygon(5)
print(f"Ennek a polygonnak {third_polygon.sides} oldala van, a színe {third_polygon.color} és oldalainak szélessége {third_polygon.oldalszelesseg}")