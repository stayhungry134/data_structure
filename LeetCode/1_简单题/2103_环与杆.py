"""
name: 2103_环与杆
create_time: 2025/6/4 23:55
author: Ethan

Description: 
"""


class Solution:
    def countPoints(self, rings: str) -> int:
        tem_map = {}
        for i in range(len(rings) // 2):
            color_index = rings[i*2: i*2+2]
            color = color_index[0]
            _index = color_index[1]
            if not tem_map.get(_index):
                tem_map[_index] = [color]
            else:
                if color not in tem_map[_index]:
                    tem_map[_index].append(color)
        return len([key for key, value in tem_map.items() if len(value) == 3])

print(Solution().countPoints("B0B6G0R6R0R6G9"))