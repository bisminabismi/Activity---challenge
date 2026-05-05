total_seats = 5
bookings = {}

def check_availability():
    print("Available seats:", total_seats - len(bookings))

def book_ticket():
    if len(bookings) >= total_seats:
        print("No seats available")
        return
    name = input("Enter name: ")
    age = input("Enter age: ")
    booking_id = str(len(bookings) + 1)
    bookings[booking_id] = {"name": name, "age": age}
    print("Booked! ID:", booking_id)

def view_ticket():
    bid = input("Enter booking ID: ")
    if bid in bookings:
        print("Details:", bookings[bid])
    else:
        print("Not found")

def cancel_ticket():
    bid = input("Enter booking ID: ")
    if bid in bookings:
        del bookings[bid]
        print("Cancelled")
    else:
        print("Not found")

while True:
    print("\n1.Check\n2.Book\n3.View\n4.Cancel\n5.Exit")
    ch = input("Choose: ")

    if ch == "1":
        check_availability()
    elif ch == "2":
        book_ticket()
    elif ch == "3":
        view_ticket()
    elif ch == "4":
        cancel_ticket()
    elif ch == "5":
        break
    else:
        print("Invalid choice")
