"""
name: 657_机器人能否回到原点
create_time: 2023/9/14 22:45
author: Ethan

Description: 在二维平面上，有一个机器人从原点 (0, 0) 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 (0, 0) 处结束。

移动顺序由字符串 moves 表示。字符 move[i] 表示其第 i 次移动。机器人的有效动作有 R（右），L（左），U（上）和 D（下）。

如果机器人在完成所有动作后返回原点，则返回 true。否则，返回 false。

注意：机器人“面朝”的方向无关紧要。 “R” 将始终使机器人向右移动一次，“L” 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        move_dic = {}
        for move in moves:
            if move_dic.get(move):
                move_dic[move] += 1
            else:
                move_dic[move] = 1

        return move_dic.get('U') == move_dic.get('D') and move_dic.get('L') == move_dic.get('R')


    def judgeCircle1(self, moves: str) -> bool:
        """
        对于一般长度的字符串，这种方法足够快速，不过如果数字过大的话，它比较低效，因为他将执行 两次循环
        :param moves:
        :return:
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')

