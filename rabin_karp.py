# d is the number of characters in the input alphabet
d = 256


def search(pattern, text, prime):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    # The value of h would be "pow(d, M-1)%prime"
    for i in range(M - 1):
        h = (h * d) % prime

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    # Slide the pattern over text one by one
    for i in range(N - M + 1):
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            # if p == t and pattern[0...M-1] = text[i, i+1, ...i+M-1]
            if j == M:
                print("Pattern found at index " + str(i))

        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % prime

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + prime


text = "GEEKS FOR GEEKS"
pattern = "GEEK"
prime = 16148168401
search(pattern, text, prime)
