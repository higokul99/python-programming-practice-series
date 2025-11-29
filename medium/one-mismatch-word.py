def just_one_mismatch(target, candidates):
    """
    Find strings that differ from the target by exactly one character.

    Args:
        target (str): The reference string
        candidates (list): List of candidate strings to check

    Returns:
        list: Strings that have exactly one character different from target
    """
    result = []

    for candidate in candidates:
        # Strings must be same length to compare
        if len(candidate) != len(target):
            continue

        mismatch_count = 0
        for i in range(len(target)):
            if target[i] != candidate[i]:
                mismatch_count += 1
                # Early exit if more than one mismatch
                if mismatch_count > 1:
                    break

        if mismatch_count == 1:
            result.append(candidate)

    return result


# Example from the image
target = "banana"
candidates = ["bana","apple", "banaba", "bonanzo"]
result = just_one_mismatch(target, candidates)
print(result)  # Output: ['banaba']

# More test cases
print(just_one_mismatch("hello", ["hello", "hallo", "hexlo", "world"]))  # ['hallo', 'hexlo']
print(just_one_mismatch("test", ["test", "tost", "best", "tes"]))  # ['tost', 'best']