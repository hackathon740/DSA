s = "madam"

def palindrome(s, left, right):

    if left >= right:
        return True

    if s[left] != s[right]:
        return False

    return palindrome(s, left + 1, right - 1)


if palindrome(s, 0, len(s)-1):
    print("It is a palindrome")
else:
    print("It is not a palindrome")