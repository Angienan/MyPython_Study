#为函数添加类型注解
def calc(scores: list[int]) -> float:
    return sum(scores)/len(scores)

def calc_data(scores: list[int]) -> tuple[int,int,float ]:
    max_v = max(scores)
    min_v = min(scores)
    avg_v = sum(scores)/len(scores)
    return max_v, min_v, avg_v

#在函数中类型推断依旧可用