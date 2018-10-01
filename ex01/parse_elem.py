import json

# file = open("elements.json", "r")
# elem_file = file.read()
# file.close
# el = json.loads(elem_file)
with open("elements.json") as el_file:
    el = json.load(el_file)
    print("<!DOCTYPE html>")
    print('<html>')
    print('<head>')
    print('<link href="style.css" rel="stylesheet" type="text/css" media="all">')
    print('</head>')
    print('<body>')
    for i in range(118):
        category = str(el['elements'][i]['category'])
        if category == "alkali metal":
            colour = "white"
        elif category == "alkaline earth metal":
            colour = "yellow"
        elif category == "lanthanide":
            colour = "chocolate"
        elif category == "actinide":
            colour = "brown"
        elif category == "transition metal":
            colour = "grean"
        elif category == "post-transition metal":
            colour = "violet"
        elif category == "metalloid":
            colour = "fuchsia"
        elif category == "diatomic nonmetal":
            colour = "magenta"
        elif category == "polyatomic nonmetal":
            colour = "pink"
        elif category == "halogen":
            colour = "grey"
        elif category == "noble gas":
            colour = "red"
        elif category == "unknown, probably transition metal":
            colour = "tan"
        elif category == "unknown, probably post-transition metal":
            colour = "tan"
        else:
            colour = "grey"
        print('<div class="atom" style="top:' + str(65 * el['elements'][i]['ypos']) + 'px; left:'+ str(65 * el['elements'][i]['xpos']) + 'px; background-color:'+colour+'">')
        print('<p class="num">' + str(el['elements'][i]['number']) + '</p>')
        print('<p class="symbol"><b>' + el['elements'][i]['symbol'] + '</b></p>')
        print('<p class="mass">' + str(el['elements'][i]['atomic_mass']) + '</p>')
        print('</div>\n')
    print('</body>')
    print('</html>')
