#!/usr/bin/python
# Written by Cameron "Camdar" Wong

import sys, random

DIRS = {
    '>': lambda x, y: (x + 1, y),
    '<': lambda x, y: (x - 1, y),
    '^': lambda x, y: (x, y - 1),
    'v': lambda x, y: (x, y + 1)
}

INSTRUCTIONS = {}

class inst_wrapper:
    __slots__ = ['char']
    def __init__(self, char):
        self.char = char
    def __call__(self, func):
        INSTRUCTIONS[self.char] = func
        return func


def safe_pop(stack):
    if stack:
        return stack.pop()
    stack.append(0)
    return 0


@inst_wrapper('+')
def befunge_add(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(a + b)

@inst_wrapper('-')
def befunge_sub(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(a - b)

@inst_wrapper('*')
def befunge_mul(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(a * b)

@inst_wrapper('/')
def befunge_div(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    if b == 0:
        print("Interpreter: Error: Dividing by 0!")
        exit()
    stack.append(a // b)

@inst_wrapper('%')
def befunge_mod(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(0 if b == 0 else a % b)

@inst_wrapper('!')
def befunge_not(stack):
    stack.append(int(not safe_pop(stack)))

@inst_wrapper('`')
def befunge_gt(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(int(a > b))

@inst_wrapper(':')
def befunge_dup(stack):
    v = safe_pop(stack)
    stack.append(v)
    stack.append(v)

@inst_wrapper('\\')
def befunge_swap(stack):
    b, a = safe_pop(stack), safe_pop(stack)
    stack.append(b)
    stack.append(a)

@inst_wrapper('$')
def befunge_discard(stack):
    safe_pop(stack)

@inst_wrapper('.')
def befunge_num_out(stack):
    print(safe_pop(stack), end='')

@inst_wrapper(',')
def befunge_str_out(stack):
    print(chr(safe_pop(stack)), end='')

@inst_wrapper('&')
def befunge_num_in(stack):
    try:
        stack.append(int(input()))
    except ValueError:
        print("Invalid integer! Pushing 0!")
        stack.append(0)

@inst_wrapper('~')
def befunge_str_in(stack):
    stack.append(ord(input()[0]))


class prog_state:
    __slots__ = (
        'grid', 'dir', 'coords', 'stack',
        'active', 'jump', 'width', 'height',
        'strmode'
    )

    def __init__(self, prog):
        self.grid = prog
        self.height = len(prog)
        self.width = len(prog[0])
        self.coords = (0, 0)
        self.dir = DIRS['>']
        self.stack = []
        self.active = True
        self.jump = False
        self.strmode = False

    def handle_next(self):
        x = self.coords[0] % self.width
        y = self.coords[1] % self.height
        inst = self.grid[y][x]

        # String mode
        if self.strmode:
            if inst == '"':
                self.strmode = False
            else:
                self.stack.append(ord(inst))
            return

        # p / g
        if inst == 'p':
            v = safe_pop(self.stack)
            x = safe_pop(self.stack) % self.width
            y = safe_pop(self.stack) % self.height
            self.grid[y][x] = chr(v % 1048576)
            return

        if inst == 'g':
            x = safe_pop(self.stack) % self.width
            y = safe_pop(self.stack) % self.height
            self.stack.append(ord(self.grid[y][x]))
            return

        # Specials
        if inst == '@':
            self.active = False
            return

        if inst == '#':
            self.jump = True
            return

        if inst == '|':
            inst = 'v^'[bool(safe_pop(self.stack))]

        if inst == '_':
            inst = '><'[bool(safe_pop(self.stack))]

        if inst == '?':
            inst = random.choice('><^v')

        if inst == '"':
            self.strmode = True
            return

        # Numbers
        if inst.isdigit():
            self.stack.append(int(inst))
            return

        # Directions
        if inst in DIRS:
            self.dir = DIRS[inst]
            return

        # Normal instructions
        if inst in INSTRUCTIONS:
            INSTRUCTIONS[inst](self.stack)

    def step(self):
        x, y = self.dir(*self.coords)
        self.coords = (x % self.width, y % self.height)

        if self.jump:
            self.jump = False
            x, y = self.dir(*self.coords)
            self.coords = (x % self.width, y % self.height)


def main():
    if len(sys.argv) != 2:
        print('usage: befunge_interpreter.py file.bf')
        return

    with open(sys.argv[1]) as f:
        prog = [list(line.rstrip('\n')) for line in f]

    width = max(len(line) for line in prog)
    for line in prog:
        line.extend([' '] * (width - len(line)))

    state = prog_state(prog)

    while state.active:
        state.handle_next()
        state.step()

    print('\nProgram terminated.')


if __name__ == '__main__':
    main()
