#Daily step goal
print("🚶Step walk 🚶‍♂️")
daily_goal = int(input("hey! what is step goal ? "))
steps_walked = int(input("how many steps have you walked now ? "))

remaining_step = daily_goal - steps_walked

if remaining_step > 0:
    print(f"👌 Finished hard. You have {remaining_step} steps to achieve you goal!!👌")
elif remaining_step == 0:
    print("🎉Congrats you have achieved your goal!🎉")
else:
    print(f"Wow!!🎉🎉🎉You have walked {-remaining_step} more than your goal🎉.")