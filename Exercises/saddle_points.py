def saddle_points(matrix):
    if matrix == []:
        return []
    max_vals = max_each_row(matrix)
    min_vals = min_each_column(matrix)
    ret = []
    for i in max_vals:
        for j in min_vals:
            if i["value"] == j["value"] and i["row"] == j["row"] and i["column"] == j["column"]:
                ret.append({"row": i["row"], "column": i["column"]})
    return ret

def max_each_row(matrix):
    max_vals = []
    for i,k in enumerate(matrix):
        for j,v in enumerate(k):
            if max(k) == v:
                max_vals.append({"row": i+1, "column": j+1, "value": v})
    return max_vals

def min_each_column(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    min_vals = []
    for i,k in enumerate(transposed):
        for j,v in enumerate(k):
            if min(k) == v:
                min_vals.append({"row": j+1, "column": i+1, "value": v})
    return min_vals




print(saddle_points([[6, 7, 8], [5, 5, 5], [7, 5, 6]]))
print(saddle_points([[4, 5, 4], [3, 5, 5], [1, 5, 4]]))
print(saddle_points([[1, 2, 3], [3, 1, 2], [2, 3, 1]]))
print(saddle_points([[9, 8, 7], [5, 3, 2], [6, 6, 7]]))
