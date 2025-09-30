total_scores = int(input("Provide the total amount of scores: "))
counter = 1
failed_scores_count = 0
approved_scores_count = 0
average_total_scores = 0
average_approved_scores = 0
average_failed_scores = 0

while (counter <= total_scores):
    score = int(input(f"Insert the score number {counter} "))

    if (score < 70):
        failed_scores_count = failed_scores_count + 1
        average_failed_scores = average_failed_scores + score 
    else:
        approved_scores_count = approved_scores_count + 1
        average_approved_scores = average_approved_scores + score
    
    
    counter = counter + 1

average_approved_scores = average_approved_scores / approved_scores_count if approved_scores_count > 0 else 0
average_failed_scores = average_failed_scores / failed_scores_count if failed_scores_count > 0  else 0
average_total_scores = average_total_scores + (score / total_scores) if total_scores > 0  else 0

print(f"The student has {approved_scores_count} approved scores")
print(f"This is the average of approved scores: {average_approved_scores}")
print(f"The student has {failed_scores_count} failed scores")
print(f"This is the average of failed scores: {average_failed_scores}")
print(f"The average total score is: {average_total_scores}")