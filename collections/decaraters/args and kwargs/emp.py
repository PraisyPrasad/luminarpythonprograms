employees={1000:{"name":"sajay","desig":"pythontrainer","exp":3},
           1001:{"name":"sabir","desig":"bigdatatrainer","exp":3},
           1002:{"name":"christy","desig":"ml","exp":3}}
#eid=int(input("enter employee id"))
# if (eid in employees):
#     print("eid exit")
# else:
#     print("eid not exit")
# if(eid in employees):
#     print(employees[eid]["name"])
# else:
#     print("eid not exit")
def emp_details(**kwargs):
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if(id in employees):
        print(employees[id]["name"])
        print(employees[id][prop])
    else:
        print("eid not exists")
emp_details(eid=1000,prop="desig")