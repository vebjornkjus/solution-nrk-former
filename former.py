from collections import deque
import heapq

def get_connected_shapes(board, x, y):
    shape = board[y][x]
    to_visit = deque([(x, y)])
    connected = set()

    while to_visit:
        cx, cy = to_visit.pop()
        if (cx, cy) not in connected and board[cy][cx] == shape:
            connected.add((cx, cy))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                    to_visit.append((nx, ny))
    
    return connected

def remove_shapes(board, connected):
    for x, y in connected:
        board[y][x] = 0

def apply_gravity(board):
    for col in range(len(board[0])):
        empty_row = len(board) - 1
        for row in range(len(board) - 1, -1, -1):
            if board[row][col] != 0:
                board[empty_row][col] = board[row][col]
                if empty_row != row:
                    board[row][col] = 0
                empty_row -= 1

def heuristic(board):
    # Calculate the number of connected components and the size of the largest group
    components = 0
    largest_group_size = 0
    visited = set()
    
    for y in range(len(board)):
        for x in range(len(board[0])):
            if (x, y) not in visited and board[y][x] != 0:
                connected = get_connected_shapes(board, x, y)
                components += 1
                largest_group_size = max(largest_group_size, len(connected))
                visited.update(connected)
    
    # Return a tuple of the number of components and the size of the largest group
    return components, largest_group_size


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()



def solve_board(board, max_depth=13):
    def board_to_tuple(board):
        return tuple(tuple(row) for row in board)

    start = board_to_tuple(board)
    visited = {}
    priority_queue = [(heuristic(board), 0, start, [])]

    while priority_queue:
        (components, largest_group_size), cost, current_board, path = heapq.heappop(priority_queue)
        if current_board in visited and visited[current_board] <= cost:
            continue
        visited[current_board] = cost
        if cost > max_depth:
            continue
        for y in range(len(current_board)):
            for x in range(len(current_board[0])):
                if current_board[y][x] != 0:
                    new_board = [list(row) for row in current_board]
                    connected = get_connected_shapes(new_board, x, y)
                    remove_shapes(new_board, connected)
                    apply_gravity(new_board)
                    new_board_tuple = board_to_tuple(new_board)
                    if new_board_tuple not in visited or visited[new_board_tuple] > cost + 1:
                        new_cost = cost + 1
                        new_components, new_largest_group_size = heuristic(new_board)
                        new_path = path + [(x, y)]
                        heapq.heappush(priority_queue, ((new_components, new_largest_group_size), new_cost, new_board_tuple, new_path))
                        print(f"Visiting path: {new_path}")
                        if all(cell == 0 for row in new_board for cell in row):
                            return new_path
    
    return None

# Board needs to be changed manually every day
board = [
    [3, 2, 1, 3, 3, 2, 3],
    [4, 1, 1, 2, 3, 2, 3],
    [3, 2, 1, 1, 1, 2, 2],
    [4, 4, 1, 3, 3, 4, 1],
    [1, 4, 1, 2, 3, 4, 4],
    [3, 4, 2, 3, 3, 1, 3],
    [3, 2, 2, 2, 4, 1, 3],
    [4, 1, 4, 1, 4, 1, 3],
    [3, 3, 3, 1, 2, 1, 3],
]

solution = solve_board(board)
if solution:
    current_board = [row[:] for row in board]  # Make a copy of the board
    for move in solution:
        x, y = move
        symbol = current_board[y][x]
        print(f"Move: ({x+1}, {len(board)-y}) (Symbol: {symbol})")
        connected = get_connected_shapes(current_board, x, y)
        remove_shapes(current_board, connected)
        apply_gravity(current_board)
        print_board(current_board)
    print(f"Solved in {len(solution)} moves.")
    print(f"Optimal move sequence: {' -> '.join(map(str, [(x+1, len(board)-y) for x, y in solution]))}")
else:
    print("No solution found.")
