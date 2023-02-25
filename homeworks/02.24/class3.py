def convert(R, G, B):
    Xmin, Xmax = min(R, G, B), max(R, G, B)
    L = (Xmin + Xmax) / 2

    if Xmin == Xmax:
        H = 0
        S = 0
    else:
        if Xmax == R:
            H = (G - B) / (Xmax - Xmin)
        if Xmax == G:
            H = 2 + (B - R) / (Xmax - Xmin)
        if Xmax == B:
            H = 4 + (R - G) / (Xmax - Xmin)
        if H < 0:
            H = H + 6
        H *= 60

        if L < 0.5:
            S = (Xmax - Xmin) / (Xmax + Xmin)
        else:
            S = (Xmax - Xmin) / (2 - Xmax - Xmin)

    return H, S, L


print(convert(0.1, 0.3, 0.9))
