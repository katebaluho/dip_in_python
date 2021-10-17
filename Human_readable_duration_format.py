'''
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration
 is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year
is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid,
but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds,
but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than
any valid more significant unit of time.
'''
import time

def format_duration(seconds):
    one_year = 365*24*3600
    one_day = 24*3600
    one_hour = 3600
    one_minute = 60
    one_sec = 1

    years = seconds//(one_year)
    days = (seconds-years*one_year)//(one_day)
    hours = (seconds-years*one_year - days*one_day)//(one_hour)
    minutes = (seconds - years * one_year - days * one_day - hours*one_hour) // (one_minute)
    sec = (seconds - years * one_year - days * one_day - hours*one_hour - minutes*one_minute)

    elements_count = sum([1 for i in [years,days,hours,minutes,sec] if i > 0])
    print(elements_count)

    res = ''

    if not elements_count:
        return 'now'
    if years:
        res += f"{years} year" if years == 1 else f"{years} years"
        elements_count -= 1
        if elements_count > 1:
            res += ', '
        elif elements_count == 1:
            res += ' and '
        else:
            res += ''
    if days:
        res += f"{days} day" if days == 1 else f"{days} days"
        elements_count -= 1
        if elements_count > 1:
            res += ', '
        elif elements_count == 1:
            res += ' and '
        else:
            res += ''
    if hours:
        res += f"{hours} hour" if hours == 1 else f"{hours} hours"
        elements_count -= 1
        if elements_count > 1:
            res += ', '
        elif elements_count == 1:
            res += ' and '
        else:
            res += ''
    if minutes:
        res += f"{minutes} minute" if minutes == 1 else f"{minutes} minutes"
        elements_count -= 1
        if elements_count > 1:
            res += ', '
        elif elements_count == 1:
            res += ' and '
        else:
            res += ''
    if sec:
        res += f"{sec} second" if sec == 1 else f"{sec} seconds"

    return res

print(format_duration(3600*24*365+8000))
print(format_duration(120))
print(format_duration(60))

###############################################3
times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration2(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]

print(format_duration2(3600*24*365+8000))
print(format_duration2(120))
print(format_duration2(60))




