# made this file because I thought this would be cooler than entering an ip address

# custom remap function because the arduino map() function doesn't exist here
def remap(old_val, old_min, old_max, new_min, new_max):
    # copied formula, didn't take the time to learn how it works
    return round((((old_val - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)


# ip encrypt function
def get_code(ip, key):
    # init vars
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    # split ip into it's numbers
    nums = ip.split(".")

    # remap key to an index on the alphabet
    start = remap(key, 0, 255, 0, len(alphabet))

    # for each num
    for i, num in enumerate(nums):
        '''
        I wrote this in a haze a while ago and I don't quite remember how the
        formula I made works exactly, but the gist of it is it take the number, converts
        it to a hexadecimal value, and maps the value to the alphabet (i.e 0 = A, F = P),
        starting from the index specified by the key (i.e. if key = 3, start at D [0 = D, F = S])
        '''
        if i == int((len(nums) + 1) / 2):  # add a hyphen to the middle of the code
            code += f"{alphabet[(int(num) // 16 + start) % 26]}-{alphabet[((int(num) % 16) + start) % 26]}"
        else:
            code += f"{alphabet[(int(num) // 16 + start) % 26]}{alphabet[((int(num) % 16) + start) % 26]}"

    # Do the same thing with the key itself, except don't shift it at all
    # the key is put at the end of the code in order for the decrypter to decipher the code
    code += f"{alphabet[key // 16]}{alphabet[(key % 16)]}"
    # return code
    return code


# getting ip from a code
def get_ip_from_code(code):
    # init vars
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ip = ""

    # get rid of hyphen
    code = code.replace("-", "")

    # one liner to group letters into groups of 2 (important for hexadecimal conversion)
    letters = [code[i:i + 2] for i in range(0, len(code), 2)]

    # decipher the key
    key = alphabet.index(letters[-1][0]) * 16 + alphabet.index(letters[-1][1])
    start = remap(key, 0, 255, 0, 26)

    # for each letter couple (minus the key)
    for letter_couple in range(len(letters) - 1):
        '''
        Same story here, don't really remember how I reversed it,
        but it essentially does the encrypt function steps in reverse order.
        I did write these myself, I just forgot how I did it
        '''
        first_letter_num = alphabet.index(alphabet[alphabet.index(letters[letter_couple][0]) - start]) * 16
        last_letter_num = alphabet.index(alphabet[alphabet.index(letters[letter_couple][1]) - start])

        # append the new nums to the ip
        ip += f"{first_letter_num + last_letter_num}"

        # add . to the ip for the in between spaces
        if letter_couple != len(letters) - 2:
            ip += "."
    # return the ip
    return ip
