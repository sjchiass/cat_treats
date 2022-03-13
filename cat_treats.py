import random
import argparse

# argparse lets you add arguments to your python script
# For example, the user can do `python cat_treats.py -f index.html -k 25 --replacement` to
# sample 25 treat locations with replacement, saving the output to index.html
parser = argparse.ArgumentParser(description="Sample locations to put cat treats")
parser.add_argument("-f", "--output_file", type=str, help="location of file to output", default="./index.html")
parser.add_argument("-k", "--size", type=int, help="size of sample", default=10)
parser.add_argument("-r", "--replacement", action="store_true", help="whether to sample with replacement")

# This command will save the user's arguments in `args`
# The code can then access the sample size through `args.size`
args = parser.parse_args()

# This is a nested dictionary, with lists as the lowest level
# You can get all of the living room locations by accessing `treats["Living room"]`
# The indentation is not necessary but it makes the code easier to read.
treats = {
    "Living room" : {
        "Grey cat tree" : [
            "ground level",
            "in house",
            "behind house",
            "top of house",
            "second level",
            "in scratch pad"
            ],
        "TV house" : [
            "beneath",
            "inside",
            "on top"
            ],
        "Under toys" : [
            "gingerbread man",
            "any catnip toy",
            "whoop whoop",
            "crunchy big fish",
            "motorized big fish"
            ],
        "Green tent" : ["inside"],
        "Red tent" : ["inside"],
        "Red-white basket" : ["inside"],
        "Boxes" : ["any"],
        "Plastic food bowl" : ["any"],
        "Window" : ["on shelf"],
        "Pantry" : ["ground"],
        "Any small brown scratching post" : [
            "on top",
            "ground-level"
        ],
        "Big cat tree" : [
            "ground level",
            "2nd level",
            "3rd platform",
            "in house",
            "on house",
            "in basket",
            "top level"
            ],
        "Purple chair" : ["on seat"],
        "Long chair" : ["on seat"],
        "TV cabinet" : [
            "NES level",
            "VCR level",
            "DVD level",
            "TV level"
            ]
        },
    "Entrance" : {
        "Beige chair" : ["on seat"],
        "Entrance boxes" : ["any"],
        "Litter box" : ["on top"]
        },
    "Hallway" : {
        "Rug" : ["on top"]
        }
}

# We collapse all of the possibilities into a simple flat list for sampling
draws = []
# The `.keys()` method lets you get all of the "keys" for a dictionary
for room in treats.keys():
    # Again the `.keys()` method
    for furniture in treats[room].keys():
        # The lowest level is a list, so no need for `.keys()`
        for location in treats[room][furniture]:
            # The `.join()` method lets you concatenate strings,
            # like the `paste()` function in R
            draws.append(" => ".join([room, furniture, location]))

# `choices()` and `sample()` are replacement and non-replacement sampling
# The `sorted()` function does "in-place" sorting (I sort to make sure
# the locations are grouped together)
if args.replacement:
    draws = sorted(random.choices(draws, k=args.size))
else:
    draws = sorted(random.sample(draws, k=args.size))

# The `open()` function lets us write our results to a file
with open(args.output_file, "w") as f:
    f.write("<html><body>")
    f.writelines("<br>".join(draws))
    f.write("</body></html>")
