message = str(input())
hash_key = str(input())
alphabet = [
    "а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
    "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"
]
CURRENT_INDEX = 0
def get_new_symbol(old, hashed_symbol):
    try:
        current_index = alphabet.index(old.lower())
        hash_index = alphabet.index(hashed_symbol.lower())
        if current_index + hash_index >= len(alphabet):
            new_index = current_index + hash_index - len(alphabet)
        else:
            new_index = current_index + hash_index
        return alphabet[new_index]
    except ValueError:
        return old
# моя комната самая большая
# столстолстолстолстолстолс
# стол
# 0123

def get_hash_symbol():
    global CURRENT_INDEX
    if CURRENT_INDEX + 1 >= len(hash_key):
        CURRENT_INDEX = 0
    result = hash_key[CURRENT_INDEX]
    CURRENT_INDEX += 1
    return result

result = ''
for symbol in message:
    result += get_new_symbol(symbol,get_hash_symbol())

print(f'result = {result}')

