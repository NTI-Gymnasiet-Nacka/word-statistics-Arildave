import re
from collections import Counter

def read_from_file(path: str):
    
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def antal_ord(text: str):
    
    words = text.split()
    return len(words)

def mest_frekventa_ord(text: str):
    
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    most_common_word = word_counts.most_common(1)
    return most_common_word[0] if most_common_word else None

def genomsnittlig_ordlängd(text: str):
    words = re.findall(r'\b\w+\b', text)
    if words:
        total_length = sum(len(word) for word in words)
        return total_length / len(words)
    return 0

def langsta_kortaste_ord(text: str):
    words = re.findall(r'\b\w+\b', text)
    if words:
        longest_word = max(words, key=len)
        shortest_word = min(words, key=len)
        return longest_word, shortest_word
    return None, None

def antal_unika_ord(text: str):
    words = re.findall(r'\b\w+\b', text.lower())
    word_counts = Counter(words)
    unique_words = [word for word, count in word_counts.items() if count == 1]
    return len(unique_words)

def main():
    text = read_from_file("en_resa_genom_svenska_skogen.txt") # Läs filen till en sträng
    
    print(f"Antal ord: {antal_ord(text)}")
    print(f"Mest frekventa ord: {mest_frekventa_ord(text)}")
    print(f"Genomsnittlig ordlängd: {genomsnittlig_ordlängd(text):.2f}")
    
    longest, shortest = langsta_kortaste_ord(text)
    print(f"Längsta ordet: {longest}")
    print(f"Kortaste ordet: {shortest}")
    
    print(f"Antal unika ord: {antal_unika_ord(text)}")

if __name__ == "__main__":
    main()
