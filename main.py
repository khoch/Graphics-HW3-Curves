from display import *
from draw import *
from iparser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script_nocurves', edges, transform, screen, color )
