def count_letter_a(input_string):
    count = input_string.lower().count('a')
    
    if count > 0:
        print(f"A letra 'a' aparece {count} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

def main():
    input_string = input("Informe uma string: ")
    count_letter_a(input_string)

if __name__ == "__main__":
    main()
