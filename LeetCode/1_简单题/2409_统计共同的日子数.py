"""
name: 2409_统计共同的日子数.py
create_time: 2025/6/11 22:29
author: Ethan

Description: https://leetcode.cn/problems/count-days-spent-together/description/
"""
from typing import List


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        datesOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        prefixSum = [0]
        for date in datesOfMonths:
            prefixSum.append(prefixSum[-1] + date)

        arriveAliceDay = self.calculateDayOfYear(arriveAlice, prefixSum)
        leaveAliceDay = self.calculateDayOfYear(leaveAlice, prefixSum)
        arriveBobDay = self.calculateDayOfYear(arriveBob, prefixSum)
        leaveBobDay = self.calculateDayOfYear(leaveBob, prefixSum)
        return max(0, min(leaveAliceDay, leaveBobDay) - max(arriveAliceDay, arriveBobDay) + 1)
    # 转换为一年当中的第几天更为简单
    def calculateDayOfYear(self, day: str, prefixSum: List[int]) -> int:
        month = int(day[:2])
        date = int(day[3:])
        return prefixSum[month - 1] + date


arriveAlice = "10-20"
leaveAlice = "12-22"
arriveBob = "06-21"
leaveBob = "07-05"

print(Solution().countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))
