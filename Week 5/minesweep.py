grid =[['-', '#','-','-'],
       ['#', '#','-','-'],
       ['#', '-','#','-'],
       ['-', '#','#','-']]
# loop through every row of array grid
for i, row in enumerate(grid):
    # get the length of array grid
    grid_len = len(grid)
    # loop though every column of row
    for j, cell in enumerate(row):
        # check if the current cell is not a hashtag
        if cell != '#':
            #get the length of row
            row_len = len(row)
            count = 0
            #check all neighbouring cells and count the hashtags, if the cells are out of the range,ignore
            if i-1 >= 0 and j-1 >= 0:
                nw = grid[i-1][j-1]
                if nw == '#':
                    count += 1
            if j-1 >= 0:
                w = grid[i][j-1]
                if w == '#':
                    count += 1
            if i-1 >=0:
                n = grid[i-1][j]
                if n == '#':
                    count += 1
            if j+1 < row_len:
                e = grid[i][j+1]
                if e == '#':
                    count += 1  
            if i-1 >=0 and j+1 < row_len:
                ne = grid[i-1][j+1]
                if ne == '#':
                    count += 1
            if i+1 < grid_len and  j-1 >= 0:   
                sw = grid[i+1][j-1]
                if sw == '#':
                    count += 1
            if i+1 < grid_len:
                s = grid[i+1][j]
                if s == '#':
                    count += 1
            if i+1 < grid_len and j+1 < row_len:
                se = grid[i+1][j+1]
                if se == '#':
                    count += 1
            #set the count in the currentt cell
            grid[i][j] = count


for row in grid:
    print(row)