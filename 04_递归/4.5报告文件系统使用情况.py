"""
name: 4.5报告文件系统使用情况
create_time: 2025/2/11 11:33
author: Ethan

Description: 
"""
import os


def disk_usage(path):
    """
    报告文件系统使用情况
    :param path:
    :return:
    """
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print(f"{0:<7}{total:<7,} {path}")
    return total
