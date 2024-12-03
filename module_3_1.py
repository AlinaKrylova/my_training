calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string,  list_to_search):
    count_calls()
    for i in range (len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    return string.lower() in list_to_search

print(string_info('Backbiting'))
print(string_info('Ferrying'))
print(string_info('Perfectionism'))

print(is_contains('cAnaRy', ['caNaRY', 'GoLdfiSH', 'sNail']))
print(is_contains('bAt', ['chiPmuNK', 'wEasel','wEAseL']))
print(is_contains('AnTeLOpE', ['bUFfalo', 'anTelOpe']))

print(calls)