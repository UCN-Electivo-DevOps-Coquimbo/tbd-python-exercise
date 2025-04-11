def isPalindrome(text: str):
    if(text=="" or len(text)==1):
        return True
    mid= (int)(len(text)/2);
    for i in range (mid):
        final= (i*-1)-1
        if(text[i]!=text[final]):
            return False        
    return True

def execute():
    variable= input("Ingresa para verificar palindromo: ")
    print(isPalindrome(variable))



