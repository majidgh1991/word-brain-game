__author__ = 'majid'
from itertools import permutations
from StringIO import StringIO
from copy import deepcopy
import cProfile
import re

def get_char(pattern, n, i, j):
    return pattern[i*n+j]


def collapse(pattern, n):
    # pattern = list(pattern)
    for i in range(n):
        for j in range(n):
            if pattern[i*n+j] == ' ':
                for ii in reversed(range(0, i)):
                    pattern[(ii+1)*n + j] = pattern[ii*n + j]
                pattern[j] = ' '

    return pattern

def print_board(pattern, n):
    io = StringIO()
    for i in range(len(pattern)):
        if i!=0 and i%n == 0:
            io.write('\n')
        io.write(pattern[i] + ',')
    print io.getvalue()

def get_surroundings(pattern, n, i, j):
    chars = []
    indexes = []
    if i < n-1:
        indexes.append((i + 1, j))
        chars.append(pattern[(i+1)*n + j])
        if j > 0:
            indexes.append((i+1, j-1))
            chars.append(pattern[(i+1)*n + j-1])
        if j < n-1:
            indexes.append((i+1, j+1))
            chars.append(pattern[(i+1)*n + j+1])
    if i > 0:
        indexes.append((i - 1, j))
        chars.append(pattern[(i-1)*n + j])
        if j > 0:
            indexes.append((i-1 , j-1))
            chars.append(pattern[(i-1)*n + j-1])
        if j < n-1:
            indexes.append((i-1, j+1))
            chars.append(pattern[(i-1)*n + j+1])
    if j > 0:
        indexes.append((i, j-1))
        chars.append(pattern[(i)*n + j-1])
    if j < n-1:
        indexes.append((i, j+1))
        chars.append(pattern[(i)*n + j+1])
    return chars, indexes

def if_valid_temp(string, pattern, n, i, j, used):
    if len(string) == 0:
        return True, [[]]
    chars, indexes = get_surroundings(pattern, n, i, j)
    validity = []
    possible_inds = []
    for char, index in zip(chars, indexes):
        if index in used:
            continue
        if char == string[0]:
            val, inds = if_valid_temp(string[1:], pattern, n, index[0], index[1], used+[index])
            if val:
                validity.append(val)
                possible_inds += [x + [index] for x in inds]
    return len(validity)>0, possible_inds

def if_valid(string, pattern, n):
    if len(string) == 0:
        return True
    letter = string[0]
    validity = []
    possible_inds = []
    for index in [x[0] for x in enumerate(pattern) if x[1] == letter]:
        # index = m.start()
        i = int(index/n)
        j = index%n
        val, inds = if_valid_temp(string[1:], pattern, n, i, j, [(i,j)])
        if val:
            validity.append(val)
            possible_inds += [x + [(i,j)] for x in inds]
    return len(validity)>0,possible_inds


def find_word(letters, ws, res):
    if len(ws) == 0:
        print res
        return
    if ws[0] not in words:
        return
    for p in words[ws[0]]:
        val, inds = if_valid(p, letters, 4)

        if val:
            for xx in inds:
                new_board = deepcopy(letters)
                for ii in xx:
                    new_board[ii[0]*4+ii[1]] = ' '
                new_board = collapse(new_board, 4)
                find_word(new_board, ws[1:], res+[p])


words_temp = set([x.strip().lower() for x in open('words.txt')])
words = dict()
for word in words_temp:
    l = len(word)
    if l not in words:
        words[l] = set()
    words[l].add(word)

while True:
    args = raw_input('Enter your input:')
    ws = []
    try:
        args = args.split(',')
        letters = args[0]
        for xx in args[1:]:
            ws.append(int(xx))
    except:
        print 'exception'
        continue
    if letters == 'END':
        break

    print(len(letters))
    if len(letters) != 16:
        print 'here!'
        continue
    letters = list(letters)
    print_board(letters, 4)
    find_word(letters, ws, [])

