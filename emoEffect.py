EmotieID = 1
effect = 0
nth_color = 1

if EmotieID == 1:
    if nth_color == 1:
        effect = 4
    elif nth_color == 2:
        effect = 2
    elif nth_color == 3:
        effect = 1
    else:
        effect = 5

elif EmotieID == 2:
    if nth_color == 1:
        effect = 3
    elif nth_color == 2:
        effect = 4
    elif nth_color == 3:
        effect = 1
    else:
        effect = 5

elif EmotieID == 3:
    if nth_color == 1:
        effect = 1
    elif nth_color == 2:
        effect = 2
    elif nth_color == 3:
        effect = 3
    else:
        effect = 5

elif EmotieID == 4:
    if nth_color == 1:
        effect = 1
    elif nth_color == 2:
        effect = 2
    elif nth_color == 3:
        effect = 4
    else:
        effect = 5

elif EmotieID == 5:
    if nth_color == 1:
        effect = 1
    elif nth_color == 2:
        effect = 2
    elif nth_color == 3:
        effect = 3
    else:
        effect = 5

elif EmotieID == 6:
    if nth_color == 1:
        effect = 1
    elif nth_color == 2:
        effect = 3
    elif nth_color == 3:
        effect = 4
    else:
        effect = 5

elif EmotieID == 7:
    if nth_color == 1:
        effect = 4
    elif nth_color == 2:
        effect = 1
    elif nth_color == 3:
        effect = 2
    else:
        effect = 5

else:
    effect = 5

print(effect)