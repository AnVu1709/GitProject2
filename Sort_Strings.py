def sort_strings(strings):

    return sorted(strings)

def get_user_input():

    input_string = input("Enter strings separated by spaces: ")
    strings = input_string.split()  
    return strings

def main():

    strings = get_user_input()  
    sorted_strings = sort_strings(strings)  
    print("Sorted strings:", sorted_strings)

if __name__ == "__main__":
    main()