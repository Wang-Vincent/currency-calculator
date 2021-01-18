import requests
import sys


def get_data(api):
    """

    Get data from api and return rate data in a dictionary

    :param api: a string represents the api address
    :precondition: The information from the API exists and in correct format
    :postcondtion: can always convert and return if precondtion is met.
    :return: currency rate in dictionary
    """
    data = requests.get(api)
    json_data = data.json()
    return json_data['rates']


def currency_converter():
    """

    Ask user for the amount of CAD dollar wanted to convert and the currency to convert.
    Then print out the converted amount of money.

    :precondition: user must enter a integer in the first input prompt and a valid number representing the currency
                    they want to exchange to in the second input prompt
    :postcondtion: can always execute if precondtion is met.

    """

    while True:
        rates = get_data('https://api.exchangeratesapi.io/latest?base=CAD')
        currency_name = list(rates.keys())
        money_to_convert = input('Please enter how much Canadian dollar(CAD) you want to convert, '
                                 'or enter q to exit the program:\n')
        if money_to_convert == 'q':
            end_program()
        else:
            money_to_convert = float(money_to_convert)
            print_currency(currency_name, rates)
            convert_to = input(f'Please enter the number associated with the currency you want to convert, '
                               f'or enter q to exit the program:\n')
            if convert_to.lower() == 'q':
                end_program()
            else:
                if convert_to.isnumeric():
                    if 1 <= int(convert_to) <= 33:
                        converted_money = round(money_to_convert * rates[currency_name[int(convert_to) - 1]],2)
                        print(f"{money_to_convert} CAD can be converted to {converted_money} "
                              f"{currency_name[int(convert_to) - 1]}")
                else:
                    print('Invalid input, please try again.')


def print_currency(currency_name, rates):
    """

    print the currency names along with their rate to Canadian dollars vertically for better readability.

    :param currency_name: a string representing the currency's name
    :param rates: a string representing the currency's rate to Canadian dollars.
    :precondition: this is a helper function. it can always execute if corrected parameter is passed in.
    :postcondition: this function can always execute.

    """
    print(f'Available currency abbreviations:')
    for index, currency in enumerate(currency_name, 1):
        print(f"{index}. {currency}: {rates[currency]}")


def end_program():
    print('Program ends.')
    sys.exit()


def main():
    currency_converter()


if __name__ == '__main__':
    main()
