names = ["Hello", 1, 8.6, True]

two_dee = [[1,2,3], [4,5,6], [7,8,9]]
idx = two_dee[2][2]

for row in two_dee: # Gets into the little brother lists
    print(f"Row : {row}")
    
    for col in row: # Pulls values out of little brother lists
        print(f"Column {col}")
        
scores = [
[81.9, 64.7, 50.0, 61.1],
[72.2, 43.6, 44.8, 70.2],
[66.8, 75.1, 80.2, 49.9],
[80.5, 56.7, 48.8, 60.9]
]

for count, row in enumerate(scores, start=1):
    
    print(f"Term (index) {count}")
    
    for col in row:
        print(f"Grade : {col}")
