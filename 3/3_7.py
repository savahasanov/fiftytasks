def convert_time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        time_parts = time_str[:-2].strip().split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])

        if 'PM' in time_str and hours != 12:
            hours += 12
        elif 'AM' in time_str and hours == 12:
            hours = 0

        return f"{hours:02}:{minutes:02}"
    else:
        time_parts = time_str.split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])

        period = 'AM'
        if hours >= 12:
            period = 'PM'
            if hours > 12:
                hours -= 12

        if hours == 0:
            hours = 12

        return f"{hours}:{minutes:02} {period}"

print(convert_time("02:30 PM"))
print(convert_time("14:30"))
