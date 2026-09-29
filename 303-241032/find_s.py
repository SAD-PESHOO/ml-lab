"""Find-S Algorithm (most specific hypothesis)
Sirf positive examples use karta hai."""

# Attributes: Sky, AirTemp, Humidity, Wind, Water, Forecast | Target: EnjoySport
data = [
    (["Sunny", "Warm", "Normal", "Strong", "Warm", "Same"], "Yes"),
    (["Sunny", "Warm", "High", "Strong", "Warm", "Same"], "Yes"),
    (["Rainy", "Cold", "High", "Strong", "Warm", "Change"], "No"),
    (["Sunny", "Warm", "High", "Strong", "Cool", "Change"], "Yes"),
]


def find_s(examples):
    n = len(examples[0][0])
    h = ["0"] * n  # sabse specific hypothesis
    first = True
    for x, label in examples:
        if label != "Yes":
            continue  # negative examples ignore
        if first:
            h = x[:]
            first = False
        else:
            for i in range(n):
                if h[i] != x[i]:
                    h[i] = "?"
        print("After", x, "->", h)
    return h


if __name__ == "__main__":
    print("Final Hypothesis:", find_s(data))
