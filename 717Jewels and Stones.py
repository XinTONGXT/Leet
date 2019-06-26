# -*- coding:utf8 -*-
# @Project : Leetcode
# @File    : 717Jewels and Stones.py
# @Author  : Xin 
# @Time    : 2019/6/17 16:16


"""
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.
Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3

Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
"""


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        if len(J)>50 or len(S)>50:
            if len(J)-50>0:
                print('string J is too long, please give a short one, at most 50, already more then {} letters!'
                  .format(len(J)-50))
            elif len(S)-50>0:
                print('string J is too long, please give a short one, at most 50, already more then {} letters!'
                  .format(len(S) - 50))
        else:
            output = 0

            for letter in S:
                if letter in J:
                    output += 1

            print('the number of Jewels in Stones is: {}'.format(output))
            return output