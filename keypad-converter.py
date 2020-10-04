numbers = [2, 2, 2, 3, 3, 2, 3, ]


counts = [
    0,  # 0
    0,  # 1
    0,  # 2
    0,  # 3
    0,  # 4
    0,  # 5
    0,  # 6
    0,  # 7
    0,  # 8
    0,  # 9
]


letterMappings = [
    ["@", "@", "@", "@"],  # 0
    ["@", "@", "@", "@"],  # 1
    ["A", "B", "C", "@"],  # 2
    ["D", "E", "F", "@"],  # 3
    ["G", "H", "I", "@"],  # 4
    ["J", "K", "L", "@"],  # 5
    ["M", "N", "O", "@"],  # 6
    ["P", "Q", "R", "S"],  # 7
    ["T", "U", "V", "@"],  # 8
    ["W", "X", "Y", "Z"],  # 9
]


result = ""

i = 0
j = 0

while True:
    # setup local indeces
    _i = numbers[i]
    _j = counts[_i]-1

    # check if j reached end of numbers array
    if j == len(numbers):
        result += letterMappings[_i][_j]
        break

    if _i == numbers[j]:
        counts[_i] += 1
        j += 1
    else:
        result += letterMappings[_i][_j]
        counts[_i] = 0
        i = j

print(result)
