class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_mask = [0] * len(board)
        col_mask = [0] * len(board)
        box_mask = [0] * len(board)

        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                
                bit_position = int(board[row][col]) - 1
                digit_mask = 1 << bit_position
                box_index = (row // 3) * 3 + (col // 3)
                
                if digit_mask & row_mask[row]:
                    return False 
                if digit_mask & col_mask[col]:
                    return False 
                if digit_mask & box_mask[box_index]:
                    return False 

                row_mask[row] |= digit_mask
                col_mask[col] |= digit_mask
                box_mask[box_index] |= digit_mask
        
        return True