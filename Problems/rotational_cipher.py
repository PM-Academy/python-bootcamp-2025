def rotate(text, key):
  # declare cipher
  # loop each char in the text
    # get the index of char within the alphabet string
    # sum the key and index of he char
    # get the char at the total index
    # add the target value to the cipher
  if key == 26 or key == 0:
    return text
  cipher = ''
  plain = 'abcdefghijklmnopqrstuvwxyz'
  for ch in text:
     is_upper = False
     if ch == ' ':
       cipher += ch
       continue
     if ch.isupper():
       is_upper = True
     index = plain.index(ch.lower())
     target_index = index + key;
     if (target_index >= 26):
       target_index -= 26
     cipher_char = plain[target_index]
     cipher += cipher_char.upper() if is_upper else cipher_char
  return cipher

print(rotate('omg', 5))
print(rotate('c', 0))
print(rotate('Cool', 26))
print(rotate('The quick brown fox jumps over the lazy dog', 13))
print(rotate('Gur dhvpx oebja sbk whzcf bire gur ynml qbt', 13))
