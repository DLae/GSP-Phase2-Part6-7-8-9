from lib.exerciseTaskPart7 import *

def test_simple():
    remover = VowelRemover("ab")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "b"

def test_long_sentence_with_punctuation():
    remover = VowelRemover("We will remove the vowels from this sentence.")
    result_no_vowels = remover.remove_vowels()
    assert result_no_vowels == "W wll rmv th vwls frm ths sntnc."
    
def test_removing_all_vowels():
    remover = VowelRemover("aeiou")
    assert remover.remove_vowels() == ""
    
def test_finding_most_common_character():
    counter = LetterCounter("Digital Punk")
    assert counter.calculate_most_common() == [2, "i"]