def return_string():
    return "Hello World"


def returns_string_passed_in(value='default'):
    return value


def return_a_string_of_values(*values):
    compiled_string = ""

    for value in values:
        is_first_value = value == values[0]
        value_to_append = (" " + value, value)[is_first_value]
        compiled_string += value_to_append
    return compiled_string


def return_customer_account_balance(name, account_number, bank_balance):
    customer_balance = "Hi {} of account {} your balance is {:.2f}".format(name, account_number, bank_balance)
    return customer_balance
