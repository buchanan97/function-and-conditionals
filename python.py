import difflib


# example 1
# With this example I used a temperature calculation based on what outside temperature will likely result in.

# The temperature is set variable notation is declared alongside the integer value 

mild = 70 

hot = 80

chilly = 50

cold = 33

freezing = -20

user_input = int (input("Please type in your outside temperature: ")) #here I stated how the input calculation would be represented as 

# I set the conditional statements that will correspond to the user input in order to set the logic for temperature mapping. 
if user_input < 50:

    print("It is cold, wear a coat")

elif user_input < 33:

    print("print wear a coat and put on gloves and boots!!")

elif user_input > 50:

    print("It is mild")

elif user_input > 80:
    print("It is hot")

else:
    print("Not an integer closing now ...")

# example 2  
# This carries on with the logic of temperature based on the users input but using the try and except clause

# try-except Block:

# The try block attempts to convert the user input to an integer.
# If the conversion fails (e.g., the user enters a non-integer), a ValueError exception is raised, and the except block is executed.
mild = 70 

hot = 80

chilly = 50

cold = 33

freezing = -20
try: 
    user_input = int(input("Please type in your outside temperature: "))
#conditional logic holds the input compares to the variable value set beforehand. 
    if user_input <= freezing:
        print("It's freezing! Bundle up!")
    elif user_input <= cold:
        print("It's cold, wear a coat.")
    elif user_input <= chilly:
        print("It's chilly, wear a light jacket.")
    elif user_input <= mild:
        print("It's mild, enjoy the weather!")
    else:
        print("It's hot, stay hydrated!")
#except clause will hold the value error if the value is not a integer. 
except ValueError:
    print("Invalid input. Please enter an integer.")

#example 3
nvidia_geforce_rtx3040 = 700
intel_core_i7 = 500
nvidia_geforce_rtx_4070 = 1000
intel_core_i9 = 700

try:
    user_input = str(input("type in your choice of purchase: "))

    if user_input == "nvidia_geforce_rtx3040":
        print(f'this will cost you: {nvidia_geforce_rtx3040}')
    elif user_input == "intel_core_i7":
        print(f'This item will cost you: {intel_core_i7}')
    elif user_input == "nvidia_geforce_rtx_4070":
        print(f'This item will cost you: {nvidia_geforce_rtx_4070}')
    elif user_input == "intel_core_i9":
        print(f'This item will cost you: {intel_core_i9}')
    else:
        print("This isn't in the shop options sorry..)")

except ValueError:
    print("Invalid input. Please enter a valid product name.")
# #
#Example 4
#with this example I used a dictionary in order too store the value of the computer items, instead of using variables with underscores. 
# The reason for this is because if a user inputs a string with a value with spaces, my code won't execute the dcode effecitively.
# it will lead to an error clause, which the exception handling. So in order to stay away from this I used a dictionary to store the key and value pairs for each item. 
items = {
    "nvidia geforce rtx3040": 700,
    "intel core i7": 500,
    "nvidia geforce rtx 4070": 1000,
    "intel core i9": 700
}

#the try-exception clause handler will run the loop of storing the input and comparing it with the dictionary values. 
try:
    user_input = input("Type in your choice of purchase: ").lower().strip()
#     User Input: We take the user's input, convert it to lowercase, and remove any leading or trailing whitespace using lower().strip().
# Iterating Over Dictionary: We iterate over the items dictionary, accessing each item and its price.
    for item, price in items.items():
        if user_input in item.lower():
            print(f"This item will cost you: {price}")
            break
    else:
        print("This isn't in the shop options sorry...")
except ValueError:
    print("You did not enter a string value (words...)")

# #example 5
music_production_vst = {
        'ableton 9': 200,
        'ableton 10': 500,
        'ableton 11': 1200
    }
def vst_software():

    user_answer = input("What is your choice of a vst: ").lower().strip()
    # Convert dictionary keys to a set of lowercase keys
    lowercase_keys = set(key.lower() for key in music_production_vst.keys())

    if user_answer.lower() in lowercase_keys:
        price = str(music_production_vst[next(key for key in music_production_vst if key.lower() == user_answer.lower())])
        print(f"Here is the VST of your choice: {user_answer} - ${price}")
    else:
        print("This VST is not available in our shop. Goodbye...")

vst_software()

#example 6
#for this example I used american express card as an example to showcase what will output if a user chosen from the selections

amex_cards = {
    'Amex Gold Card': 200,
    'Amex Blue Cash Card': 100,
    'Amex Platinum Card': 699,
    'Amex Black Card' : 5000
} # I set a dictionary clause that holds the str (key) , and price (value of the key). 


def card_selection():
    user_card_option = input("Please enter your choice of American Express card: ").lower().strip()

    # Normalize input by removing extra spaces and converting to lowercase
    normalized_input = ' '.join(user_card_option.split())

    # Check for exact match first
    if normalized_input in amex_cards:
        item = str(amex_cards[normalized_input])
        print(f'Here is your choice of card: {normalized_input} - $ {item}')
    else:
        # Check for close matches using difflib and keyword matching
        closest_matches = difflib.get_close_matches(normalized_input, amex_cards.keys(), cutoff=0.6)
        if closest_matches:
            suggested_card = closest_matches[0]
            print(f"Did you mean '{suggested_card}'? (y/n)")
            user_confirmation = input().lower()
            if user_confirmation == 'y':
                item = str(amex_cards[suggested_card])
                print(f'Here is your choice of card: {suggested_card} - $ {item}')
            else:
                print("Card not found. Please try again.")
        else:
            # Keyword-based matching
            keywords = normalized_input.split()
            for card_name, price in amex_cards.items():
                if all(keyword in card_name.lower() for keyword in keywords):
                    print(f"Did you mean '{card_name}'? (y/n)")
                    user_confirmation = input().lower()
                    if user_confirmation == 'y':
                        item = str(price)
                        print(f'Here is your choice of card: {card_name} - $ {item}')
                        return
            print("Card not found. Please try again.")

card_selection()

# example 7
# My previous code works fine but in order to shorten it and to show my enhanced skills for conditionals and fucntions. I simplified like this.
# Temperature
mild = 70 

hot = 80

chilly = 50

cold = 33

freezing = -20
try: 
    user_input = int(input("Please type in your outside temperature: "))
#conditional logic holds the input compares to the variable value set beforehand. 
    if user_input <= freezing:
        print("It's freezing! Bundle up!")
    elif user_input <= cold:
        print("It's cold, wear a coat.")
    elif user_input <= chilly:
        print("It's chilly, wear a light jacket.")
    elif user_input <= mild:
        print("It's mild, enjoy the weather!")
    else:
        print("It's hot, stay hydrated!")
#except clause will hold the value error if the value is not a integer. 
except ValueError:
    print("Invalid input. Please enter an integer.")
