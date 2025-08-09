def count_islands(grid):
  if not grid:
    return 0

  rows = len(grid)
  cols = len(grid[0])
  visited = [[False for _ in range(cols)] for _ in range(rows)]

  def dfs(r, c):
    if (
      r < 0 or r >= rows or
      c < 0 or c >= cols or
      grid[r][c] != 'L' or
      visited[r][c]
    ):
      return

    visited[r][c] = True

    directions = [
      (-1, 0), (1, 0), (0, -1), (0, 1),
      (-1, -1), (-1, 1), (1, -1), (1, 1)
    ]

    for dr, dc in directions:
      dfs(r + dr, c + dc)

  island_count = 0

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 'L' and not visited[i][j]:
        dfs(i, j)
        island_count += 1

  return island_count

print("Enter the number of rows:")
n = int(input())

print("\nEnter the grid rows :")
grid = []
for _ in range(n):
    row = input().strip().split()
    grid.append(row)

result = count_islands(grid)
print("\nNumber of islands:", result)
