#date  12_02_2025
'''
Avul Pakir Jainulabdeen Abdul Kalam BR was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007.
 Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering.
'''
# name="APJ abdul kalam"
# birth_year=2022
# print(name)
# print(birth_year)



#date 13_02_2025
'''
Avul Pakir Jainulabdeen Abdul Kalam BR was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007.
 Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering.
'''
# fullname=input("enter the full name:")
# age=int(input("enter the age:"))
# print(f"fullname is{fullname}\nand age is{age}")


#DATE 20-02-25

name=input("enter students name:")
marks=float(input("enter total marks:"))
if marks<0 or marks>100:
    print("invalid marks!please try again")
elif marks>=90:
    grade="A+"
    remarks="outstanding"
elif marks>=80:
    grade="A"
    remarks="very good"
elif marks>=70:
    grade="B+"
    remarks="good"
elif marks>=60:
    grade="B"
    remarks="Needs improvement"
elif marks>=50:
    grade="C"
    remarks="better luck next time"
else:
    grade="F"
    remarks="work harder"
print(f"name: {name}")
print(f"grade {grade}")
print(f"remarks {remarks}")
if grade=="F":
    print("better luck next time!study well:")
else:
    print("congratulations!keep up the good work")

