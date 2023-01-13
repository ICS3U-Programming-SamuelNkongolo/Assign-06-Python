#!/usr/bin/env python3
# Created By: Samuel Nkongolo
# Date: Dec 1, 2022
# This program ask the user to enter integers and shows them the even ones

def list_of_num(user_list):
    even_num = []
    for user_num in user_list:
        if user_num % 2 == 0:
            even_num.append(user_num)
    return even_num


def main():
    #explain program and ask user for a list of numbers
    user_list_split = []
    print("This program asks user to enter a list of numbers and the returns the list with only even numbers")
    print("Make sure to enter list in the correct format")
    user_list = input("Enter a list of integers : ")
    user_list_split = user_list.split(',')
    user_list = user_list.strip()
    list_size = len(user_list_split)
    for i in range(list_size):
        try:
            user_list_split[i] = int(user_list_split[i])
        except ValueError:
            print("Invalid Input (string was entered)")
    even_num = list_of_num(user_list_split)
    #display list with only even numbers

    print(even_num, end=" ")


if __name__ == "__main__":
    main()