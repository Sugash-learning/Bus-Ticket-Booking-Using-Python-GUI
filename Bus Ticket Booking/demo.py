import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Bus Ticket Booking System")

# Define seat prices
seat_price = 100

# Initialize selected seats
selected_seats = []

# Function to update seat selection
def select_seat(seat_button, seat_id):
    if seat_id in selected_seats:
        selected_seats.remove(seat_id)
        seat_button.config(bg="lightgray")
    else:
        selected_seats.append(seat_id)
        seat_button.config(bg="green")

# Function to calculate and show the bill
def show_bill():
    if not selected_seats:
        messagebox.showwarning("No Seats Selected", "Please select at least one seat.")
        return

    total_cost = len(selected_seats) * seat_price
    bill_message = (
        f"*** Sugash Travels ***\n"
        f"------------------------\n"
        f"Selected Seats: {', '.join(selected_seats)}\n"
        f"Seat Price: ₹{seat_price}\n"
        f"Total Seats: {len(selected_seats)}\n"
        f"------------------------\n"
        f"Total Cost: ₹{total_cost}\n"
        f"------------------------\n"
        f"Thank you for choosing Sugash Travels!"
    )

    # Create a new window to display the bill
    bill_window = tk.Toplevel(root)
    bill_window.title("Bill")

    # Create a text widget to display the bill message
    bill_text = tk.Text(bill_window, height=15, width=50)
    bill_text.pack(padx=10, pady=10)
    bill_text.insert(tk.END, bill_message)
    bill_text.config(state=tk.DISABLED)  # Make the text widget read-only

    # Add a button to close the bill window
    close_button = tk.Button(bill_window, text="Close", command=bill_window.destroy)
    close_button.pack(pady=5)

# Create seat buttons
for row in range(5):
    for col in range(4):
        seat_id = f"{row+1}-{col+1}"
        seat_button = tk.Button(root, text=seat_id, width=10, height=2, bg="lightgray")
        seat_button.config(command=lambda btn=seat_button, id=seat_id: select_seat(btn, id))
        seat_button.grid(row=row, column=col, padx=5, pady=5)

# Add the bill button
bill_button = tk.Button(root, text="Show Bill", width=20, command=show_bill)
bill_button.grid(row=5, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()
