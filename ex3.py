# Exercice 3 : Correction et Optimisation avec Listes et Tuples

data = [
    ("Alice", [14, 16, 18]),
    ("Bob", [12, 9, 10]),
    ("Charlie", [19, 20, 17]),
    ("Diana", [8, 7, 10])
]

# 1. Students with average >= 15
selected_students = [name for name, scores in data if sum(scores) / len(scores) >= 15]

# 2. Highest individual score
highest_score = max(score for _, scores in data for score in scores)

# 3. Count of students with at least one score < 10
students_with_low_score = sum(1 for _, scores in data if any(score < 10 for score in scores))

# Output
print("Selected students:", selected_students)
print("Highest score:", highest_score)
print("Students with at least one score < 10:", students_with_low_score)

