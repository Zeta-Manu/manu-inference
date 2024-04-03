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

    return averages, class_confidences
