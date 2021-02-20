def checkPathSimilarity(cur_path, paths_set) -> bool :
    for path in paths_set :
        if isSubPath(cur_path.copy(), path.copy()) :
            return True
        elif getInterProp(cur_path.copy(), path.copy()) > 0.8 :
            return True
    return False


def isSubPath(sub_path, sup_path) -> bool :
    sub_path.reverse()
    for node in sup_path :
        if sub_path == [] :
            return True
        if node == sub_path[-1] :
            sub_path.pop()
    return False


def getInterProp(sub_path, sup_path) -> float :
    sub_path_len = len(sub_path)
    sub_path.reverse()
    for node in sup_path :
        if sub_path == [] :
            return 1
        if node == sub_path[-1] :
            sub_path.pop()
    return (sub_path_len - len(sub_path)) / sub_path_len

# 有序数组子串
#子集 报 True 可信
#超集 误报少
# 有序交集占比