#!/usr/bin/env python3

import os
import sys
import random

####################################################################

FN_PREFIX = "IMG_"
FN_NPAD = 4

if len( sys.argv ) == 2 :
    FN_PREFIX = sys.argv[ 1 ]

if len( sys.argv ) == 3 :
    FN_PREFIX = sys.argv[ 1 ]
    FN_NPAD = int(sys.argv[ 2 ])

print( f"FN_PREFIX , FN_NPAD = {FN_PREFIX} , {FN_NPAD}" )

FN_PREFIX_LOWER = FN_PREFIX.lower(  )

####################################################################

SWD = os.path.dirname( os.path.abspath( __file__ ) )

dir_local = f"{SWD}/local"

if not os.path.isdir( dir_local ) : os.mkdir( dir_local )

for f in os.listdir(dir_local):
    os.remove(os.path.join(dir_local, f))

####################################################################

seq_min = 1
seq_max = pow(  10 , FN_NPAD ) - 1

seq_start = random.randint( seq_min , seq_max )
seq_end = random.randint( seq_min , seq_max )


print(f"{seq_min}-{seq_max} -> seq_start={seq_start} seq_end={seq_end}")

####################################################################

exts = [ "jpg" , "png" , "mov" , "mp4" ]

def file_create( n ) :
    n_padded = f"{n}".zfill( FN_NPAD )
    fn = f"{dir_local}/{FN_PREFIX}x{n_padded}." + random.choice( exts )
    fp = open( fn , "x" )
    fp.close( )
    print( fn )

####################################################################

seq_current = seq_start

while True :
    file_create( seq_current )

    if seq_current == seq_end :
        break 

    seq_current = seq_current + 1
    if seq_current > seq_max : seq_current = seq_min

####################################################################


