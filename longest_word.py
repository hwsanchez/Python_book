def LongestWord(sen):
  index = None
  words = sen.split()
  most_characters = 0
  longest_word = ''
  for word in words:
    real_word = ''.join(char for char in word if char.isalpha())
    if len(real_word) > most_characters:
      most_characters = len(real_word)
      longest_word = real_word
  return longest_word

# keep this function call here 
print(LongestWord("Que hubo! Yo!§$%&"))
