print("Let's count together: {}, then goes {}, and then {}".format("one", "two", "three"))

str1 = "five"
str2 = "six"
str3 = "seven"
print(f"Let's count together: {str1}, then goes {str2}, and then {str3}")

actual_result = "abrakadabra"
print(f"Wrong text, got {actual_result}, something wrong")

print(f"{2 + 3}")

catalog_text = self.catalog_link.text  # считываем текст и записываем его в переменную
assert catalog_text == "Каталог", \
        f"Wrong language, got {catalog_text} instead of 'Каталог'"