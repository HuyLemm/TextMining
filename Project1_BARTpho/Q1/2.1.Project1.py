import json
import pandas as pd
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt


# Đường dẫn đến tập tin JSON
file_path = "Project1_Data.json"

# Đọc dữ liệu từ tập tin JSON
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# khởi tạo ba danh sách rỗng để lưu độ dài của câu hỏi, đoạn văn và nhãn
question_lengths = []
text_lengths = []
labels = []

# Phân tích và thống kê dữ liệu
for datum in data:
    question_lengths.append(len(datum["question"]))
    text_lengths.append(len(datum["text"]))
    labels.append(datum["label"])

# Thống kê độ dài của câu hỏi
mean_question_length = np.mean(question_lengths)
max_question_length = np.max(question_lengths)
min_question_length = np.min(question_lengths)

print("Độ dài trung bình của câu hỏi:", mean_question_length)
print("Độ dài tối đa của câu hỏi:", max_question_length)
print("Độ dài tối thiểu của câu hỏi:", min_question_length)

# Thống kê độ dài của đoạn văn
mean_text_length = np.mean(text_lengths)
max_text_length = np.max(text_lengths)
min_text_length = np.min(text_lengths)

print("Độ dài trung bình của đoạn văn:", mean_text_length)
print("Độ dài tối đa của đoạn văn:", max_text_length)
print("Độ dài tối thiểu của đoạn văn:", min_text_length)

# Phân bố của nhãn (label)
label_counts = Counter(labels)
print("Số lượng nhãn True (Positive):", label_counts[True])
print("Số lượng nhãn False (Negative):", label_counts[False])

# Thống kê các từ phổ biến trong câu hỏi và đoạn văn
all_questions = [datum["question"] for datum in data]
all_texts = [datum["text"] for datum in data]

question_words = " ".join(all_questions).split()
text_words = " ".join(all_texts).split()

question_word_counts = Counter(question_words)
text_word_counts = Counter(text_words)

print("Top 10 từ phổ biến trong câu hỏi:", question_word_counts.most_common(10))
print("Top 10 từ phổ biến trong đoạn văn:", text_word_counts.most_common(10))

# Biểu đồ độ dài của câu hỏi và đoạn văn:
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.hist(question_lengths, bins=20, color='skyblue', edgecolor='black')
plt.title('Độ dài của câu hỏi')
plt.xlabel('Độ dài')
plt.ylabel('Số lượng')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.hist(text_lengths, bins=20, color='salmon', edgecolor='black')
plt.title('Độ dài của đoạn văn')
plt.xlabel('Độ dài')
plt.ylabel('Số lượng')
plt.grid(True)

plt.tight_layout()
plt.show()

# Bảng thống kê phân bố của nhãn (label):

labels = ['True', 'False']
counts = [label_counts[True], label_counts[False]]

plt.figure(figsize=(6, 4))
plt.bar(labels, counts, color=['skyblue', 'salmon'])
plt.xlabel('Nhãn')
plt.ylabel('Số lượng')
plt.title('Phân bố của nhãn')
plt.show()

# Biểu đồ thống kê các từ phổ biến trong câu hỏi và đoạn văn:

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
question_word_counts_df = pd.DataFrame(question_word_counts.most_common(10), columns=['Word', 'Count'])
plt.barh(question_word_counts_df['Word'], question_word_counts_df['Count'], color='skyblue')
plt.title('Top 10 từ phổ biến trong câu hỏi')
plt.xlabel('Số lượng')
plt.ylabel('Từ')
plt.gca().invert_yaxis()

plt.subplot(1, 2, 2)
text_word_counts_df = pd.DataFrame(text_word_counts.most_common(10), columns=['Word', 'Count'])
plt.barh(text_word_counts_df['Word'], text_word_counts_df['Count'], color='salmon')
plt.title('Top 10 từ phổ biến trong đoạn văn')
plt.xlabel('Số lượng')
plt.ylabel('Từ')
plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()