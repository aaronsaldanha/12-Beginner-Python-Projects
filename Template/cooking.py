def madlib():
    seasoning1 = input('Seasoning1: ')
    vegetable = input('Vegetable: ')
    fish = input('Fish: ')
    body_part1 = input('Body Part1: ')
    size = input('Size: ')
    body_part2 = input('Body Part2: ')
    seasoning2 = input('Seasoning2: ')
    seasoning3 = input('Seasoning3: ')

    madlib = f"Traditional Sushi Roll\
Step 1: Prepare sushi rice by mixing cooked short-grain rice with seasoned {seasoning1}.\n\
Step 2: Cut both ends of the {vegetable} and peel it. Now cut it in half lengthwise and repeat to get 4 strips. Remove the seeds and cut again to get 8 pieces in total.\n\
Step 3: Cut out thin slices of raw {fish}, about 1/4- 1/2 inches thick. Make long stripes.\n\
Step 4: Place the bamboo mat on a flat surface and cover it with a plastic sheet. Now put the Nori sheet on the bamboo mat.\n\
Step 5: Moisten your {body_part1}. Take a {size} ball of sushi rice in your hands and spread an even layer on the Nori. Use your {body_part2} to apply gentle pressure and keep a half-inch space on all sides\n\
Step 6: Now add {vegetable} and {fish} strips in the middle section of the rice. If the {fish} or {vegetable} pieces are short, you may add extra pieces lined up to cover the Nori sheet’s length.\n\
Step 7: Roll the bamboo mat away from you to create a tight and compact log. Keep pressing slightly as you roll to ensure that the vegetables stick together properly. Apply a few drops of water on the edges and seal it.\n\
Step 8: Moisten the knife and cut the roll into 6-8 pieces. Serve with {seasoning2} and {seasoning3}. Repeat the steps for remaining vegetables.\n"

    print(madlib)
