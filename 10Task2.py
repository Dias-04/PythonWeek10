def convert_seconds(total_seconds):
    days = total_seconds // 86400
    hours = (total_seconds % 86400) // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"

seconds = int(input("Enter the number of seconds: "))
print(convert_seconds(seconds))
