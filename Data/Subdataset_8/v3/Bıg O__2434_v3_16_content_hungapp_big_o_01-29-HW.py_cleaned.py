def solve_first_problem():
    na, nb = map(int, input().split())
    k, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a[k - 1] < b[-m]:
        print("YES")
    else:
        print("NO")
def solve_second_problem():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    min_value = min(points, key=lambda x: x[0])[0]
    max_value = max(points, key=lambda x: x[1])[1]
    answer = next(i + 1 for i, (x, y) in enumerate(points) if x == min_value and y == max_value)
    print(answer)
def solve_third_problem():
    n = int(input())
    teams = [tuple(map(int, input().split())) for _ in range(n)]
    sorted_teams = sorted(teams, key=lambda x: abs(x[0] - x[1]), reverse=True)
    final_1 = [1 if i < n
    final_2 = [1 if i < n
    print(''.join(map(str, final_1)))
    print(''.join(map(str, final_2)))
def solve_fourth_problem():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    count = [0] * (m + 1)
    for genre in a:
        count[genre] += 1
    ways = sum(count[i] * count[j] for i in range(1, m) for j in range(i + 1, m + 1))
    print(ways)
def main():
    solve_first_problem()
if __name__ == "__main__":
    main()