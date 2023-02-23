# indian = [ "samosa", "daal", "naan"]
# chinese = ["egg role", "pot sticker", "fried rice"]
# italian = ["pizza", "pasta", "risoto"]

# dish = input ("Enter the dish name : ").lower().strip()

# if dish in indian:
#     print(f"{dish} is an indian dish")
# elif dish in chinese :
#     print(f"{dish} is an chinese dish")
# elif dish in italian :
#     print(f"{dish} is an italia dish")
# else :
#     print(f"i have no idea where is {dish} from ")


# if dish in indian or dish in italian :
#     print(f"you have chosen {dish} and it is avery good  choice ")

# print(f"{dish} is an italian dish" if dish in italian else "it is not italian" )


India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

city1 = input("Enter the first city : ")
city2 = input("Enter the second city : ")

if city1  in India and city2 in India :
    print(f"{city1} and  {city2} are located in India ")

elif city1  in USA and city2 in USA :
    print(f"{city1} and  {city2} are located in USA ")

elif city1 in UK and city2 in UK :
    print(f"{city1} and  {city2} are located in UK ")

else:
    print(f"{city1} and {city2} don't belong to the same country ")




