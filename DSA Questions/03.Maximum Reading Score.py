def get_max_score(books:list[tuple[str,int]])->int:
    #define empty dict
    category_max = {}

    for category,score in books:
        if category not in category_max:
            category_max[category] = score
        else:
            category_max[category] = max(category_max[category],score)    

    sum_score = sorted(category_max.values(),reverse=True)
   # sum=0
    # for num in sum_score:
    #     sum += num
    return sum(sum_score[0:3])



books = [("Adventure", 4), ("History", 3), ("Reference", 1), ("Fiction", 2)]
print(get_max_score(books))
