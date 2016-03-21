from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    script = open(fname)
    instr = script.read().split('\n')
    i = 0
    while i < len(instr):
        if instr[i] == "line":
            i += 1
            values = instr[i].split(' ')
            add_edge( points, int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5])) 
            i += 1
        elif instr[i] == "circle":
            i += 1
            values = instr[i].split(' ')
            add_circle( points, int(values[0]), int(values[1]), 0, int(values[2]), float(1/50)) 
            i += 1
        elif instr[i] == "hermite":
            pass #welp.
        elif instr[i] == "b":
            pass #welp.
        elif instr[i] == "ident":
            transform = new_matrix(4, 4)
            ident(transform)
            i += 1
        elif instr[i] == "scale":
            i += 1
            values = instr[i].split(' ')
            scale = make_scale( float(values[0]), float(values[1]), float(values[2]))
            matrix_mult(scale, transform)
            i += 1
        elif instr[i] == "translate":
            i += 1
            values = instr[i].split(' ')
            translate = make_translate( int(values[0]), int(values[1]), int(values[2]))
            matrix_mult(translate, transform)
            i += 1
        elif instr[i] == "xrotate":
            i += 1
            rotX = make_rotX(int(instr[i]))
            matrix_mult(rotX, transform)
            i += 1
        elif instr[i] == "yrotate":
            i += 1
            rotY = make_rotY(int(instr[i]))
            matrix_mult(rotY, transform)
            i += 1
        elif instr[i] == "zrotate":
            i += 1
            rotZ = make_rotZ(int(instr[i]))
            matrix_mult(rotZ, transform)
            i += 1
        elif instr[i] == "apply":
            matrix_mult(transform, points)
            i += 1
        elif instr[i] == "display":
            draw_lines(points, screen, [255, 255, 255])
            #display(screen)
            i += 1
        elif instr[i] == "save":
            draw_lines(points, screen, [255, 255, 255])
            i += 1
            save_ppm(screen, instr[i])
            i += 1

		