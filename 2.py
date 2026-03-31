words = ["apple", "banana", "apple", "orange", "banana"]
# {'apple': 2, 'banana': 2, 'orange': 1}
def countFruits(words):
    results = {}

    for i in words:
        if i not in results:
            results[i] = 1
        else:
            results[i] += 1    

    return results

print(countFruits(words))
        