def main():
    sentence = input ("Input: ")
    no_vowels = remove_vowels(sentence)
    
    
    print(f"Output: {no_vowels}")

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result =""
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()