data = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 70000},
    {"name": "C", "salary": 50000}
]

# def highest_salary(data):
#     maxSal=0
#     name = ''

#     for x in data:
#         if x["salary"] > maxSal:
#             maxSal = x["salary"]
#             name = x['name']

#     return name,maxSal        
        
# print(highest_salary(data))      

def highest_salary(data):
    results={}

    for x in data:
        sal = x['salary']
        if sal not in results:
            results[sal] = []

        results[sal].append(x['name'])    
    return results        
        
print(highest_salary(data))     