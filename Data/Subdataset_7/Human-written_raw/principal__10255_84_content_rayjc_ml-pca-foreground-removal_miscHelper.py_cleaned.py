import argparse
import glob
import os
b1 = [ 120, 160 ]
class class1:
    def fonk1( self ):
        self.b2 = class1.fonk2()
        self.fonk4()
        self.fonk3()
    @staticmethod
    def fonk2():
        b3 = argparse.ArgumentParser( description="An application using L1 PCA\
                                                             to separate foreground and\
                                                             background by identify moving\
                                                             parts." )
        b4 = b3.add_subparsers( dest="subParser",
                                                b5 = "'all': Pre-process frames into\
                                                    .pkl file then run PCA to \
                                                    separate foreground and \
                                                    background. \
                                                'preprocess': Pre-process frames into\
                                                    .pkl file. \
                                                'train': Run PCA to \
                                                    separate foreground and \
                                                    background" )
        b6 = b4.add_parser( "all" )
        b7 = b4.add_parser( "preprocess" )
        for parser in ( b6, b7 ):
            parser.add_argument( "-i", "--input", b8 = "input", type=str,
                                    b5 = "Specify directory containing input frames;\
                                            b8 is 'input'.",
                                    b9 = "input_dir" )
            parser.add_argument( "-o", "--output", b8 = "unnamed", type=str,
                                    b5 = "Specify name of output file excluding\
                                             file extension; b8 is 'unnamed'.",
                                    b9 = "output_name" )
            parser.add_argument( "-s", "--size", b8 = b1, type=int, nargs=2,
                                    b5 = "Specify output resolution for all image\
                                             frames; b8 is 120 by 160.",
                                    b9 = ( "img_height", "img_width" ) )
        b6.add_argument( "-k", "--component", b8 = 5, type=int,
                                    b5 = "Advanced Setting: specify number of principal\
                                            components for PCA; b8 is 5.",
                                    b9 = "component" )
        b6.add_argument( "-n", "--iteration", b8 = 10, type=int,
                                    b5 = "Advanced Setting: specify number of gradient\
                                            descent iterations for PCA; b8 is 10.",
                                    b9 = "iteration" )
        b10 = b4.add_parser( "train" )
        b10.add_argument( "-d", "--data", b8 = "*.pkl", type=str,
                                    b5 = "Specify input .pkl file which contains\
                                        a matrix of size nxd (n frames, d pixels);\
                                        b8 searches current directory.",
                                    b9 = "data_filepath" )
        b10.add_argument( "-o", "--output", b8 = "", type=str,
                                    b5 = "Specify name of output file excluding\
                                             file extension; b8 is the same\
                                             name as selected .pkl file.",
                                    b9 = "output_name" )
        b10.add_argument( "-s", "--size", b8 = b1, type=int, nargs=2,
                                    b5 = "Specify the image resolution of the frames\
                                             in .pkl; b8 is 120 by 160.",
                                    b9 = ( "img_height", "img_width" ) )
        b10.add_argument( "-k", "--component", b8 = 5, type=int,
                                    b5 = "Advanced Setting: specify number of principal\
                                            components for PCA; b8 is 5.",
                                    b9 = "component" )
        b10.add_argument( "-n", "--iteration", b8 = 10, type=int,
                                    b5 = "Advanced Setting: specify number of gradient\
                                            descent iterations for PCA; b8 is 10.",
                                    b9 = "iteration" )
        return vars( b3.parse_args() )
    def fonk3( self ):
        self.b2[ "size" ] = tuple( self.b2[ "size" ] )
        self.fonk5()
    def fonk4( self ):
        assert "." not in self.b2[ "output" ],\
                "--output should not exclude any file extension"
        assert len( self.b2[ "output" ] ) < 30,\
                "--output should not exceed 30 characters..."
        assert all( val < 3000 for val in self.b2[ "size" ] ),\
                "--size seems to be too large..."
        if self.b2[ "subParser" ] == "all"\
            or self.b2[ "subParser" ] == "preprocess":
            assert os.path.isdir( self.b2[ "input" ] )
        if self.b2[ "subParser" ] == "train":
            assert "pkl" in self.b2[ "data" ] and glob.glob( self.b2[ "data" ] ),\
                    "Input data file must be in .pkl format"
    def fonk5( self ):
        if self.b2[ "subParser" ] == "train":
            b11 = glob.glob( self.b2[ "data" ] )
            if len( b11 ) > 1:
                b12 = input( "Multiple .pkl files found: {}. Please enter one of the above: "
                                    .format( b11 ) )
                while( b12 not in b11 ):
                    b12 = input( "Multiple .pkl files found: {}. Please enter one of the above: "
                            .format( b11 ) )
            else:
                b12 = b11[ 0 ]
            self.b2[ "data" ] = b12
            self.b2[ "output" ] = b12.split( '.' )[ 0 ]
def fonk6( rgbImg ):
    return np.dot( rgbImg[...,:3], [ 0.2989, 0.5870, 0.1140 ] )