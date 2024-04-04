def calculate_average_confidence(result_arr):
    class_confidences = {}

    for result in result_arr:
        class_name = result["class"]
        confidence = result["conf"]

        if class_name not in class_confidences:
            class_confidences[class_name] = {"sum": 0, "count": 0}

        class_confidences[class_name]["sum"] += confidence
        class_confidences[class_name]["count"] += 1

    # Calculate the average confidence for each unique class
    averages = {}
    for class_name, values in class_confidences.items():
        averages[class_name] = values["sum"] / values["count"]

    # Combine averages and counts into a single dictionary
    combined_data = {}
    for class_name, avg_value in averages.items():
        count_data = class_confidences[class_name]
        combined_data[class_name] = {
            "average": avg_value,
            "sum": count_data["sum"],
            "count": count_data["count"],
        }

    # Sort the combined data by count and average in descending order
    sorted_data = sorted(
        combined_data.items(), key=lambda x: (-x[1]["count"], -x[1]["average"])
    )

    # Convert the sorted list of tuples back into a dictionary
    sorted_dict = dict(sorted_data)

    return averages, class_confidences, sorted_dict
