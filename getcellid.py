# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:20:23 2015

@author: Marco
"""
import bisect;
import sys;

def level_cell(cellid):
    return bisect.bisect_left(underbound, cellid);
    
def getcellid(cellid, normalised):
    level_ = level_cell(cellid); #at which level is the cell
    cellid_n = cellid - underbound[level_-1] - 1; #normalized cellid
    fintile = [];
    if cellid == 0:
        cellid_n = 0;
    if level < level_:              # If the level is too low 
        return None;
    if level > level_:              # If an upperlevel cell comes in
        iterat_n = level - level_; #amount of iterations needed to find bottom level cell
        print "iterations "+str(iterat_n) + " -------------------";
        temp_tile_l = [];
        togo_tile_l = [];
        togo_tile_l.append(cellid_n);
        for x in range(0, iterat_n):
            for y in togo_tile_l:
                temp_tile_l.extend( range(y*4, (y+1)*4) );
            togo_tile_l = temp_tile_l[:];
            temp_tile_l = [];
        for x in togo_tile_l:
            t = x + underbound[level-1] + 1;
            if t not in tile_l:
                fintile.append(int(t));
                tile_l.append(int(t));
    else:
        tile_l.append(int(cellid));
        fintile = [int(cellid)];
    if normalised:
        fintile_n = []
        for x in fintile:
            fintile_n.append(x - underbound[level-1] - 1); #normalized cellid
        return fintile_n;
    else:
        return fintile;
        
def main():
    points = int(sys.stdin.readline().split(" ")[2]);
    for i in range(0, 2):
        sys.stdin.readline();
    ox, oy, oz = map(float, sys.stdin.readline().split(" ")[2:5]);
    bb_min = map(float, sys.stdin.readline().split(" ")[2:5]);
    bb_max = map(float, sys.stdin.readline().split(" ")[2:5]);
    print points;
    print bb_min;
    print bb_max;
    
    global level;    
    level = int(sys.argv[1]);
    global underbound;
    underbound = [];
    underbound.append(0)
    for x in range(1, level+1):
        underbound.append(underbound[-1]+4**x)
    global tile_l;      #list of tiles that have already been used
    tile_l = [];
    while True:
        line = sys.stdin.readline();
        if line != '':
            if line[0] == 'v':              
                pass;
            if line[0] == 'x':
                cell = int(line.split(" ")[2]);
                result = getcellid(cell, True);
                if result != None:
                    print result;
                if cell == 0:
                    break;
                
if __name__ == "__main__":
    main() 