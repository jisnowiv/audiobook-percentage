import math
import sys

debugMode = False

secondsInAMinute = 60
secondsInAnHour = 3600


def debug_print(text):
    if debugMode:
        print(text)


def print_usage():
    print('Usage:')
    print('\tpython main.py <currentHours> <currentMinutes> <currentSeconds> '
          '<remainingHours> <remainingMinutes> <remainingSeconds>')


def calculate_percentage(ch, cm, cs, rh, rm, rs):
    try:
        current_hours = int(ch)
        current_minutes = int(cm)
        current_seconds = int(cs)

        debug_print('Current hours: ' + str(current_hours))
        debug_print('Current minutes: ' + str(current_minutes))
        debug_print('Current seconds: ' + str(current_seconds))

        remaining_hours = int(rh)
        remaining_minutes = int(rm)
        remaining_seconds = int(rs)

        debug_print('Remaining hours: ' + str(remaining_hours))
        debug_print('Remaining minutes: ' + str(remaining_minutes))
        debug_print('Remaining seconds: ' + str(remaining_seconds))

    except ValueError:
        print('Exception while parsing strings, please confirm that all arguments are numeric.')
        print_usage()
    else:
        total_seconds_current = current_seconds
        total_seconds_current += current_minutes * secondsInAMinute
        total_seconds_current += current_hours * secondsInAnHour
        debug_print('Total current seconds: ' + str(total_seconds_current))

        total_seconds_remaining = remaining_seconds
        total_seconds_remaining += remaining_minutes * secondsInAMinute
        total_seconds_remaining += remaining_hours * secondsInAnHour
        debug_print('Total remaining seconds: ' + str(total_seconds_remaining))

        total_seconds = total_seconds_current + total_seconds_remaining

        decimal = (total_seconds_current/total_seconds)
        percent = decimal * 100
        percent_truncated = math.trunc(percent)

        debug_print('Decimal: ' + str(decimal))
        debug_print('Percent: ' + str(percent))
        debug_print('Truncated percent: ' + str(percent_truncated))

        return percent_truncated


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    debug_print('Number of arguments: ' + str(len(sys.argv)))
    debug_print('Argument List: ' + str(sys.argv))

    if len(sys.argv) < 7:
        print_usage()
        exit()

    if sys.argv.__contains__('d'):
        debugMode = True

    final_percent = calculate_percentage(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
    print('Currently at ' + str(final_percent) + '%')
