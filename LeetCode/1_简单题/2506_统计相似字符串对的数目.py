"""
name: 2506_统计相似字符串对的数目.py
create_time: 2025/6/14 0:10
author: Ethan

Description: https://leetcode.cn/problems/count-pairs-of-similar-strings/description/
"""
from itertools import count
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # 需要注意的是set是无序的，所以需要对它进行排序
        tem_ls = [''.join(sorted(set(word))) for word in words]
        tem_map = {}
        res = 0
        for tem_set in tem_ls:
            if tem_set not in tem_map:
                tem_map[tem_set] = 0
            tem_map[tem_set] += 1
        for cnt in tem_map.values():
            # 这里需要注意的是，
            if cnt > 1:
                res += cnt * (cnt - 1) // 2
        return res
    # 可以使用frozenset
    def similarPairs1(self, words: List[str]) -> int:
        from collections import defaultdict
        n = len(words)
        res = 0
        dic = defaultdict(int)
        for word in words:
            key = ''.join(sorted(set(word)))
            res += dic[key]
            dic[key] += 1
        return res

words = ["zhdnqjzxyqpjiqvwrnuoabjrnhjaiijkqobibqwqrkqcucnsfe","ebypoudjghjqdajftomwkywegkdekwteapftaxrwxeznfmagmm","lurfmpwlkdbmglwpjaplwwtescdesicynqkqwjupuujzkesapz","hmwwgnctvjhaptvqivxrkvdfaoqjyznjolttgazfeyxsicwcmb","lrigpmlpdixbhbjneibdxijzpyyugfmdktmlvoctfeoaweamyn","kaeuuyymblsuyvsicdfauthdwqqihdjuarkidwzdpwbxxajdbg","mngezpncoomyiqyhztfhaijuhrdlianizzpbvcindyrwfzqvnk","prhcaxzpjwvdueoygkywqfsryvxzkgxnumxpenlrspxdmwnqyt","sezreoamsswjyzcaiirgyvxgvxngxrqvuvvheehxhbbnybcyny","fbvbxkovmwmwjtjgtqirwudyvvjefautpczrdlrclbixuccozo","ybvirklfjoekzgorplieylabgbgofuhubtvtjldxalvxxmalsw","uyrdbegalsqsjpssewkwziafrudinwbmgfdrfnnbbhskfjzjss","frmhuhgzzgyxdqefmhlporsijbdkcdhlydrdhgwkkqknwcskrm","lseltkspmmblhvtwlgxmouqxmpqmvsjasutsezocjoosiugznj","pjscihggxhereavrsqhraoprvzorrdprhlzktddmzezwrtcspu","vayjhuxszgdgikwxsldetyygracxekrydrzyosqeeeozsmrpzc","gxprhfzdgsoywbzoaunekxcowzgojjhiuvhtcuuciczlzhixiw","guidagwcywkpbmvdpeczgsejagheglqbwebzavvvcpiefkycdm","pjhehvajuieuovmtfemlrlrdssdjmtttwohsxjizluxymfktay","wffnlwkasfqaaohqvgaimhmzhpdvkptksyqezkbjqeacalrhgz","eicauvmhbzuurrkrgpeybcnavvxpfolumkvlmowicgfuulbuty","sihunfzfytveeiqyetplzjhypnrxczsejyzqaxnuzhurepocan","snuswczsdqfegfipxhhkvbyiiucmhuzbwrivlsmhzybbsqewuk","mzdsvqykkofgjhkddrpatweicfglsdqpcijkjosaltpybzwkuw","fmpiojraotpepeqqrjwstexeehrlmetmgndjnarscxymoipwdo","pxeecbmlggcnfynevzhuegsbftzaobbjfaawjfunmwfajdbrkw","kqdhfgkopchlybpbzllzqvxofraueqfstxgtrwgbwqfecvowqy","ussmspxjfoywtpudnrweewzsdeldzamadwrefxjgsulylewfji","knlhcggfstodwandgmpbiqxiqcngzpxikhncgrzumnpjbwcgdw","hqqrovqivnaranshdbfvrathzjkcwszrrqilrvsfhmwgnrmqbn","cuutcjswrwqqyouknpbzitygjekactwvftdpbnevyrcsizdwrh","ovcscvokvlwqtidcgojqdpmnceblwelozkikvajdczydefblfh","lqpgzgyyilgvatrdjwgheymgnqesfcolbplqkddyldvxjsgqql","wramyyybwswidprjcwqtcvfvhirxjqljteflaemmfscgrcpfkq","ouatwdpdgcgakwruotygizvzftnnsefbvrpzplrhqccjjghjkc","unqdeiweshjwffvgqskeozdffovxsezhbxwehprhwzdqhavsjo","bqfbmghcposkezenfslrondjptrnthvivxmoqmjuydwmoroyko","zmbxdjqxsspubqibiwumlbuikdajhdqzuqceaeyppnfzqnqmoh","umvxmxmjdlymqftqnemjrsbqkxoayvukhibfgxncotghvjlapy","iuesnjxnnesnzafzddxowkmhvpwuempvjgyqbjdwrlvxnhpujf","kbukztogkabwyfvnvfheogqpsilnxcgfjunoltopxyxhkfkomc","iwmjpkkmugejwcnkbgnzpwrudcbqaagdgbhnexoxuyruayfvno","ahjiviziaqcwfgkujaxwpsxahmmfvdjpmenyphwmaohmytbsoi"]

print(Solution().similarPairs(words))