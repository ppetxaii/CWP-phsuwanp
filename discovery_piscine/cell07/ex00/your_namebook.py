def array_of_names(persons):
    names = []
    
    for Fname, Lname in persons.items():
        full_name = Fname.capitalize() + " " + Lname.capitalize()
        names.append(full_name)
    
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))