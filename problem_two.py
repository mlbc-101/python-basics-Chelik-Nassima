"""Write a program which can compute the factorial of a given numbers."""
#function calcule le factoriel
def fonction_factoriel(n):
    if(n==1 or n==0):#test d'arret
        return 1
    else:
        return n*fonction_factoriel(n-1)
print(fonction_factoriel(4))  