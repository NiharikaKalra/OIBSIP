import random
import string

def password_gen():
    print("What password you want")
    
    while True:
        # 1. Length validation (User input)
        try:
            len_asking = input("\nLength of password you want, how much long password? (Min 8): ")
            len_password = int(len_asking)
            if len_password < 8:
                print("Safety alert: Minimum 8 password length is required.")
                continue
        except ValueError:
            print("Error: Please write a valid number.")
            continue
            
        # 2. Selecting character pools
        print("\nTypes of character select by user:")
        print("  [A] UPPERCASE LETTERS (A-Z)")
        print("  [B] lowercase letters (a-z)")
        print("  [C] Numbers (0-9)")
        print("  [D] Symbols (!@#...)")
        
        user_choice = input("Choose 2 or more than 2 options (e.g., ABC): ").strip().upper()
        
        # Validation for choices using set to handle duplicates like 'AA'
        unique_choices = set(user_choice)
        if len(unique_choices) < 2 or any(char not in "ABCD" for char in unique_choices):
            print("Wrong input! Please choose at least 2 unique options from A, B, C, D.")
            continue
            
        # 3. Building the pool and ensuring criteria match
        char_pool = ""
        gen_chars = []
        
        if "A" in user_choice:
            char_pool += string.ascii_uppercase
            gen_chars.append(random.choice(string.ascii_uppercase))
        if "B" in user_choice:
            char_pool += string.ascii_lowercase
            gen_chars.append(random.choice(string.ascii_lowercase))
        if "C" in user_choice:
            char_pool += string.digits
            gen_chars.append(random.choice(string.digits))
        if "D" in user_choice:
            char_pool += string.punctuation
            gen_chars.append(random.choice(string.punctuation))
            
        # 4. Fill remaining password length
        while len(gen_chars) < len_password:
            gen_chars.append(random.choice(char_pool))
            
        # 5. Shuffle to randomize order
        random.shuffle(gen_chars)
        final_password = "".join(gen_chars)
        
        # Output
        print("\n" + "="*40)
        print(f"Your Secure Password: {final_password}")
        print("="*40)
        
        # 6. Loop control
        retry = input("\nDo you want to create another password? (y/n): ").strip().lower()
        if retry != 'y' and retry != 'yes':
            print("\nExit")
            break

# Program execute karne ke liye function call
if __name__ == "__main__":
    password_gen()
