lineTable =  [
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 2, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 2, 0, 0],
        [0, 0, 2, 1, 0],
        [0, 1, 2, 0, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 2, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 2, 2, 2, 1],
        [1, 0, 0, 0, 1],
        [1, 2, 1, 2, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 2, 1],
        [1, 1, 1, 0, 1],
        [1, 2, 1, 1, 1],
        [1, 0, 1, 1, 1],
        [1, 2, 0, 2, 1],
        [1, 0, 2, 0, 1],
        [2, 2, 2, 2, 2],
        [2, 2, 3, 2, 2],
        [2, 2, 1, 2, 2],
        [2, 3, 3, 3, 2],
        [2, 1, 1, 1, 2],
        [2, 3, 2, 3, 2],
        [2, 1, 2, 1, 2],
        [2, 2, 2, 3, 2],
        [2, 2, 2, 1, 2],
        [2, 3, 2, 2, 2],
        [2, 1, 2, 2, 2],
        [2, 3, 1, 3, 2],
        [2, 1, 3, 1, 2],
        [3, 3, 3, 3, 3],
        [3, 3, 2, 3, 3],
        [3, 2, 2, 2, 3],
        [3, 2, 1, 2, 3],
        [3, 2, 3, 2, 3],
        [3, 3, 3, 2, 3],
        [3, 2, 3, 3, 3],
        [3, 3, 2, 2, 3],
        [3, 2, 2, 3, 3],
        [3, 3, 1, 3, 3],
        [3, 3, 1, 2, 3],
        [3, 2, 1, 3, 3]
    ]
#-----------------------------------------------------------------以下為篩選無重複賠付線
result=[]
def has_duplicate_first_three(arr, arr_list):
    # 取得 arr 的前三個元素
    first_three = arr[:3]
    # 遍歷 arr_list 中的其他陣列
    for other_arr in arr_list:
        # 排除與 arr 相同的陣列，並檢查其前三個元素是否與 first_three 相同
        if arr != other_arr and first_three == other_arr[:3]:
            return True  # 如果找到重複的前三個元素，回傳 True
    return False  # 如果沒有找到重複的前三個元素，回傳 False

# 使用列表解析建立一個不包含重複前三個元素的新陣列 result
result = [arr for arr in lineTable if not has_duplicate_first_three(arr, lineTable)]

print(result)

# -----------------------------------------------------------------以下為索引編號

# target_line = [1, 2, 1, 2, 1] # 輸入索引的賠付線 EX:[1, 2, 1, 2, 1]
def findLine():
    index = None  # 存放結果的欄位
    for x in result:
        target_line = x
        for i, line in enumerate(lineTable):
            if line == target_line:
                index = i + 1  
                break
    
        if index is not None:
            print(f"第{index}線.")
        else:
            print("找不到")
        
# -----------------------------------------------------------------
def addscript(script):
    for x in result:
        for y in range(5):
            script[y]=script[y]+x[y]
        print(script)

# findLine()
addscript([1,1,1,1,1])