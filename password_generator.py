import random  
import string 

def chars(characters, amount): 
    sym_list = [] 
    end = len(characters) 
    for _ in range(amount): 
        index = random.randrange(0, end) 
        sym_list.append(characters[index]) 
    return sym_list 
 
def main(): 
    password = ( 
        chars(string.ascii_uppercase, 4) +  
        chars(string.ascii_lowercase, 4) +  
        chars(string.digits, 3) +  
        chars(string.punctuation, 3) )
    random.shuffle(password) 
    print("".join(password)) 
 
if __name__ == '__main__': 
    main()