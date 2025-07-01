
# Create a shopping cart  programme that will continuosly ask the user for food product and the price of the product
# Have an exit clause if the user wishes to stop adding more things to their cart
# Show food items and how much it costs at the end

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press q to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price to the {food}: R"))
        foods.append(food)
        prices.append(price)
        
        print("-----YOUR SHOPPING CART-----")
        
        for food in foods:
            print(food, end= " ")
            
        for price in prices:
            total += price
            
            print("\n")
            print(f"Your total is: R{total}")