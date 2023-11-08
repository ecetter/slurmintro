
import sys

def generate_fibonacci_triangle( n ):
    triangle = [ ]
    a, b = 0, 1
    
    for i in range( n ):
        row = [ ]
        for j in range( i + 1 ):
            row.append( a )
            a, b = b, a + b
        triangle.append( row )
            
    return triangle


def print_fibonacci_triangle( triangle ):
    for row in triangle:
        print( " ".join( map( str, row ) ) )
        print( "\n- - - - - - - - - - \n" )

if __name__ == "__main__":
    if len( sys.argv ) != 2:
        print( "Usage: python fibonacci_triangle.py <number_of_rows>" )
    else:
        try:
            n = int( sys.argv[1] )
            if n < 0:
                print("Please enter a non-negative integer.")
            else:
                fibonacci_triangle = generate_fibonacci_triangle( n )
                print(" \nFibonacci Triangle:" )
                print_fibonacci_triangle( fibonacci_triangle )
        except ValueError:
            print( "Invalid input. Please enter a valid integer." )
