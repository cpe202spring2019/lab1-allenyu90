
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""

   num = 0
   if int_list is None:
      raise ValueError
   elif int_list == []:
      return None
   elif len(int_list) == 1:
      return int_list[0]
   else:
      for i in int_list:
         if i > num:
            num = i
   return num

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""

   if int_list is None:
      raise ValueError
   elif int_list == []:
      return int_list
   elif len(int_list) == 1:
      return int_list
   else:
      reverse = reverse_rec(int_list[1:])
      reverse.append(int_list[0])
   return reverse

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   mid = (low + high) // 2
   if int_list is None:
      raise ValueError
   elif int_list == []:
      return None
   if high < low:
      return None
   if int_list[mid] == target:
      return mid
   elif int_list[mid] > target:
      return bin_search(target, low, high - 1, int_list)
   elif int_list[mid] < target:
      return bin_search(target, low + 1, high, int_list)
   

