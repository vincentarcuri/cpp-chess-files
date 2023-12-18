import os


path = "/home/vinarc/Code/agent_chessv2/cpp_chess"
os.chdir(path)

FILES = [
    'Pieces2',
    'Board2',
    'Game',
    'search',
    'clib',
    #'tests'
]

# Compile files separately
# for file in FILES:
#     os.system(f"gcc {file}.cpp -o {file}.o -std=c++20 -lstdc++ -c")

# Compile one executable together
os.system(f"gcc -o clib {'.cpp '.join(FILES)}.cpp -g -std=c++20 -lstdc++")

#os.system("./chess")