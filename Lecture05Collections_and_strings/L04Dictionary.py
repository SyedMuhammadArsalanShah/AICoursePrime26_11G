a={
    
    "name": "smas",
    "age": 52,
    "FastFood": False,
    "Hobbies": ["books reading", "coding", "teachings"],
    "Education": {
        "ds":2026,
        "se":2030,
        "bs":2035,
        "ms":2056,
        
        },
    
}



print(a)
print(a["name"])
print(a["Hobbies"])
print(a["Education"]["ds"])
print(a.keys())
print(a.values())
print(a.items())
print(a.get("height"))





oxfordMT_dictionary={
    
    "qalam":"pen",
    "kitab":"book",
    "smas":"kaam bht zayada dety hen"
}


print("check your words in world famous dictionary ", list(oxfordMT_dictionary.keys()))
search = input("enter your word \n")
print(oxfordMT_dictionary.get(search))
      