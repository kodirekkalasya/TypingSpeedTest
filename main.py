import time


text = "Python is a powerful programming language used for web development data science and automation."

print("\n=== Typing Speed Test ===")
print("\nType the following text:\n")
print(text)
input("\nPress Enter when you're ready...")


start_time = time.time()

typed_text = input("\nStart typing:\n")


end_time = time.time()


time_taken = end_time - start_time

word_count = len(typed_text.split())
wpm = (word_count / time_taken) * 60


correct_chars = 0
for i in range(min(len(text), len(typed_text))):
    if text[i] == typed_text[i]:
        correct_chars += 1

accuracy = (correct_chars / len(text)) * 100

# Display results
print("\n===== Results =====")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Words Per Minute (WPM): {wpm:.2f}")
print(f"Accuracy   : {accuracy:.2f}%")