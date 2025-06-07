welcome_message = """Hello!, Welcome to my Personal Energy Tracker
This simple program helps you track how much electricity your common household appliances use.
You will enter how many hours per day you use the appliance.
Then, the tracker will estimate your daily and monthly energy usage in kilowatt-hours (kWh)
Let us help you understand your energy habits better!"""

print(welcome_message)

# appliances rating
led_light_bulb = 9
incandescent_bulb = 100
refrigerator = 250
microwave_oven = 800
electric_kettle = 1500
coffee_maker = 600
dish_washer = 1200
air_conditioner = 1500
iron = 1500
television = 100
laptop = 100
fan = 70 
water_heater = 3000
fridge = 100 

print("We are going to test with five appliances")
# inputs from user
appliance1 = input("Input the first appliance: ")
number_of_hours1 = input("Input the number of hours: ")

appliance2 = input("Input the second appliance: ")
number_of_hours2 = input("Input the number of hours: ")

appliance3 = input("Input the third appliance: ")
number_of_hours3 = input("Input the number of hours: ")

appliance4 = input("Input the fourth appliance: ")
number_of_hours4 = input("Input the number of hours: ")

appliance5 = input("Input the fifth appliance: ")
number_of_hours5 = input("Input the number of hours: ")

watts1 = eval(appliance1)
watts2 = eval(appliance2)
watts3 = eval(appliance3)
watts4 = eval(appliance4)
watts5 = eval(appliance5)

# Calculating the kWh of each appliance
usage1 = int(number_of_hours1) * int(watts1)
usage2 = int(number_of_hours2) * int(watts2)
usage3 = int(number_of_hours3) * int(watts3)
usage4 = int(number_of_hours4) * int(watts4)
usage5 = int(number_of_hours5) * int(watts5)

total_usage = usage1 + usage2 + usage3 + usage4 + usage5
monthly_usage = total_usage * 30

# Output
print("Energy Usage Report")

print("Total Daily Usage: " + str(round(total_usage)) + " kWh")
print("Estimated Monthly Usage: " + str(round(monthly_usage)) + " kWh")
