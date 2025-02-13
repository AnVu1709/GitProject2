def sort_integers():
    numbers = input("Enter integers pleaseeee: ")
    
    num_list = list(map(int, numbers.split()))

    sorted_asc = sorted(num_list)

    sorted_desc = sorted(num_list, reverse=True)

    print("\nOriginal List:", num_list)
    print("Sorted (Ascending):", sorted_asc)
    print("Sorted (Descending):", sorted_desc)


if __name__ == "__main__":
    sort_integers()
