"""
name: 2409_统计共同的日子数.py
create_time: 2025/6/11 22:29
author: Ethan

Description: https://leetcode.cn/problems/count-days-spent-together/description/
"""


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 先计算谁在前，交叉的天数等于先结束的那个人的结尾，减去后开始的那个人的开头
        # 比较日期
        def date_gt(str1: str, str2: str) -> bool:
            month1, day1 = str1.split('-')
            month2, day2 = str2.split('-')
            if int(month1) < int(month2):
                return False
            elif int(month1) > int(month2):
                return True
            elif int(day1) < int(day2):
                return False
            else:
                return True
        def diff_date(str1: str, str2: str) -> int:
            month1, day1 = str1.split('-')
            month2, day2 = str2.split('-')
            if month1 < month2:
                return 0
            month2 = int(month2)
            diff_days = int(day1) - int(day2)
            diff_month = int(month1) - month2
            diff_month_days = sum(month_days[month2 - 1: month2 + diff_month - 1])
            res = diff_month_days + diff_days + 1
            if res < 0:
                res = 0
            return res

        date1 = leaveAlice  # 先结束的结尾
        date2 = arriveBob  # 后开始的开头
        if date_gt(leaveAlice, leaveBob):
            date1 = leaveBob
        if date_gt(arriveAlice, arriveBob):
            date2 = arriveAlice

        return diff_date(date1, date2)


arriveAlice = "10-20"
leaveAlice = "12-22"
arriveBob = "06-21"
leaveBob = "07-05"

print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
