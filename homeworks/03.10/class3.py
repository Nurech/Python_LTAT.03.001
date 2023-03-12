# 3. Rhymes When writing poetry, there is often a need to find a suitable word that rhymes with the word at the end of the previous line.
# Write a program that allows the user to test different rhyme-words of a given word and select the best. The words can be in any language.
#
# Easier version
#
# Let the rhyme score of two words be the maximum number of consecutive letters, starting from the end, that are the same in both words.
# The user first enters a word and then starts to enter words that rhyme with the first word. For each rhyme-word, the program prints its
# rhyme score with respect to the first word. If the user enters 'done', then the program prints out the word that had the largest rhyme
# score.
#
# Enter word: program
# Enter rhyme-word: tram
# Rhyme score is 3
# Enter rhyme-word: kilogram
# Rhyme score is 5
# Enter rhyme-word: wolfram
# Rhyme score is 3
# Enter rhyme-word: telegram
# Rhyme score is 4
# Enter rhyme-word: done
# The word with the highest rhyme score was 'kilogram', with a score of 5.

word = input('Enter word: ')

rhyme_word = input('Enter rhyme-word: ')
highest_score = 0
highest_word = ''

while rhyme_word != 'done':
    score = 0
    for i in range(1, min(len(word), len(rhyme_word)) + 1):
        if word[-i] == rhyme_word[-i]:
            score += 1
        else:
            break
    print('Rhyme score is', score)
    if score > highest_score:
        highest_score = score
        highest_word = rhyme_word
    rhyme_word = input('Enter rhyme-word: ')

print('The word with the highest rhyme score was \'{}\', with a score of {}.'.format(highest_word, highest_score))
