# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.
#
# move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

def move_zeros(lst):
   zrl = [n for n in lst if n == 0]
   lst = list(filter(lambda val: val != 0, lst))
   lst.extend(zrl)
   return lst



print(move_zeros([1, 0, 1, 2, 0, 1, 3]))