from datetime import datetime, timedelta

def timeToEat(time: str) -> list[int, int]:
    '''Takes in the current time as a string and determines the duration of time before Sloth's next meal.
    Sloth is a very habitual person. He eats breakfast at 7:00 a.m. each morning, lunch at 12:00 p.m. and dinner at 7:00 p.m. in the evening.

    Args:
        time: The input string with time format of "%I:%M %p".

    Returns:
        list[int, int]: List with first element being hours and second being minutes until next meal.
    '''
    current = datetime.strptime(time.replace('.', ''), "%I:%M %p").time()
    meals = [
        datetime.strptime("7:00 am", "%I:%M %p").time(),
        datetime.strptime("12:00 pm", "%I:%M %p").time(),
        datetime.strptime("7:00 pm", "%I:%M %p").time()
    ]

    next_meal = next((meal for meal in meals if meal > current), None)
    
    if next_meal is None:
        next_meal = meals[0]
        current_dt = datetime.combine(datetime.today(), current)
        next_meal_dt = datetime.combine(datetime.today() + timedelta(days=1), next_meal)
    else:
        current_dt = datetime.combine(datetime.today(), current)
        next_meal_dt = datetime.combine(datetime.today(), next_meal)
    
    delta = next_meal_dt - current_dt
    total_seconds = delta.total_seconds()
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    
    return [hours, minutes]

if __name__ == '__main__':
    func = timeToEat
    inputs = [
        "2:00 p.m.",
        "5:50 a.m.",
        "6:59 p.m.",
        "6:59 a.m.",
        "7:01 a.m.",
        "12:00 a.m.",
        "7:00 a.m.",
        "7:00 p.m.",
        "12:00 p.m."
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
