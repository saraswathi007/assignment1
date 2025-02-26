#DATE  12_02_2025:


'''
Avul Pakir Jainulabdeen Abdul Kalam BR was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007.
 Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering.
'''
# name="APJ abdul kalam"
# birth_year=2022
# print(name)
# print(birth_year)



#DATE 13_02_2025:



'''
Avul Pakir Jainulabdeen Abdul Kalam BR was an Indian aerospace scientist and statesman who served as the 11th president of India from 2002 to 2007.
 Born and raised in a Muslim family in Rameswaram, Tamil Nadu, he studied physics and aerospace engineering.
'''
# fullname=input("enter the full name:")
# age=int(input("enter the age:"))
# print(f"fullname is{fullname}\nand age is{age}")


# #DATE 20-02-25:



# name=input("enter students name:")
# marks=float(input("enter total marks:"))
# if marks<0 or marks>100:
#     print("invalid marks!please try again")
# elif marks>=90:
#     grade="A+"
#     remarks="outstanding"
# elif marks>=80:
#     grade="A"
#     remarks="very good"
# elif marks>=70:
#     grade="B+"
#     remarks="good"
# elif marks>=60:
#     grade="B"
#     remarks="Needs improvement"
# elif marks>=50:
#     grade="C"
#     remarks="better luck next time"
# else:
#     grade="F"
#     remarks="work harder"
# print(f"name: {name}")
# print(f"grade {grade}")
# print(f"remarks {remarks}")
# if grade=="F":
#     print("better luck next time!study well:")
# else:
#     print("congratulations!keep up the good work")

# DATE 21-02-2025:


menus=["dosa","poori","idli","biryani","eggrice","vegrice"]
one_dosa=30
one_poori=20
one_idli=25
one_biryani=80
one_eggrice=40
one_vegrice=45
your_order=input("enter your order:")
if your_order in menus:
    print(f"yess..{your_order} is available:")
    quantity=int(input(f"how many {your_order} you want:"))
    if your_order=="dosa":
        total=quantity*one_dosa
        print(f"your total bill is {total}")
        print("thankyou for visiting:")
    elif your_order=="poori":
        total=quantity*one_poori
        print(f'your total bill is {total}')
        print("thankyou for visiting::")
    elif your_order=="idli":
        total=quantity*one_idli
        print(f"your total bill is {total}")
        print("thankyou for visiting:")
    elif your_order=="biryani":
        total=quantity*one_biryani
        print(f"your total bill is {total}")
        print("thankyou for visiting::")
    elif your_order=="eggrice":
        total=quantity*one_eggrice
        print(f"your total bill is {total}")
        print("thankyou for visiting::")
    elif your_order=="vegrice":
        total=quantity*one_vegrice
        print(f"your total bill is {total}")
        print("thankyou for visiting::")
else:
    print(f"sorry {your_order} is not available:")
    print("Do you want to order another item???")
