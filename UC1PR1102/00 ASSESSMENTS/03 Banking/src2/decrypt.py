def rot_decrypt(enc_string, n=1):
    raw_string = ""
    for letter in enc_string:
        raw_letter = chr(ord(letter) - n)
        raw_string = raw_string + raw_letter