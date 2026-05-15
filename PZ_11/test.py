string = "14t6esf126771rsfdghw"

def extract_digits(a):
    for x in a:
        if x.isdigit():
            yield x

gen = extract_digits(string)

print(next(gen))
print(next(gen))