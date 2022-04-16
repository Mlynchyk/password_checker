import sys 
 
def create_set(c1, c2): 
    char_set = set() 
    for c in range(ord(c1), ord(c2)+1): 
        char_set.add(chr(c)) 
    return char_set 
 
def main(): 
    if len(sys.argv) < 2: 
        print("Enter the password. Ex: \"python password.py [password]\"") 
        exit() 
         
    up_chars  = create_set("A", "Z")   
    low_chars = create_set("a", "z")   
    dig_chars = create_set("0", "9") 
    sym_chars = create_set("!", "/").union(create_set(":", "@"), create_set("[", "'"), create_set("{", "~")) 
    up_count = low_count = dig_count = sym_count = 0 
     
    for char in sys.argv[1]: 
        if char in up_chars: up_count += 1 
        if char in low_chars: low_count += 1 
        if char in dig_chars: dig_count += 1 
        if char in sym_chars: sym_count += 1 
     
    if up_count > 0 and low_count > 0 and dig_count > 0 and sym_count > 0 and len(sys.argv[1]) > 13: 
        print("Strong password") 
        exit()     
     
    print("Week password:") 
    if up_count == 0 or low_count == 0: 
        print("- Password must contain both lowercase and uppercase characters") 
    if dig_count == 0: 
        print("- Password must contain digits")  
    if sym_count == 0:  
        print("- Password must contain at least one punctuation character (!\"#$%'()*+,-./:;<=>?@[\\]^_`{|}~)") 
    if len(sys.argv[1]) < 14: 
        print("- Password must be at least 14 characters long") 
         
if name == '__main__': 
    main()