#1 
# nums = [1,2,3,4,5,6,7]
# k = 3
# print(nums[-k:] + nums[:len(nums) - k])

#2
# newlist = []
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# for i in nums1:
#     if i in nums2:
#         if i not in newlist:
#             newlist.append(i)
# print(newlist)

#3
# nums = [1,2,3,4]
# newlist = []
# s = 0
# for i in nums:
#     s+= i
#     newlist.append(s)
# print(newlist)


#4
# def isValid(s):
#     for i in range(len(s)//2):
#         s = s.replace('()', '')
#         s = s.replace('[]', '')
#         s = s.replace('{}', '')
#     return len(s) == 0
# print(isValid('{[()]}'))
