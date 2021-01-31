# for
# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))

# hero = ['아이언맨', '토르', '헐크']
# for item in hero:
#     print(item)

# while
# custmer = "토르"
# index = 5
# while index >= 1:
#     print("커피 나왔어요")
#     index -= 1
#     if index == 0:
#         print("끝")

# continue, break
# absent = [2, 5] # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("{0}번, 너 당장 교무실로 따라와".format(student))
#         break
#     print("{0}번, 책 읽어".format(student))

# 한 줄 for
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# # 이름을 길이로 반환
# students = ['iron man', 'thor', 'groot']
# students = [len(i) for i in students]
# print(students)