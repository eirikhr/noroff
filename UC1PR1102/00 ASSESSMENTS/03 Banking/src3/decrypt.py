
def rot_decrypt(string, shift=8):
    cipher = ""
    for char in string: 
      if char == " ":
        cipher = cipher + char
      elif char.isupper():
        cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
      else:
        cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    
    return cipher


filename = str(input("Please input timestamp (without .txt)")) + ".txt"
output_filename = filename + " - DECRYPTED.txt"

output = open(output_filename, 'w')

file = open(filename, 'r')

for line in file:
    if (line == "\n") or ("SECTION" in line) or line.startswith('['):
        output.write(line)
    else:
        output.write(rot_decrypt(line.replace('\n', '')))
        output.write("\n")

print("Decryption attempt completed.")