min_h = int(input())
max_h = int(input())
ann_h = int(input())

if ann_h > max_h:
    print("Excess")
else:
    if ann_h < min_h:
        print("Deficiency")
    else:
        print("Normal")
