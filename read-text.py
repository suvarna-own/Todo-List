# files= ['doc.txt', 'report.txt', 'love.txt']
# for file in files:
#     file = open(f"{file}", "r")
#     content = file.read()
#     print(f"Content of {file.name}: {content}")

text = "://example.com"
# Removes 'w', 'e', 'm', 'c', 'o', and '.' from both ends
print(text.strip(":/ep"))  # Output: 'example'