#https://codeforces.com/contest/1351/problem/C

def skier(movements):
    visited_segments = set()
    x, y = 0, 0  
    total_time = 0

    def lilkaw(x1, y1, x2, y2):
        return (min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    
    for move in movements:
        next_x, next_y = x, y
        if move == 'N':
            next_y += 1
        elif move == 'S':
            next_y -= 1
        elif move == 'E':
            next_x += 1
        elif move == 'W':
            next_x -= 1
        
        segment = lilkaw(x, y, next_x, next_y)
        
        if segment not in visited_segments:
            total_time += 5
            visited_segments.add(segment)
        else:
            total_time += 1
        
        x, y = next_x, next_y

    return total_time

t = int(input())
for _ in range(t):
    movements = input().strip()
    print(skier(movements))
