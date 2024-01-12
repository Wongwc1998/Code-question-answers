def encode_base62(num, base_chars):
    """
    Encode a decimal number into base 62 using the specified characters.

    :param num: The decimal number to encode.
    :param base_chars: A string containing 62 unique characters
    used for the encoding.
    :return: A string representing the base 62 encoded number.
    """
    if num == 0:
        return base_chars[0]

    base = len(base_chars)
    encoded = ''

    while num > 0:
        encoded = base_chars[num % base] + encoded
        num //= base

    return encoded

# Base 62 characters


BASE62_CHARS = "C7xicPMGvzAZyTNodmwnV5D3B6H0Oup8E21W9sqLQX4YjSeUhIRJgafFtrKlbk"

# Test cases provided by the user
test_cases = [
    (15840, 'cGp'), (16465, 'cmW'), (17941, 'cX3'), (17942, 'cXB'),
    (18898, 'ctR'), (19172, 'ckN'), (20512, 'PVg'), (20626, 'PD4'),
    (20758, 'PBR'), (25736, 'MYM'), (25893, 'MSL'), (26039, 'MUk'),
    (26134, 'MIE'), (26345, 'Mgr'), (26346, 'MgK'),  (26676, 'MKd'),
    (28161, 'GVT'), (31622, 'vNx'), (31873, 'vwP'), (32028, 'vV9'), 
    (35260, 'zAj'), (36368, 'zO9'), (36428, 'zu1'), (38716, 'AcO'),
    (38805, 'APF'), (40111, 'AHl'), (40893, 'ALW'), (40956, 'AQ9'),
    (40957, 'AQs'), (40958, 'AQq'), (40959, 'AQL'), (40960, 'AQQ'),
    (42541, 'Zcz'), (47987, 'yuk'), (49137, 'yh2'), (49169, 'yIi'),
    (49443, 'yau'), (49444, 'yap'), (49639, 'ytL'), (50047, 'T7T'),
    (50048, 'T7N'), (50127, 'Tx8'), (50128, 'TxE'), (50129, 'Tx2'),
    (51183, 'Tn2'), (51184, 'Tn1'), (51204, 'Tnf'), (52071, 'T2a'),
    (52977, 'Thu'), (54650, 'NTO'), (55908, 'N2e'), (56100, 'N9g'),
    (57924, 'ocd'), (60538, 'oeH'), (60539, 'oe0'), (60540, 'oeO'),
    (61474, 'okE'), (63141, 'dH6'), (64436, 'dUw'), (64437, 'dUn'),
    (67416, 'm2D'), (72677, 'wtT'), (73039, 'nCi'), (73040, 'nCc'),
    (73211, 'nxJ'), (73654, 'nzb'), (73756, 'nZq'), (74037, 'ndz'),
    (74038, 'ndA'), (76081, 'nIG'), (76082, 'nIv'), (79467, 'VXS'),
    (79564, 'VYw'), (79790, 'VeK'), (79791, 'Vel')
]

# Function to test if the encoding matches the expected output


def test_encoding(test_cases_param, base_chars):
    """
    Run the test cases for the encoding
    """
    results = []
    for num, expected in test_cases_param:
        encoded = encode_base62(num, base_chars)
        results.append((num, encoded, expected, encoded == expected))
    return results


if __name__ == "__main__":
    # Running the test
    test_results = test_encoding(test_cases, BASE62_CHARS)
    print(encode_base62(30001, BASE62_CHARS))
    print(encode_base62(55555, BASE62_CHARS))
    print(encode_base62(77788, BASE62_CHARS))
    print(test_results)
