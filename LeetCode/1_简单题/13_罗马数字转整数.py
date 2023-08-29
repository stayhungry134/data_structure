"""
name: 13_罗马数字转整数
create_time: 2023/7/9 22:02
author: Ethan

Description: 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 1 。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/roman-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def roman_to_int(s: str) -> int:
    roman_dic = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    # 如果字符串在给定的字典中
    if roman_dic.get(s):
        return roman_dic.get(s)
    else:
        s_len = len(s)
        result = 0
        for i in range(s_len):
            tem_num = roman_dic.get(s[i])
            # 如果罗马数字比下一个罗马数字小，就表示减去
            if i < s_len - 1 and tem_num < roman_dic.get(s[i+1]):
                result -= tem_num
            else:
                result += tem_num
        return result


roman_s = "IX"
print(roman_to_int(roman_s))
