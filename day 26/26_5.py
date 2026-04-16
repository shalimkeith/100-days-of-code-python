weather_c = {
    "Monday":12,
    "Tuesday":21,
    "Wednesday":32,
    "Thursday":34,
    "Friday":25,
    "Saturday":26,
    "Sunday":17
}


weather_f = {day:(temp_c * 9/5)+32 for (day, temp_c) in weather_c.items()}

print(weather_f)