contents = [
    "doc content",
    "report content",
    "presentation content"
]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f'../files/{filename}', 'w')
    file.write(content)
    file.close()
