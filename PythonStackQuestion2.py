def display_top_scores(scores):
    # Sort scores in descending order
    sorted_scores = sorted(scores, reverse=True)

    # Take the top 3 scores
    top_scores = sorted_scores[:3]

    # Display the top 3 scores in three different text fields
    field1, field2, field3 = top_scores[:3]

    # Printing for demonstration purposes; you can replace this with your actual GUI or text field update logic
    print(f"Field 1: {field1}")
    print(f"Field 2: {field2}")
    print(f"Field 3: {field3}")

# Example usage with an array of scores
scores_array = [85, 92, 78, 95, 88, 90]
display_top_scores(scores_array)