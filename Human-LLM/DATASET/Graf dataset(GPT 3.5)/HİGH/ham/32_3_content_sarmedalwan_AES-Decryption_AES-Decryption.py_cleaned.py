import sys
b1 = \
[132, 201, 141, 74, 140, 94, 141, 140, 141, 15, 31, 164, 90, 229, 201, 141, 78,
114, 241, 217, 141, 217, 140, 180, 141, 164, 51, 141, 188, 221, 31, 164, 241,
177, 141, 140, 51, 217, 141, 201, 229, 152, 141, 78, 241, 114, 78, 102, 94,
141, 74, 152, 31, 152, 141, 94, 201, 31, 164, 102, 164, 51, 90, 141, 201, 229,
164, 31, 201, 152, 152, 51, 115]
a1 = 84
def fonk1( int_list, int_key ):
    b2 = bytearray( int_list )
    b3 = fonk2( b2 )
    b4 = fonk3( int_key )
    b5 = []
    for nibbles in b3:
        b5 +=  \
        [ fonk6( nibbles, b4 ) ]
    b6 = \
    fonk4( b5 )
    b7 = fonk11( b6 )
    return b7
def fonk2( a_bytearray ):
    b8 = []
    for b15 in a_bytearray:
        b9 = fonk3( b15 )
        b8 += [ b9 ]
    return b8
def fonk3( b15 ):
    b10 = b15 & 0b00000011
    b11 = ( b15 >> 2 ) & 0b00000011
    b12 = ( b15 >> 4 ) & 0b00000011
    b13 = ( b15 >> 6 ) & 0b00000011
    return( bytearray( [ b13, b12, b11, b10 ] ) )
def fonk4( bytes_as_nibbles ):
    b14 = []
    for nibble_quad in bytes_as_nibbles:
        b14 += [ fonk5( nibble_quad ) ]
    return b14
def fonk5( quadruple_bytearray ):
    b15 = \
    ( quadruple_bytearray[ 0 ] << 6 ) | \
    ( quadruple_bytearray[ 1 ] << 4 ) | \
    ( quadruple_bytearray[ 2 ] << 2 ) | \
    ( quadruple_bytearray[ 3 ] )
    return b15
def fonk6( nibble_quadruple, key_quadruple ):
    b16 = fonk7(nibble_quadruple, key_quadruple)
    b16 = fonk8(b16)
    b16 = fonk9(b16)
    b16 = fonk7(b16, key_quadruple)
    b16 = fonk10(b16)
    b16 = fonk8(b16)
    b16 = fonk9(b16)
    b16 = fonk7(b16, key_quadruple)
    return b16
def fonk7( nibbles, a1 ):
    b16 = nibbles[:]
    for i in range(4):
        b16[i] ^= a1[i]
    return b16
def fonk8( nibbles ):
    b16 = nibbles[:]
    b17 = b16[-2]
    b16[-2]=b16[-1]
    b16[-1]=b17
    return b16
def fonk9( nibbles ):
    b16 = nibbles[:]
    for i in range(4):
        if b16[i] == 0:
            b16[i] = 2
        elif b16[i] == 1:
            b16[i] = 0
        elif b16[i] == 2:
            b16[i] = 3
        elif b16[i] == 3:
            b16[i] = 1
    return b16
def fonk10( nibbles ):
    b16 = nibbles[:]
    b16[0] = (b16[0]-b16[2])%4
    b16[1] = (b16[1]-b16[3])%4
    return b16
def fonk11( b14 ):
   b16 = ''
   for b15 in b14:
       b16 += chr( b15 )
   return b16
if b18 = = '__main__':
    if len( sys.argv ) < 2:
        print( "Must have another command-line argument" )
    elif sys.argv[ 1 ] == 'a':
        print( "dec_decrypt:" )
        print( fonk1( b1, a1 ) )
    elif sys.argv[ 1 ] == 'b':
        b16 = \
        fonk7( fonk3( 0b10101010 ),\
                 fonk3( 0b10001000 ) )
        b19 = fonk5( b16 )
        print( "dec_xor \n10101010 with \n10001000:\n" )
        print( format( b19, '08b' ) )
    elif sys.argv[ 1 ] == 'c':
        b16 = \
        fonk8( fonk3( 0b10001000 ) )
        b19 = fonk5( b16 )
        print( "dec_swap_last_two of \n10001000:\n" )
        print( format( b19, '08b' ) )
    elif sys.argv[ 1 ] == 'd':
        b16 = \
        fonk9( fonk3( 0b00011011 ) )
        b19 = fonk5( b16 )
        print( "dec_s_box of \n00011011:\n" )
        print( format( b19, '08b' ) )
    elif sys.argv[ 1 ] == 'e':
        b16 = \
        fonk10( fonk3( 0b00011011 ) )
        b19 = fonk5( b16 )
        print( "dec_subtract_last_two_first_two of \n00011011:\n" )
        print( format( b19, '08b' ) )
    else:
        print( 'Bad argument' )