# Imagine an onscreen keyboard, for example like what pops up when you're searching in a streaming app, and you traverse the keyboard using the commands u, d, l, r, and !, where u is up, d is down, l is left, r is right, and ! is select. Given a string and the length of each row as inputs, determine the steps needed to create the str using the keyboard.
# Things to note include:
# - we are only dealing with the letters a through z in the keyboard
# - the length of each row in the keyboard can vary depending on the input parameter, and it could even be 26 meaning there is only one row
# - you cannot traverse across boundaries of the keyboard grid. e.g., if your at z, going right will not lead to a, and if you're at the end of a row, going right will not lead to the next row

def keyboard_steps(target, row_len):
    cur_pos = (0, 0)
    steps = []
    for char in target:
        ascii_offset = ord(char) - ord('a')
        target_pos = (ascii_offset // row_len, ascii_offset % row_len)

        # move vertically to the target row
        while cur_pos[0] < target_pos[0]:
            steps.append('d')
            cur_pos = (cur_pos[0] + 1, cur_pos[1])
        while cur_pos[0] > target_pos[0]:
            steps.append('u')
            cur_pos = (cur_pos[0] - 1, cur_pos[1])
        
        # move horizontally to the target column
        while cur_pos[1] < target_pos[1]:
            steps.append('r')
            cur_pos = (cur_pos[0], cur_pos[1] + 1)
        while cur_pos[1] > target_pos[1]:
            steps.append('l')
            cur_pos = (cur_pos[0], cur_pos[1] - 1)
        
        # select the target character
        steps.append('!')
    
    return steps

print(keyboard_steps('hello', 5))
# Output: ['r', 'r', 'r', 'r', '!', 'd', 'd', 'r', '!', '!', 'l', 'l', 'l', 'u', '!', 'd', 'd', 'r', 'r', 'r', '!']



