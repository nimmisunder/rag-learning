# Step 1: Read file
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

print("Original Text:")
print(text)

chunks = text.split(".")
print("\nChunks")
for chunk in chunks:
    print(chunk.strip())

# Step 3: Save chunks
with open("output.txt", "w", encoding="utf-8") as f:
    for chunk in chunks:
        if chunk.strip() != "":
            f.write(chunk.strip() + "\n---\n")

print("\nSaved to output.txt")
