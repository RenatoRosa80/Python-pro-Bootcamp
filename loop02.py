student_scores = [150, 142, 105, 185, 120, 171, 149, 24, 59, 68, 199, 78, 65, 89]

max_score = 0

for score in student_scores:
    if score > max_score:
        max_score = score
        
print(max_score)