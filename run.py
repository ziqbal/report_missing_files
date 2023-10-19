#!/usr/bin/env python3

import os
import sys

####################################################################

FN_PREFIX = "IMG_"
FN_NPAD = 4

if len( sys.argv ) == 2 :
    FN_PREFIX = sys.argv[ 1 ]

if len( sys.argv ) == 3 :
    FN_PREFIX = sys.argv[ 1 ]
    FN_NPAD = int( sys.argv[ 2 ] )

print( f"FN_PREFIX , FN_NPAD = {FN_PREFIX} , {FN_NPAD}" )

FN_PREFIX_LOWER = FN_PREFIX.lower(  )

####################################################################

scan_files = os.scandir( os.getcwd(  ) )

####################################################################

list_files = [ ]

for f in scan_files :
    if not f.is_file( ) : continue
    if not f.name.lower(  ).startswith( FN_PREFIX_LOWER ) : continue
    list_files.append( f.name )

list_files.sort( )
#print( list_files )

####################################################################

seq_min = 1
seq_max = pow(  10 , FN_NPAD ) - 1

board = [ ]

for n in range( seq_min , seq_max + 1 ) :
    board.append( False )

####################################################################

for fn in list_files:
    f , e  = os.path.splitext(fn)
    if len(f)<FN_NPAD: continue
    n = f[-FN_NPAD:]
    if not n.isnumeric(): continue
    n=int(n)
    #print(f"{f} {e} {n}")
    board[n-1]=True

#print(board)

####################################################################

gap_count = 0
state_ingap = True

for n in range( seq_min , seq_max + 1 ) :
    #print(n) 
    if state_ingap :
        if not board[ n - 1 ] :
            gap_count = gap_count + 1
            continue
        state_ingap = False
        if gap_count == 0 :
            continue

        str_from = f"{n-gap_count}".zfill( FN_NPAD )
        str_to = f"{n-1}".zfill( FN_NPAD )
        print( f"MISSING #### {str_from} -> {str_to} ( {gap_count} )" )
        gap_count = 0
        continue

    if not state_ingap :
        if not board[ n - 1 ] :
            gap_count = 1
            state_ingap = True
            continue

if state_ingap and gap_count > 0 :
    str_from = f"{n-gap_count+1}".zfill( FN_NPAD )
    str_to = f"{n}".zfill( FN_NPAD )
    print( f"MISSING #### {str_from} -> {str_to} ( {gap_count} )" )

