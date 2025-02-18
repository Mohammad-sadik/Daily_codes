def check_index(arr):
    while True:
        try:
            index = int(input("Enter the index value: "))
            if 0 <= index < len(arr):
                del arr[index]
                print("Updated List:", arr)
                break
            else:
                print(f"Invalid index! Please enter a value between 0 and {len(arr)-1}.")
        except ValueError:
            print("Invalid input! Please enter a valid integer index.")

def check_element(arr):
    while True:
        element = input("Enter the element value: ")
        if element in arr:
            arr.remove(element)
            print("Updated List:", arr)
            break
        else:
            print(f"Invalid element! The element should be from {arr}.")

list_a = input("Enter the array (space-separated values): ").split()

print("*" * 15 + " Deleting by Index " + "*" * 15)
check_index(list_a)

print("*" * 15 + " Deleting by Element " + "*" * 15)
check_element(list_a)
