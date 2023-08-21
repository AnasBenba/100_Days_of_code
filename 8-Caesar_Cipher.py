import art

print(art.logo)
# List of alphabets for shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

bool = True

while bool:

  for_shift, for_text, for_direction = True, True, True

  while for_direction:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode' or direction == 'decode':
        for_direction = False
    else:
        print("you have to type 'encode' or 'decode'.")

  while for_text:
    text = input("Type your message:\n").lower()
    if text == '':
        print("Enter a valid text.")
    else:
        for_text = False

  while for_shift:
    shift = input("Type the shift number:\n")
    if shift.isnumeric():
        shift = int(shift)
        if shift <= 26:
            for_shift = False
        else:
            print(f"{shift} is greater then the number of alphabets")
    else:
        print("You should enter a number")
   # The modulo operator (%) can be used in the shift to ensure it remains between 0 and 26

  def caesar(text, shift):
    i = 0
    new_text = ''

    while i < len(text):
      letter = text[i]
      if letter not in alphabet:
        new_text += letter
      else:
        index = alphabet.index(letter)
    
        if direction == 'encode':
          index += shift
        elif direction == 'decode':
          index -= shift
        new_text += alphabet[index]
      i += 1
    return new_text

  new_text = caesar(text, shift)
  
  if direction == 'encode':
    print(f"Here's the encoded result: {new_text}!")
  else:
    print(f"Here's the decoded result: {new_text}!")
  
  decide = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if decide == 'yes':
    bool = True
  else:
    bool = False
print("Goodbye")