def percent(mark):
    p = ((mark[0] + mark[1] + mark[2] + mark[3]) / 400) * 100
    return p

mark1 = [45, 78, 67, 89, 99]
percentage1 = percent(mark1)

mark2 = [43, 57, 98, 78, 76]
percentage2 = percent(mark2)

print(percentage1, percentage2)