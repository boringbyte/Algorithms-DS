import heapq
import random


def verify_alien_dictionary(words, order):
    # Time Complexity: O(N * M) where N is number of words and M is avg number of characters in each word
    # Space Complexity: O(1)
    order_map = {ch: i for i, ch in enumerate(order)}

    def check_order(word1, word2):
        for ch1, ch2 in zip(word1, word2):
            if ch1 != ch2:
                return order_map[ch1] < order_map[ch2]
            return len(ch1) <= len(ch2)
    return all(check_order(word1, word2) for word1, word2 in zip(words, words[1:]))


def minimum_remove_to_make_valid_parentheses1(s):
    # Time Complexity: O(N)
    # Space Complexity: O(N)
    in_valid, stack = set(), []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                in_valid.add(i)
    while stack:
        in_valid.add(stack.pop())
    return "".join(char for i, char in enumerate(s) if i not in in_valid)


def minimum_remove_to_make_valid_parentheses2(s):
    s, stack = list(s), []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                s[i] = ""
    while stack:
        s[stack.pop()] = ""
    return "".join(s)


def k_closest_points_to_origin1(points, k):
    # Time Complexity: O(NlogN)
    # Space Complexity:
    return sorted(points, key=lambda x, y: x * x + y * y)[:k]


def k_closest_points_to_origin2(points, k):
    # O(nlogk) --> n for loop and logk for push and pop
    # We want to maintain max heap, that's why we use -ve distance
    def euclidean(x, y):
        return x * x + y * y

    heap = []
    for i, (x, y) in enumerate(points):
        distance = euclidean(x, y)
        if len(heap) >= k:
            heapq.heapreplace(heap, (-distance, i))
        else:
            heapq.heappush(heap, (-distance, i))
    return [points[i] for (_, i) in heap]


def k_closest_points_to_origin3(points, k):
    # O(n) because of quick select algorithm. This is mainly used to find k min or max in an unsorted array
    # During quick select algorithm, our search space becomes half on average for each loop.
    """
    Quick select algorithm
        1. Set the left and right and pivot index to 0, n-1 and n as initial values
        2. Loop till pivot index not equals to k
        3. During the loop process, get new pivot index using partition function
        4. Now update left to pivot_index + 1 if pivot is less than k
        5. Now update right to pivot_index - 1 if pivot or else.

    Partition logic
        1. Find the pivot index between left and right mid-points or some random point between left and right inclusive
        2. Set i and pivot_distance to left and Euclidean in this instance
        3. Swap right and pivot index with each other
        4. Loop from left to right + 1
        5.      If Euclidean distance of j is less than pivot_distance
        6.      Swap the i and j elements
        7.      Update i to i + 1
        8. Finally return i - 1
    """

    def euclidean(point):
        x, y = point
        return x * x + y * y

    def swap(i, j):
        points[i], points[j] = points[j], points[i]

    def partition(left, right):
        pivot_index = left + (right - left) // 2
        i, pivot_distance = left, euclidean(points[pivot_index])
        swap(pivot_index, right)
        for j in range(left, right + 1):
            if euclidean(points[j]) < pivot_distance:
                swap(i, j)
                i += 1
        return i - 1

    left, right, pivot_index = 0, len(points) - 1, len(points)
    while pivot_index != k:
        pivot_index = partition(left, right)
        if pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1
    return points[:k]


def k_closest_points_to_origin4(points, k):
    n = len(points)

    def euclidean(point):
        x, y = point
        return x * x + y * y

    def swap(i, j):
        points[i], points[j] = points[j], points[i]

    def partition(left, right, pivot_index):
        pivot = euclidean(points[pivot_index])
        swap(pivot_index, right)
        pivot_index = left
        for i in range(left, right):
            if euclidean(points[i]) <= pivot:
                swap(i, pivot_index)
                pivot_index += 1
        swap(pivot_index, right)
        return pivot_index

    def quick_select(left, right):
        if left < right:
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if k == pivot_index:
                return
            elif k < pivot_index:
                quick_select(left, pivot_index - 1)
            else:
                quick_select(pivot_index + 1, right)

    quick_select(0, n - 1)
    return points[:k]


