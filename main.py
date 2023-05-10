class House:
    def __init__(self):
        self.items_in_house = {
            "Rudy": {"seconds": 10, "quantity": 1},
            "Mason": {"seconds": 10, "quantity": 1},
            "can of beans": {"seconds": 5, "quantity": 5},
            "water bottle": {"seconds": 5, "quantity": 5},
            ".950 JDJ": {"seconds": 15, "quantity": 1},
            "mp3 player": {"seconds": 5, "quantity": 1},
            "tool box": {"seconds": 10, "quantity": 1},
            "medicine": {"seconds": 4, "quantity": 1},
            "pillow": {"seconds": 1, "quantity": 3},
            "chess": {"seconds": 6, "quantity": 1},
            "bug repellent": {"seconds": 5, "quantity": 1},
            "turtle": {"seconds": 30, "quantity": 1},
            "fuel": {"seconds": 5, "quantity": 3},
            "oxygen tank": {"seconds": 3, "quantity": 3},
            "alien mask": {"seconds": 3, "quantity": 1},
            "first aid": {"seconds": 5, "quantity": 1},
            "radio": {"seconds": 7, "quantity": 1}
        }

    def grab_items(self):
        items = []
        time = 100

        while time > 0:
            print("-----------------------------------")
            for index, (item_name, item_details) in enumerate(self.items_in_house.items(), start=1):
                seconds = item_details["seconds"]
                quantity = item_details["quantity"]
                print(f"{index}: {quantity} {item_name}(s) -{seconds} seconds")
            print("-----------------------------------")
            grab = int(input("Type the number corresponding to the item you would like to grab: "))
            item_keys = list(self.items_in_house.keys())

            if grab <= len(item_keys):
                selected_item = item_keys[grab - 1]  # Get the selected item key
                print(selected_item)

                if (
                    self.items_in_house[selected_item]["quantity"] > 0
                    and time - self.items_in_house[selected_item]["seconds"] >= 0
                ):
                    items.append(selected_item)  # Add the selected item to the items list
                    self.items_in_house[selected_item]["quantity"] -= 1  # Decrement the quantity of the selected item
                    time -= self.items_in_house[selected_item]["seconds"]  # Subtract the seconds from the time
                    print("Time remaining:", time)  # Print the remaining time
                elif self.items_in_house[selected_item]["quantity"] == 0:
                    print(f"No more {selected_item} left.")
                    print("Time remaining:", time)  # Print the remaining time
                else:
                    print("Not enough time to grab that item.")
                    print("Time remaining:", time)  # Print the remaining time
            else:
                print("Invalid input. Please try again.")
                print("Time remaining:", time)  # Print the remaining time

        print(items)  # Print the list of grabbed items



def main():
    house = House()
    house.grab_items()


if __name__ == '__main__':
    main()
