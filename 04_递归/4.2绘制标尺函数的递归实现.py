"""
name: 4.2绘制标尺函数的递归实现
create_time: 2025/2/11 10:32
author: Ethan

Description: 
"""


def draw_line(tick_length, tick_label=''):
    """
    绘制标尺函数的递归实现
    :param tick_length:
    :param tick_label:
    :return:
    """
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)


def draw_interval(center_length):
    """
    绘制间隔函数的递归实现
    :param center_length:
    :return:
    """
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(num_inches, major_length):
    """
    绘制标尺函数的递归实现
    :param num_inches:
    :param major_length:
    :return:
    """
    draw_line(major_length, '0')
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))
