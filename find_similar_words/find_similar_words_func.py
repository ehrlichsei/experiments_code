import Levenshtein

def find_similar_words(word, word_list, threshold=2):
    similar_words = []
    for w in word_list:
        if Levenshtein.distance(word, w) <= threshold:
            similar_words.append(w)
    return similar_words

