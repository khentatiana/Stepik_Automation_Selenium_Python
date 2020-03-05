s = 'My Name is Julia and Julia'

if 'Julia' in s:
    print('Substring found')

index = s.find('Julia')
if index != -1:
    print(f'Substring found at index {index}')

full_string = 'text without'
substring = 'some'

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    if substring not in full_string:
        print(f"expected '{substring}' to be substring of '{full_string}'")

print(globals())
print('Imported from:', __name__)