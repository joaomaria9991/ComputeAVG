def get_grades_from_file(file_path):
    grades = []
    with open(file_path, 'r',encoding='utf-8') as file:
        for line in file:
            line = line.strip().split()
            if line:
                grade = line[-1].strip()
                grades.append(int(grade))
    return grades

def generate_array(size):
    arr = [1] * (size - 2)  
    arr.extend([2, 8])  
    return arr


def elementwise_multiply(arr1, arr2):
    result = [x * y for x, y in zip(arr1, arr2)]
    return result


def calculate_average(arr):
    total = sum(arr)
    average = total / 42
    return average


file_path = 'notas.txt' 
result = get_grades_from_file(file_path)

size = len(result)
w = generate_array(size)


med_weighted=elementwise_multiply(result,w)
med_final=calculate_average(med_weighted)
print("Certifica-te que a notas das cadeiras que valem mais que  ETCS estão em ultimo e que os valores estão ajustados na função generate_array")
print("Caso contrário dá merda")
print(med_final)