jz=[]
for _ in range(5): 
    row=list(map(int,input().split()))
    jz.append(row)
saddle_points = []
for i in range(5):
    max_in_row = max(jz[i])
    max_index = jz[i].index(max_in_row)
    is_min_in_col = True
    for j in range(5):
        if jz[j][max_index] < max_in_row:
            is_min_in_col = False
            break
    if is_min_in_col:
        saddle_points.append(max_in_row)
for point in saddle_points:
    print(point)
