def reverse(s):
    s.lower()
    return s[::-1].lower()
def ispalindrome(s):
    rev=reverse(s)
    if (rev==a):
        return True
    else:
        return False
s=str(input("enter a string "))
a=s.lower()
ans=ispalindrome(s)
if ans==1:
    print("yes this is a palindrome")
else:
    print("No this is not a palindrome ")
