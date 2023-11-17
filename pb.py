import csv
import datetime
from number_picker import generated_numbers_pb

def pbgen():
    # get auto-generated numbers from number_picker.py
    user_numbers = generated_numbers_pb()
    user_numbers = [int(num) for num in user_numbers.split(',')]
    current_datetime = datetime.datetime.now()
    count = 0

    # Open the CSV file for reading. File comes from NY Lottery Data.gov (replace the path with the correct file path)
    with open('Lottery_Powerball_Winning_Numbers__Beginning_2010.csv', 'r') as csv_file:
        # Create a CSV reader
        csv_reader = csv.reader(csv_file)

        column_index = 1

        next(csv_reader, None)

        for row in csv_reader:
            if len(row) > column_index:
                # Extract the winning numbers from the row
                winning_numbers_str = row[column_index]
                winning_numbers = [int(num) for num in winning_numbers_str.split()]

                # Check if any of the user-provided numbers match the winning numbers
                for num in user_numbers:
                    if num in winning_numbers:
                        count += 1

        # Write output to file and print msg
        with open('numbers_list.txt', 'a') as file:
            file.writelines(
                f'\nUser Numbers for Powerball {str(user_numbers)} appear {count} times as of {current_datetime}\n')

        print(f'The numbers {str(user_numbers)} appear {count} times in the Powerball.')
    return user_numbers, count