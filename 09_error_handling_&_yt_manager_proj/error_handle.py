file = open('youtube.txt', 'w')

try:
    file.write('chai aur code')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('chai aur python')


'''
File Modes:

'w' (Write): Creates a new file or overwrites an existing one.
'r' (Read): Opens a file for reading (default mode).

Why use with ??

It prevents memory leaks by guaranteeing the file closes.
It simplifies the syntax (no need to remember file.close()).
It handles exceptions gracefully without needing verbose error-handling code for simple tasks.
'''