# ###By considering the terms in the Fibonacci sequence 
# # whose values do not exceed four million, 
# # find the sum of the even-valued terms.

# #sequence <= 4000000
# #take the even terms qin the sequemce and sum them 

# sequence = []

# sequence.append(1)
# sequence.append(2)
# def cal_next_num():
#     last_index = len(sequence) - 1
#     prev_index = len(sequence) - 2
#     next_num = sequence[last_index] + sequence[prev_index]
#     return next_num

# while True:
#     next_num = cal_next_num()   
#     if next_num > 4000001:
#         break
#     sequence.append(cal_next_num())

# print(sequence)

# # sum of even 
# even_num = []
# for num in sequence:
#     if num % 2 == 0:
#         even_num.append(num)
# even_sum = sum(even_num)
# print(even_sum)###By considering the terms in the Fibonacci sequence 
# # whose values do not exceed four million, 
# # find the sum of the even-valued terms.

# #sequence <= 4000000
# #take the even terms qin the sequemce and sum them 

sequence = []

sequence.append(1)
sequence.append(2)
def cal_next_num():
     last_index = len(sequence) - 1
     prev_index = len(sequence) - 2
     next_num = sequence[last_index] + sequence[prev_index]
     return next_num

while True:
     next_num = cal_next_num()   
     if next_num > 4000001:
         break
     sequence.append(cal_next_num())

print(sequence)

# # sum of even 
even_num = []
for num in sequence:
     if num % 2 == 0:
         even_num.append(num)
     even_sum = sum(even_num)
print(even_sum)



# ##values should be less than 400001