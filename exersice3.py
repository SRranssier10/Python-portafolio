#1. Inputs
employed_name = input("Enter employee name: ")
salary = float(input("Enter base salary ($): "))
score = int(input("Enter performance score (1-100): "))
print("_________________________")
print("Employee:", employed_name)
#2. Multi-condition logic using elif
if score >= 90:
    bonus_rate = 0.20
    status = "Excellent Performance"
elif score >= 70:
    bonus_rate = 0.10
    status = "Good Performance"
else:
    bonus_rate = 0.0
    status = "Needs Improvement"
 #3. Calculation
bonus = salary * bonus_rate
total_payout = salary + bonus
#4. outputs
print("Performance Status:", status)
print("Bonus Amount: $", round(bonus, 2))
print("Total Payout: $", round(total_payout, 2))



    


