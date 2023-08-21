text = str(input())
word = str(input())

def search():
 if word in text:
  return('Word found')
 else:
  return('Word not found')

print(search(text, word))