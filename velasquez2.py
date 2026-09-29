patients={"Rhea":(105,130,480),
          "Alex": (80,90,100)}
normal=120
for key, value in patients.items():
    print(key)

    for v in value:
        if v>normal:
            print(v,"diabetic")
        else:
            print(v, "normal")