# Lists of subjects, verbs, and objects
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

# Generate all possible sentences
sentences = []

for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentences.append(f"{subject} {verb} {obj}")

# Print all generated sentences
for sentence in sentences:
    print(sentence)
