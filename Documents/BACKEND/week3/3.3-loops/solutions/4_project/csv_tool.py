

# We define these all-caps variables as "constants". They let us remember which
# column is which.
STREET = 0
CITY = 1
ZIP = 2
STATE = 3
BEDS = 4
BATHS = 5
SQUARE_FEET = 6
TYPE = 7
SALE_DATE = 8
PRICE = 9
LATITUDE = 10
LONGITUDE = 11

int_fields = [ZIP, BEDS, BATHS]
float_fields = [PRICE, LATITUDE, LONGITUDE]

def parse_hand_coded():
    # Note: Python has a built-in CSV reader and writer. For this solution we
    # WON'T use it, but in real life, it would make a bit more sense to use it.
    lines = open('sac_realestate.csv').readlines()
    column_names = lines[0]
    data_lines = lines[1:]  # Skip first line for all data lines
    print(column_names)
    data = []
    for line in data_lines:
        # Strip will remove any excess white-space (e.g. spaces, new lines)
        line = line.strip()

        # Split will transform the string into a list, separated by the comma
        columns = line.split(',')

        # "assert" is for adding quick debugging "sanity checks". A sanity
        # check is just a bit of code to ensure the data is sane (as are you
        # :p). We know all the addresses should be in CA so lets check here.
        assert columns[STATE] == 'CA'

        # Now convert it to a dict. This isn't necessary, depending on the
        # circumstance you may want to save memory and use a list or tuple.
        # However, in most cases we don't need to save memory like that.
        line_dict = {
            'street': columns[STREET],
            'city': columns[CITY],
            'zip': columns[ZIP],
            'state': columns[STATE],
            'beds': int(columns[BEDS]),
            'baths': int(columns[BATHS]),
            'square_feet': float(columns[SQUARE_FEET]),
            'type': columns[TYPE],
            'sale_date': columns[SALE_DATE],
            'price': float(columns[PRICE]),
            'latitude': float(columns[LATITUDE]),
            'longitude': float(columns[LONGITUDE]),
        }
        data.push(line_dict)
    return data


def _get_list_of_data_for_column(data, column):
    data_list = []
    for row in data:
        data_list.append(row[column])
    return data_list


def report_mode(data):
    columns = data[0].keys()
    columns_string = ', '.join(columns)
    actions = 'median, mode, mean, max, min'
    while True:
        print('Actions: ' + actions + ', quit')
        print('Columns: ', columns_string)
        print('Examples: "median price", or "max beds"')
        choice = input('? ')
        if choice == 'quit':
            return

        split_choice = choice.split()
        if len(split_choice) != 2:
            print('Invalid entry')
            continue  # Wrong size, repeat loop

        # Using "unpacking", we can assign two variables to the two items in
        # this list
        action, column = split_choice
        if column not in columns:
            print('Unknown column: ', column)
            continue

        if action not in actions:
            print('Unknown action: ', action)
            continue

        data_list = _get_list_of_data_for_column(data, column)
        if choice == 'median':
            data_list.sort()
            middle_index = int(len(data_list)/2)
            data[middle_index]

        elif choice == 'mode':
            counting_dict = {}

            # count all items
            for item in data_list:
                counting_dict.setdefault(item, 0)
                counting_dict[item] += 1

            # find most popular
            max_count = 0
            max_item = None
            for item, count in counting_dict:
                if count > max_count:
                    max_item = item
                    max_count = count

            print('Most common item:', max_item)
            print('Which appeared:', max_count)

        elif choice == 'mean':
            avg = sum(data_list) / len(data_list)
            print('Mean:', avg)

        elif choice == 'max':
            print('Max:', max(data_list))

        elif choice == 'min':
            print('Min:', min(data_list))

def main():
    data = parse_hand_coded()
    while True:
        print('%i lines of data' % len(data))
        print('report: Get statistical report')
        print('add: Add data')
        print('quit: Exit program')
        choice = input('? ')

        # "sanitize" the input to remove spacing and capitalization
        # irregularities
        choice = choice.trim().lower()

        # Check what they chose and kick off an alternate function in that case
        if choice == 'report':
            report_mode(data)
        elif choice == 'add':
            data_entry_mode(data)
        elif choice == 'quit':
            return  # Exit the function (and loop)


if __name__=='__main__':
    main()


