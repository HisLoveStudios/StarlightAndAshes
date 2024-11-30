'''
NLP_FUNCTIONS.PY

This file contains numerous functions for natural language processing of text to make the English
in the game more natural.
'''

# Import our NLP kit.
# import nltk
#from nltk.tokenize import word_tokenize
#from nltk.tag import pos_tag
from pattern.text.en import pluralize#, conjugate
from pattern.text.en import article
import numpy as np

# Formats a given list with proper English grammar. Uses 'and' as a default conjugation.
def list_to_eng(inv, conj='and'):
    list = ''
    if len(inv) > 2:
        list = ', '.join(inv[:-1]) + ', ' + conj + ' ' + inv[-1]
    elif len(inv) > 1:
        list = (' ' + conj + ' ').join(inv)
    elif len(inv) == 1:
        list = inv[0]
    else:
        list = ''
    return list

# Formats the description of an item with an accessible inventory. 
# Usage: interior_desc(<item_with_inventory>, <inventory>, end_punc='.')
def interior_desc(item, inv, end_punc='.'):
    desc = ''
    verb = ''
    if len(inv) > 0:
        if inv[0][0] in [str(i) for i in np.arange(10)]:
            verb = ' lie '
        elif len(inv) > 1:
            verb = ' lie '
        else:
            verb = ' lies '
    if len(inv) > 2:
        desc = 'Inside the ' + item + verb + list_to_eng(inv) + end_punc
    elif len(inv) > 1:
        desc = 'Inside the ' + item + verb + list_to_eng(inv) + end_punc
    elif len(inv) == 1:
        desc = 'Inside the ' + item + verb + list_to_eng(inv) + end_punc
    else:
        desc = 'There is nothing inside the ' + item + end_punc
    return desc

# Returns a dictionary with the counts of the number of times each item appears in a list.
def item_counts(arr):
    counts = {}
    for item in arr:
        counts[item] = int(arr.count(item))
    return counts

# Returns the appropriate article for a given noun. (No longer necessary.)
'''
def article(word):
    vowels = 'aeiou'
    vexceptions = ['eu', 'uni', 'u', 'one']  # Exceptions where initial vowel sounds like a consonant
    cexceptions = ['herb', 'hour', 'honor', 'heir', 'honest'] # Exceptions where initial consonant is silent
    vex = any([word.startswith(ex) for ex in vexceptions])
    cex = any([word.startswith(ex) for ex in cexceptions])
    if vex:
        return 'a'
    elif cex:
        return 'an'
    elif word[0].lower() in vowels:
        return 'an'
    else:
        return 'a'
    '''

# Converts an inventory to an English sentence, including plurals and multiplicity of items.
def inv_to_eng(inv):
    counts = item_counts(inv)
    eng_inv = []
    for item in counts:
        if counts[item] == 1:
            if not item[0].isupper() and not item[-1] == 's':
                eng_inv.append(article(item) + ' ' + item)
            else:
                eng_inv.append(item)
        elif counts[item] > 1:
            eng_inv.append(str(counts[item]) + ' ' + pluralize(item))
    return eng_inv

'''
def identify_compound_subject(sentence):
    # Tokenize the sentence
    tokens = word_tokenize(sentence)
    
    # Perform POS tagging
    tagged_tokens = pos_tag(tokens)

    # Initialize a list to store compound subjects.
    # compound_subjects = []
    
    # Look for patterns indicating compound subjects
    for i in range(len(tagged_tokens) - 3):  # We iterate up to the fourth-to-last token
        word1, tag1 = tagged_tokens[i]
        word2, tag2 = tagged_tokens[i + 1]
        word3, tag3 = tagged_tokens[i + 2]
        word4, tag4 = tagged_tokens[i + 3]
        
        # Check if the pattern matches a compound subject
        if tag1.startswith('NN') and word2.lower() in ['and', 'or', 'nor'] and tag3.startswith('NN'):
            return True
            # If so, add the compound subject to the list
            #compound_subjects.append((word1, word3))
        elif tag1.startswith('DT') and tag2.startswith('NN') and word3.lower() in ['and', 'or'] and tag3.startswith('DT') and tag4.startswith('NN'):
            return True
            # If so, add the compound subject to the list
            #compound_subjects.append((word1 + " " + word2, word3 + " " + tagged_tokens[i + 3][0]))
        else :
            return False
'''