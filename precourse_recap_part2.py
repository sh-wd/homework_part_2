current_week = 1
current_day_of_the_week = 1
total_course_weeks = 16
total_course_days_per_week = 5

def weeks_to_go():
    weeks_left = total_course_weeks - current_week
    days_left = total_course_days_per_week - current_day_of_the_week
    print(f"Only {weeks_left} weeks and {days_left} days left to go!")

def motivate_me():
    print ("We got this!! You're doing great!!!")

weeks_to_go()
motivate_me()
