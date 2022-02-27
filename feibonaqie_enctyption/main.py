# ==================
# created: 2022/02/27
# author: Lily
# ==================
"""
题目:
使用斐波那契加密方法给以下特定的信息编码加密。

斐波那契数列的前两项可以是任意的两个非负整数，且后面每一项都是前两项之和。即如果数列的最前面的两项为 3 和 7，则该数列是 3, 7, 10, 17, 27, ... 斐波那契加密方法使用这些数字和一个输入“密钥” (字母表中的一个小写字母)将一条信息编码成一串数字。其他人可通过已使用的“密钥”和数列的前两项，来破译这条信息。对于信息中的每个字符，都可以根据以下步骤生成对应的整数：

找出与该字符具有相同索引的斐波那契数（如使用上述数列，第一个字符用数字 3 来表示，第五个字符用数字 27 来表示。）

根据输入的密钥，找出对步骤 1 中斐波那契数进行偏移操作的新字母，如果新字母为z，则下一个字母从a重新开始。
通过将字符串中的字符的 ASCII 码与步骤 2 中该字母的 ASCII 码的 3 倍相加，即可以找出编码信息中每个字符的加密数字。
为了保证斐波那契数不会变得太大，每条信息第 21 个字符只能再次使用第一个斐波那契数，第 41 个字符同样如此。每一个斐波那契数列都为20项。我们保证每条信息的长度不超过 100 个字符。

示例：对于字符串 “ACSL c2”，斐波那契数列的前两项为 3 和 7，字母 ‘h’ 为“密钥”，编码数字可以通过以下方式获得：

                                                                              

输入：共有5 组数据，每组包含 4 部分信息：1&2) 斐波那契数列中起始的两个非负整数，3) “密钥”，即一个小写字母，4) 一条需要编码的字符串信息。除双引号外，键盘上的任意字符都可能在信息中出现。

输出：每行数据都输出整数，每个整数之间由空格隔开，表示编码后的信息。
"""

ASCII_a = ord('a')
ASCII_z = ord('z')
ALPHABET_CODE = list(range(ASCII_a, ASCII_z + 1))
LEN_ALPHABET = len(ALPHABET_CODE)
MAX_TURN = 20

# print('ASCII_a: ', ASCII_a)
# print('ASCII_z: ', ASCII_z)
# print('ALPHABET_CODE: ', ALPHABET_CODE)
# print('LEN_ALPHABET: ', LEN_ALPHABET)
# print('MAX_TURN: ', MAX_TURN)

def feibonaqie_list(length, first, second):
    ''' 返回一个斐波那契数列的列表
    :param length: 提供数列的长度
    :param first: 提供数列中的第一个数字
    :param second: 提供数列中的第二个数字
    :return list:
    '''
    l = [first, second]
    for _ in range(0, length - 2):
        l.append(l[-1] + l[-2])
    return l


def get_offset(fabo_list, index, key_code):
    ''' 返回偏移后的密钥ASCII编码
    :param fabo_list: 提供斐波那契数列列表
    :param index: 提供每个需加密字符在列表中的索引
    :param key_code: 密钥的ASCII编码
    '''
    # 计算以20为反转长度的字符串中每个字符的当前索引
    index = index - int(index / MAX_TURN) * MAX_TURN
    # 计算每个偏移后的安全密钥的ASCII编码
    offset_code = fabo_list[index] + key_code
    # 计算超过范围的密钥在回转后对应的密钥ASCII编码
    if offset_code > ASCII_z:
        walk_index = offset_code - ASCII_a
        offset_code = walk_index - int(walk_index / LEN_ALPHABET) * LEN_ALPHABET + ASCII_a
    return offset_code

def get_result(first, second, key_code, string_needed):
    ''' 返回加密后的字符串编码
    :param first: 提供数列中的第一个数字
    :param second: 提供数列中的第二个数字
    :param key_code: 密钥的ASCII编码
    :param sstring_needed: 需要加密的字符串
    '''
    encryption_number = []
    string_needed = list(string_needed)
    # 创建斐波那契数列
    feibonaqi = feibonaqie_list(MAX_TURN, first, second)
    for i in range(len(string_needed)):
        # 计算每次密钥的编码
        offset = get_offset(feibonaqi, i, key_code)
        # print('offset: ', offset)
        # 计算加密后的字符串编码
        encryption_number.append(ord(string_needed[i]) + 3 * offset)
    return encryption_number

# print(get_result(3, 7, ord('h'), 'ACSL c2'))

test_parameters = (
    (3, 7, 'h', 'ACSL c2'),
    (4, 9, 's', 'Python Programming is easier than programming in Java.'),
    (2, 5, 'a', 'Fibonacci Numbers are found in many places including the Mandelbrot Set.'),
    (0, 1, 'j', 'Help ME figure out how to solve this problem!'),
    (4, 8, 'z', 'It is 9:30 in the morning EST, but 6:30 on the West Coast.'),
)

for i in test_parameters:
    first = i[0]
    second = i[1]
    keycode = i[2]
    string = i[3]
    print(get_result(first, second, ord(keycode), string))