filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"python/{filename}", 'w')
    content = "Hello"
    file.write(content)
    file.close()