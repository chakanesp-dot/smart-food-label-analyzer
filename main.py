while True:
    print("\n--- Smart Food Label Analyzer ---")

    try:
        calories = float(input("Enter calories: "))
        sugar = float(input("Enter sugar (g): "))
        fat = float(input("Enter fat (g): "))
        protein = float(input("Enter protein (g): "))
    except ValueError:
        print("❌ Please enter valid numbers!")
        continue

    # Feedback
    if sugar >= 25:
        print("⚠️ High sugar content")
    if fat >= 20:
        print("⚠️ High fat content")
    if protein > 10:
        print("✅ Good protein source")
    if calories > 400:
        print("🔥 High calorie food")

    # Score
    score = 0

    if sugar < 10:
        score += 2
    else:
        score -= 2

    if fat < 15:
        score += 2
    else:
        score -= 2

    if protein > 10:
        score += 3

    print("\nHealth Score:", score)

    if score >= 4:
        result = "Healthy"
    elif score >= 0:
        result = "Moderate"
    else:
        result = "Unhealthy"

    print("Final Rating:", result)

    # Advice
    if result == "Healthy":
        print("🥗 Excellent choice!")
    elif result == "Moderate":
        print("⚖️ Consume in moderation.")
    else:
        print("🚫 Not recommended frequently.")

    # Loop control
    cont = input("\nAnalyze another product? (yes/no): ")
    if cont.lower() != "yes":
        break