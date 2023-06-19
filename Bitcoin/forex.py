#!/usr/bin/python3

from main import main
from forex_python.converter import CurrencyRates
import datetime

def get_valid_response(text, options):
    response = input(text).strip()
    while response not in options:
        response = input(f'Invalid choice, {text}').strip()
    return response

def get_valid_date():
    year = int(get_valid_response("Enter year: ", list(map((lambda x: str(x)), list(range(1, 10000))))))
    month = int(get_valid_response("Enter month: ", list(map((lambda x: str(x)), list(range(1, 13))))))
    day = int(get_valid_response("Enter day: ", list(map((lambda x: str(x)), list(range(1, 32))))))
    hour = int(get_valid_response("Enter hour: ", list(map((lambda x: str(x)), list(range(0, 24))))))
    minute = int(get_valid_response("Enter minute: ", list(map((lambda x: str(x)), list(range(0, 60))))))
    second = int(get_valid_response("Enter second: ", list(map((lambda x: str(x)), list(range(0, 60))))))
    return year, month, day, hour, minute, second, 0

def print_rates(dictionary, c):
    for key, val in dictionary.items():
        print(f'1 {c} -> {val} {key}')


def latest_currencies():
    rate = CurrencyRates()
    currency = input("Enter currency: ").strip()
    option = int(get_valid_response("Select option:\n[1] View Rates as of now\n[2] View Rates at a user specified date and time: ", "12"))

    if option == 2:
        y, m, d, h, mi, s, ms = get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        try:
            print_rates(rate.get_rates(currency, date_obj), currency)
        except:
            print(f'{currency} could not be found')
    else:
        try:
            print_rates(rate.get_rates(currency), currency)
        except:
            print(f'{currency} could not be found')
    option = int(get_valid_response("Select Option:\n[1] Return To main\n[2] Check rates again\n[3] Quit\nEnter response: ", "123"))
    if option == 1:
        main()
    elif option == 2:
        latest_currencies()

def print_conversion(base, dest, amt, res):
    print(f'{amt} {base} = {res} {dest}')


def convert_amount():
    rate = CurrencyRates()
    base_cur = input("Enter base currency: ")
    dest_cur = input("Enter destination currency: ")
    try:
        amount = float(input("Amount: "))
    except:
        print("Not a valid number")
    option = int(get_valid_response("Select option:\n[1] View coversion as of now\n[2] View conversion at a user specified date and time: ", "12"))
    if option == 2:
        y, m, d, h, mi, s, ms = get_valid_date()
        date_obj = datetime.datetime(y, m, d, h, mi, s, ms)
        try:
            print_conversion(base_cur, dest_cur, amount, rate.convert(base_cur, dest_cur, amount, date_obj))
        except:
            print("An error occured")
    else:
        try:
            print_conversion(base_cur, dest_cur, amount, rate.convert(base_cur, dest_cur, amount))
        except:
            print("An error occured")
    option = int(get_valid_response("Select Option:\n[1] Return To main\n[2] Convert again\n[3] Quit\nEnter response: ", "123"))
    if option == 1:
        main()
    elif option == 2:
        convert_amount()



def two_pairs_exchange():
    pass

def fiat_exchange():
    print("Select Option: \n \
            [1] See all latest currency rates for one currency\n \
            [2] Check exchange rate between two pairs\n \
            [3] Convert an amount in one currency to another")
    ans = int(get_valid_response("Enter response: ", "123"))

    if ans == 1:
        latest_currencies()
    elif ans == 2:
        two_pairs_exchange()
    else:
        convert_amount()
