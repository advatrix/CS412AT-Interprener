from __future__ import annotations
import os.path
import sys
import interpreter
import json_convert


def execute(program_file: str, map_file: str, argv: str, output_file: str):
    if os.path.isfile(program_file) and os.path.isfile(map_file):
        map_dict, robot = json_convert.convert(map_file)
        with open(program_file, 'r') as pr_f:
            program = pr_f.read()
        intr = interpreter.Interpreter()
        intr.interpret(program, map_dict, robot, robot_mode=True, argv=argv.split())
        with open(output_file, 'w') as o:
            o.write('Global program variables:\n')
            o.write(str(intr.sym_table[0]))
            o.write('\n\nErrors:\n')
            for error in intr.errors:
                o.write(error)
                o.write('\n')
            o.write('\n\n')
            o.write(str(intr.map))
            o.write('\n\n')
            o.write(str(intr.robot))

    else:
        sys.stderr.write('Invalid file names\n')


if __name__ == '__main__':
    sys.stdout.write('Program path: ')
    prog = 'pathfinding.txt'
    sys.stdout.write('Data path: ')
    data = 'map.json'
    sys.stdout.write('Argv: ')
    argv = '1'
    sys.stdout.write('Output path: ')
    out = 'output.txt'
    sys.stdout.write('\n')
    execute(prog, data, argv, out)