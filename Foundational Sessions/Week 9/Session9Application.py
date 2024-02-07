# Unicode Implementation
# Sample strings with non-Latin characters and emojis
data = ["Data analysis 📊", "데이터 분석", "Análisis de datos"]

# Ensuring correct Unicode encoding


encoded_data = [str.encode('utf-8') for str in data]


print("Encoded Data:", encoded_data)

# Efficient Concatenation using 'join()'
report_parts = ["Section 1: Introduction\n", "Section 2: Analysis\n", "Section 3: Conclusion\n"]
report = ''.join(report_parts)
print("Concatenated Report:", report)

# Large Text Construction using String Builder Pattern
def string_builder(strings):
    return ''.join(strings)

# Building a large report
large_report = string_builder(["Paragraph " + str(i) + "\n" for i in range(1, 101)])
print("Large Report (First 100 chars):", large_report[:100])
