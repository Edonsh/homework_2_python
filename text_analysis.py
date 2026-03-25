text = "Data science is evolving and data is becoming more important in science"

def count_words(input_text):
    lower_case_text = input_text.lower()

    words = lower_case_text.split()

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

result = count_words(text)
print(result)


