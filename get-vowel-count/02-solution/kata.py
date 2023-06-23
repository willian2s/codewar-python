def get_count(sentence):
    return sum(1 for let in sentence if let in "aeiouAEIOU")
