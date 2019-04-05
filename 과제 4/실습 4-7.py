# def merge(left,right):
#     if not (left == [] or right == []):
#         if left[0] <= right[0]:
#             return [left[0]] + merge(left[1:],right)
#         else:
#             return [right[0]] + merge(left,right[1:])
#     else:
#         return left + right


def merge(left,right):
    def loop(left,right,ss):
        if not (left == [] or right == []):
            if left[0] <= right[0]:
                ss.append(left[0])
                print(ss)
                return loop(left[1:], right, ss)
            else:
                ss.append(right[0])
                print(ss)
                return loop(left, right[1:], ss)
        else:
            if (left == []):
                return ss + sorted(right)
            elif (right == []):
                return ss + sorted(left)
    return loop(left,right,[])

print(merge([18,23,32],[7,11,55,99]))
print(merge([1,3], [14,9,8,7]))
