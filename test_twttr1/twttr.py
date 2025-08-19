def main():
    sentence = input ("Input: ")
    no_vowels = shorten(sentence)
    
    
    print(f"Output: {no_vowels}")

def shorten(text):
    vowels = "aeiouAEIOU"
    result =""
    for char in text:
        if char not in vowels.upper():
            result += char
    return result

if __name__ == "__main__":
    main()