import re
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]
for name in names:
    found=re.search(r'([A-Z][a-z|\.|\']+)(\s[A-Z][a-z|\.|\']*)*(\s[A-Z][a-z|\.|\']+)',name)
    if found:
        print(name)
    else:
        print("Invalid Name")
    