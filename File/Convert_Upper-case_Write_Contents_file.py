def convert_upper_case():
    try:
        with open('copy.txt', 'r') as file:
            file_data = file.read()
            file_data = file_data.upper()

        with open('output_file.txt', 'w') as file:
            file.write(file_data)
        print(f"\nConversion successful! Uppercase content saved to output_file")
    except Exception as e:
        print(f"Error: {e}")
    pass
    
if __name__ == "__main__":
    convert_upper_case()
