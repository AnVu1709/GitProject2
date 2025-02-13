def sort_integers(num_list):
    sorted_asc = sorted(num_list)
    sorted_desc = sorted(num_list, reverse=True)
    return sorted_asc, sorted_desc

if __name__ == "__main__":
    numbers = input("Enter integers separated by spaces: ")
    num_list = list(map(int, numbers.split()))
    sorted_asc, sorted_desc = sort_integers(num_list)

    print("\nOriginal List:", num_list)
    print("Sorted (Ascending):", sorted_asc)
    print("Sorted (Descending):", sorted_desc)
