def calculate_bill_split():
    total_bill = 4800.0
    tip_rate = 0.10
    number_of_friends = 7

    total_tip = total_bill * tip_rate
    grand_total = total_bill + total_tip
    tip_per_friend = total_tip / number_of_friends
    total_per_friend = grand_total / number_of_friends

    print(f"Total tip: {total_tip:.2f}")
    print(f"Grand total: {grand_total:.2f}")
    print(f"Tip per friend: {tip_per_friend:.2f}")
    print(f"Total per friend: {total_per_friend:.2f}")


if __name__ == "__main__":
    calculate_bill_split()
    


