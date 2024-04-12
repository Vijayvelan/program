def calculate_electricity_bill(past_kwh, current_kwh):
    units_consumed = current_kwh - past_kwh
    if units_consumed < 0:
        print("Error: Current kWh reading cannot be less than past kWh reading.")
        return None  # Indicate error

    total_bill = 0.0

    # Slab-based calculations
    slab_limits = [(1, 100, 0), (101, 200, 2.25), (201, 400, 4.5), (401, 500, 6)]
    for lower_limit, upper_limit, rate in slab_limits:
        if units_consumed <= 0:
            break  # Exit loop if all units consumed are covered

        # Calculate units consumed within the current slab
        units_in_slab = min(units_consumed, upper_limit - lower_limit + 1)

        # Add the charge for units in this slab
        total_bill += units_in_slab * rate

        # Update units consumed for the next slab
        units_consumed -= units_in_slab

    return total_bill

# Get user input
try:
    past_kwh = int(input("Enter the previous kWh reading: "))
    current_kwh = int(input("Enter the current kWh reading: "))
except ValueError:
    print("Error: Invalid input. Please enter integers for kWh readings.")
    exit()

# Calculate and display the bill amount
bill_amount = calculate_electricity_bill(past_kwh, current_kwh)
if bill_amount is not None:
    print("\n___Your Calculated Electricity Bill___\n")
    print("Total Electricity Bill: {:.2f} Rs".format(bill_amount))
