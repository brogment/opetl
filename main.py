# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# if __name__ == '__main__':
#     print_hi('PyCharm')


import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

print(f"API_KEY: {API_KEY}")