def product_of_array_except_self1(nums):
    n = len(nums)
    prefix, suffix = [1] * n, [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]

    return [p * f for p, f in zip(prefix, suffix)]


def valid_palindrome_2(s):
    def check_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return check_palindrome(i + 1, j) or check_palindrome(i, j - 1)
    return True


def sub_array_sum_equals_k(nums, k):
    # In this all are positive numbers only
    # In comments of https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation
    prefix_sum, prefix_sum_counts, result = 0, {0: 1}, 0
    for num in nums:
        prefix_sum += num
        diff = prefix_sum - k
        if diff in prefix_sum_counts:
            result += prefix_sum_counts[diff]
        prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
    return result


class BinaryMatrix:
    def get(self, row, col):
        pass

    def dimensions(self):
        pass


def leftmost_column_with_at_least_a_one1(binary_matrix):
    # https://walkccc.me/LeetCode/problems/1428/
    # https://medium.com/@srihari.athiyarath/leftmost-column-with-at-least-a-one-24184d8f4052
    m, n = binary_matrix.dimensions()
    result = float('inf')
    for i in range(m):
        l, r = 0, n
        while l < r:
            mid = l + (r - 1) // 2
            if binary_matrix.get(i, mid) == 0:
                l = mid + 1
            else:
                r = mid
        if l < n and binary_matrix.get(i, l) == 1:
            result = min(result, l)
    return result if result < float('inf') else -1


def leftmost_column_with_at_least_a_one2(binary_matrix):
    m, n = binary_matrix.dimensions()
    result, l, r = -1, 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if any(binary_matrix.get(i, mid) for i in range(m)):
            result = mid
            r = mid - 1
        else:
            l = mid + 1
    return result


def leftmost_column_with_at_least_a_one3(binary_matrix):
    m, n = binary_matrix.dimensions()
    r, c = 0, n - 1
    while r < m and c >= 0:
        if binary_matrix.get(r, c) == 0:
            r += 1
        else:
            c -= 1
    return c + 1 if c + 1 != n else -1  # if c + 1 == n means we reached last row, last column, and it's still zero


def add_strings(num1, num2):
    def string_to_digit(d):
        return ord(d) - ord('0')

    i, j, carry, result = len(num1) - 1, len(num2) - 1, 0, []
    while i >= 0 or j >= 0 or carry:
        digit1 = string_to_digit(num1[i]) if i >= 0 else 0
        digit2 = string_to_digit(num2[j]) if j >= 0 else 0
        carry, digit = divmod(digit1 + digit2 + carry, 10)
        result.append(str(digit))
        i, j = i - 1, j - 1
    return ''.join(result[::-1])


def merge_intervals1(intervals):
    intervals, result = sorted(intervals, key=lambda x: x[0]), []
    for interval in intervals:
        if not result or result[-1][-1] < interval[0]:
            result.append(interval)
        else:
            result[-1][-1] = max(result[-1][-1], interval[-1])
    return result


def merge_intervals2(intervals):
    intervals, result = sorted(intervals, key=lambda x: x[0]), []
    for start, end in intervals:
        if not result or start > result[-1][-1]:
            result.append([start, end])
        else:
            result[-1][-1] = max(result[-1][-1], end)
    return result


def add_binary(a, b):
    # https://leetcode.com/problems/add-binary/discuss/1679423/Well-Detailed-Explaination-Java-C%2B%2B-Python-oror-Easy-for-mind-to-Accept-it
    digit_map = {'0': 0, '1': 1}
    i, j, carry, result = len(a) - 1, len(b) - 1, 0, []
    while i >= 0 or j >= 0 or carry:
        digit1 = digit_map[a[i]] if i >= 0 else 0
        digit2 = digit_map[b[j]] if j >= 0 else 0
        carry, digit = divmod(digit1 + digit2 + carry, 2)
        result.append(digit)
        i, j = i - 1, j - 1
    return ''.join(result[::-1])

