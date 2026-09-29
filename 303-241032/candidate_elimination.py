"""Candidate Elimination Algorithm (Version Space)
S = specific boundary, G = general boundary."""

data = [
    (["Sunny", "Warm", "Normal", "Strong", "Warm", "Same"], "Yes"),
    (["Sunny", "Warm", "High", "Strong", "Warm", "Same"], "Yes"),
    (["Rainy", "Cold", "High", "Strong", "Warm", "Change"], "No"),
    (["Sunny", "Warm", "High", "Strong", "Cool", "Change"], "Yes"),
]


def covers(h, x):
    """Hypothesis h example x ko cover karti hai ya nahi."""
    return all(hi == "?" or hi == xi for hi, xi in zip(h, x))


def more_general_or_equal(h1, h2):
    return all(a == "?" or a == b for a, b in zip(h1, h2))


def candidate_elimination(examples):
    n = len(examples[0][0])
    domains = [sorted({x[i] for x, _ in examples}) for i in range(n)]

    S = None  # pehle positive example se set hoga
    G = [["?"] * n]

    for step, (x, label) in enumerate(examples, 1):
        if label == "Yes":
            G = [g for g in G if covers(g, x)]
            if S is None:
                S = x[:]
            else:
                S = [s if s == xi else "?" for s, xi in zip(S, x)]
        else:
            new_G = []
            for g in G:
                if not covers(g, x):
                    new_G.append(g)
                    continue
                for i in range(n):
                    if g[i] == "?":
                        for val in domains[i]:
                            if val != x[i]:
                                spec = g[:]
                                spec[i] = val
                                if S is None or more_general_or_equal(spec, S):
                                    new_G.append(spec)
            # sirf maximally general hypotheses rakho
            G = [g for g in new_G
                 if not any(g != o and more_general_or_equal(o, g) for o in new_G)]
            # duplicates hatao
            G = [list(t) for t in {tuple(g) for g in G}]

        print(f"Step {step}: S = {S}")
        print(f"         G = {G}")
    return S, G


if __name__ == "__main__":
    S, G = candidate_elimination(data)
    print("\nFinal S boundary:", S)
    print("Final G boundary:", G)
