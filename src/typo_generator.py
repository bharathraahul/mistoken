

def substitute(word,position,new_char):
    assert 0<=position<len(word), "Position must be between 1 and the length of the word"
    assert new_char != word[position], "New character must be different from the original character at the specified position"
    return word[:position] + new_char + word[position+1:]

def delete(word,position):
    assert 0<=position<len(word)," Position must be between 1 and the length of the word"
    return word[:position]+word[position+1:]





