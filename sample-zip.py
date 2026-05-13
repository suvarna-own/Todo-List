import zipfile

files_to_zip = ['member.txt', 'members.txt']

# Use 'w' mode to create a new file; ZIP_DEFLATED enables compression
with zipfile.ZipFile('my_archive.zip', 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
    for file in files_to_zip:
        zipf.write(file)
print("Files have been zipped successfully!")