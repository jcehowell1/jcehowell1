contents = ["All carrots are to be slice longitudinally.", 
            "The carrots were reportedly sliced.", 
            "Placed sliced carrots in pot of boiling water"]

filenames = ["doc.txt", "report.txt", "cook.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"python/files/{filename}", 'w')
    file.write(content)