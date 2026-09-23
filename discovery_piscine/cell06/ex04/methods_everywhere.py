import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    text = text + "Z" * (8 - len(text))
    print(text)
    
if len(sys.argv) < 2:
    print("none")
else:
    for text in sys.argv[1:]:
        if len(text) > 8:
            shrink(text)
        elif len(text) < 8:
            enlarge(text)
        else:
            print(text)