from collections import Counter


def fun1(text):
    """determines whether the supplied string reads the same both forward and backward, or is a palindrome."""
    text = text.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return text == text[::-1]  # Check if reversed string equals original


print(fun1("Radar"))


def fun2(text):
    """In the uppercase input text, finds the second most common letter or digit."""
    text = text.upper()
    counts = Counter(char for char in text if char.isalnum())  # Count alphanumeric characters
    if len(counts) < 2:
        return None
    # Get the second most frequent element (or any if multiple with same count)
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[1][0]


print(fun2("aabbbcccc"))


def fun3(text):
    """determines how many numerals, capital letters, and lowercase letters are included in the string."""
    uppercase_count = sum(char.isupper() for char in text)
    lowercase_count = sum(char.islower() for char in text)
    digit_count = sum(char.isdigit() for char in text)
    return uppercase_count, lowercase_count, digit_count


print(fun3("h123PP"))
