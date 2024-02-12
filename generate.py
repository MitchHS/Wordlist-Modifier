import argparse

def read_file_lines(filename):
    """Read lines from a file and return them as a list."""
    with open(filename, 'r') as file:
        return file.read().splitlines()

def replace_letters(word):
    """Replace specific letters with numbers in a word."""
    replacements = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 'b': '8'}
    return ''.join(replacements.get(c, c) for c in word)

def capitalize_variations(word):
    """Generate variations of a word with capitalization."""
    return {word.capitalize(), word.upper(), word}

def append_numbers(word, range_end):
    """Append numbers from 0 to range_end to the word."""
    return [f"{word}{i}" for i in range(range_end + 1)]

def generate_passwords(words_file, chars_file, numbers_range):
    """Generate a comprehensive list of password variations."""
    words = read_file_lines(words_file)
    special_chars = read_file_lines(chars_file)
    
    passwords = set()
    
    for word in words:
        # Generate capitalized versions of the word
        capitalizations = capitalize_variations(word)
        
        for variant in capitalizations:
            # Add the original and capitalized words
            passwords.add(variant)
            
            # Generate and add words with letters replaced by numbers
            replaced_variant = replace_letters(variant)
            passwords.add(replaced_variant)
            
            # Append numbers to both original and replaced words
            for num_variant in append_numbers(variant, numbers_range):
                passwords.add(num_variant)
                replaced_num_variant = replace_letters(num_variant)
                passwords.add(replaced_num_variant)
                
                # Append special characters to all above
                for char in special_chars:
                    passwords.add(f"{num_variant}{char}")
                    passwords.add(f"{replaced_num_variant}{char}")

    return passwords

def main():
    parser = argparse.ArgumentParser(description='Generate a comprehensive list of password variations.')
    parser.add_argument('words_file', type=str, help='Path to the file containing words.')
    parser.add_argument('chars_file', type=str, help='Path to the file containing special characters.')
    parser.add_argument('--range', '-r', type=int, default=9, help='Range of numbers to append (0 to N).')
    parser.add_argument('--output', '-o', type=str, default='passwords.txt', help='Output file name.')
    
    args = parser.parse_args()
    
    passwords = generate_passwords(args.words_file, args.chars_file, args.range)
    
    with open(args.output, 'w') as file:
        for password in sorted(passwords):
            file.write(f"{password}\n")

    print(f"Generated passwords have been saved to {args.output}")

if __name__ == "__main__":
    main()
