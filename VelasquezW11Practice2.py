#months = ("Jan","Feb","Mar","April", "May","Jun", "Jul","Aug","Sept","Oct","Nov","Dec")
#print(months)
#days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")
#print(days)

machine_learning = [
    ("Supervised", "decision tree"),
    ("Supervised", "random forest"),
    ("Unsupervised", "K-means"),
    ("Unsupervised", "Gaussian mixture model")
]




for learning_type in ["Supervised","Unsupervised"]:
    print(learning_type + ":")

    for item in machine_learning:
        if item[0] == learning_type:
            print(item[1])

