import sys

class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()

    def generate_board(self):
        #Nested list to represent the game board
        for i in range(self.h):
            self.board.append([0]*self.w)

    def print_board(self):
        print ("  ")
        print ("------")
        for elem in self.board:
            print (elem)
        print ("------")
        print ("  ")

    def generate_legal_moves(self, cur_pos):
        #list of moves for the knight to take next
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

    def sort_lonely_neighbors(self, to_visit):
        #More efficient to visit the lonely neighbors first. 
        #They are at the edges of the chessboard. 
        # Cannot be reached easily if done later 
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def tour(self, n, path, to_visit):
        #Recursive definition of knights tour.
        #Inputs are:
        #n = current depth of search tree
        #path = current path taken
        #to_visit = node to visit
        self.board[to_visit[0]][to_visit[1]] = n
        #append the newest vertex to the current point
        path.append(to_visit) 
        print ("Visiting: ", to_visit)
        
        #if every grid is filled
        if n == self.w * self.h: 
            self.print_board()
            print (path)
            print ("All Done")
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            #If exit loop, all neighbors failed, reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print ("Back to: ", path[-1])
            except IndexError:
                print ("No path found")
                sys.exit(1)

if __name__ == '__main__':
    #Size of grid.
    #8x8 grid
    kt = KnightsTour(8, 8)
    kt.tour(1, [], (0,0))
    kt.print_board()

