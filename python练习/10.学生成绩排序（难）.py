students = [
    {'sno': 101, 'sname': '小张', 'sgrade': 88},
    {'sno': 102, 'sname': '小王', 'sgrade': 77},
    {'sno': 103, 'sname': '小李', 'sgrade': 99},
    {'sno': 104, 'sname': '小赵', 'sgrade': 66},
]

# 根据成绩升序（从小到大）
students_sort = sorted(students, key=lambda x: x["sgrade"])
# 根据成绩降序（从大到小）
# students_sort = sorted(students, key=lambda x: x["sgrade"], reverse=True)

print(f"原列表: {students}")
print(f"排序后列表: {students_sort}")