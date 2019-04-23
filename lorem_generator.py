#------------------------------------------ EJERCICIO 8 lorem_generator.py

import sys

print(sys.argv[0])
print(sys.argv[1])
paramotroUrl = int(sys.argv[1])
i=1

loremNisum= "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus auctor ligula et tellus imperdiet, nec luctus risus pulvinar. Vestibulum odio sem, imperdiet et neque ac, tempus rhoncus odio. Etiam sollicitudin urna mi, at vestibulum nulla accumsan et. In ultricies sagittis lobortis. Quisque eleifend, felis id imperdiet bibendum, felis quam vulputate eros, non suscipit tellus orci vitae ex. Maecenas semper varius lobortis. Curabitur eu lorem ut dui molestie fermentum sed et nulla."

while i <= paramotroUrl:
    print("{} \n".format(loremNisum))
    i +=1

