import random
import argparse

parser = argparse.ArgumentParser(description="Sample locations to put cat treats")
parser.add_argument("-f", "--output_file", type=str, help="location of file to output", default="./index.html")
parser.add_argument("-k", "--size", type=int, help="size of sample", default=10)
parser.add_argument("-r", "--replacement", action="store_true", help="whether to sample with replacement")

args = parser.parse_args()

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
            "big fish",
            "whoop whoop"
            ],
        "Green tent" : ["inside"],
        "Boxes" : ["any"],
        "Window" : ["on shelf"],
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

draws = []

for room in treats.keys():
    for furniture in treats[room].keys():
        for location in treats[room][furniture]:
            draws.append(" => ".join([room, furniture, location]))

if args.replacement:
    draws = sorted(random.choices(draws, k=args.size))
else:
    draws = sorted(random.sample(draws, k=args.size))

with open(args.output_file, "w") as f:
    f.write("<html><body>")
    f.writelines("<br>".join(draws))
    f.write("</body></html>")
