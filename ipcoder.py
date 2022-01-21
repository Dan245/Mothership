def remap(old_val, old_min, old_max, new_min, new_max):
    return round((((old_val - old_min) * (new_max - new_min)) / (old_max - old_min)) + new_min)


def get_code(ip, key):
    nums = ip.split(".")
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = ""
    start = remap(key, 0, 255, 0, 26)
    for i, num in enumerate(nums):
        if i == int((len(nums)+1)/2):
            code += f"{alphabet[(int(num) // 16+start) % 26]}-{alphabet[((int(num) % 16)+start) % 26]}"
        else:
            code += f"{alphabet[(int(num) // 16+start) % 26]}{alphabet[((int(num) % 16)+start) % 26]}"
    code += f"{alphabet[key // 16]}{alphabet[(key % 16)]}"
    return code


def get_ip_from_code(code):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    code = code.replace("-", "")
    letters = [code[i:i+2] for i in range(0, len(code), 2)]
    key = alphabet.index(letters[-1][0])*16 + alphabet.index(letters[-1][1])
    start = remap(key, 0, 255, 0, 26)
    ip = ""
    for letter_couple in range(len(letters)-1):
        ip += f"{alphabet.index(alphabet[alphabet.index(letters[letter_couple][0])-start])*16 + alphabet.index(alphabet[alphabet.index(letters[letter_couple][1])-start])}"
        if letter_couple != len(letters)-2:
            ip += "."
