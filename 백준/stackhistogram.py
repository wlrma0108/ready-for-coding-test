import sys

def largest_rectangle_area(heights):
    """
    heights: List[int]
    반환값: 최대 직사각형 넓이 (int)
    단조 증가 스택으로 O(n)에 계산.
    """
    # 센티넬(0 높이) 추가: 마지막에 남은 막대들을 자동 정리
    heights.append(0)

    stack = []  # 높이가 '단조 증가'가 되도록 인덱스를 유지
    max_area = 0

    for i, h in enumerate(heights):
        # 현재 막대 h가 스택 top의 막대보다 낮아졌다면, 면적 계산 타이밍
        # '>'를 사용: 같을 때는 pop하지 않고 폭을 더 넓힐 기회를 준다(비감소 유지).
        while stack and heights[stack[-1]] > h:
            top = stack.pop()
            height = heights[top]  # 이번에 확정 계산할 높이

            # 왼쪽 경계: pop 후 스택의 새 top 바로 오른쪽
            # 오른쪽 경계: 현재 i 바로 직전 (i-1)
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i  # 스택이 비면 왼쪽 끝까지 확장 가능

            area = height * width
            if area > max_area:
                max_area = area

        # 현재 인덱스를 push하여 비감소 스택 유지
        stack.append(i)

    heights.pop()  # 센티넬 제거(원본 복원; 선택 사항)
    return max_area


def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    out_lines = []
    for token in it:
        n = int(token)
        if n == 0:
            break
        # n개의 높이를 차례로 읽는다.
        heights = [int(next(it)) for _ in range(n)]
        out_lines.append(str(largest_rectangle_area(heights)))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    main()