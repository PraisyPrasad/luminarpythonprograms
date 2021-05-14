classheld=int(input("number of class held"))
classattended=int(input("number of class attended"))
per=(classattended/classheld*100)
if(per>75):
    print("allowed")
else:
    print("not allowed")