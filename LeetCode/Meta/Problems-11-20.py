import random
import collections


def binary_tree_maximum_path_sum1(root):
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    result = [float('-inf')]

    def dfs(node):
        if node is None:
            return 0
        l, r = dfs(node.left), dfs(node.right)
        result[0] = max(result[0], l + r + node.val)
        return max(l + node.left, r + node.right, 0)

    dfs(root)
    return result[0]


def binary_tree_maximum_path_sum2(root):
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/278525/Python-iterative-solution
    result, current = float('-inf'), root
    stack, last, d = [], None, collections.defaultdict(int)
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        current = stack[-1]
        if current.right and last != current.right:
            root = current.right
        else:
            # Consume the node
            current = stack.pop()
            last = current
            d[current] = max(d[current.left] + current.val, d[current.right] + current.val, 0)
            result = max(result, d[current.left] + d[current.right] + current.val)
    return result


def valid_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() != s[r].lower():
                return False
            else:
                l, r = l + 1, r - 1
    return True


def k_th_largest_element_in_an_array(nums, k):
    n = len(nums)
    k = n - k

    def swap(i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def partition(left, right, p_index):
        pivot = nums[p_index]
        swap(p_index, right)
        p_index = left
        for i in range(left, right):
            if nums[i] <= pivot:
                swap(i, p_index)
                p_index += 1
        swap(p_index, right)
        return p_index

    def quick_select(left, right):
        p_index = random.randint(left, right)
        p_index = partition(left, right, p_index)
        if k == p_index:
            return
        elif k < p_index:
            quick_select(left, p_index - 1)
        else:
            quick_select(p_index + 1, right)

    quick_select(0, n - 1)
    return nums[k]


class SparseVector1:
    # https://zhenchaogan.gitbook.io/leetcode-solution/leetcode-1570-dot-product-of-two-sparse-vectors
    def __init__(self, nums):
        self.hashmap = {i: val for i, val in enumerate(nums) if val}

    def dot_product(self, vec):
        if len(self.hashmap) > len(vec.hashmap):
            self, vec = vec, self
        return sum(val * vec.hashmap[key] for key, val in self.hashmap.items() if key in vec.hashmap)


class SparseVector2:
    def __init__(self, nums):
        self.linked_list = [[i, val] for i, val in enumerate(nums) if val]

    def dot_product(self, vec):
        if len(self.linked_list) > len(vec.linked_list):
            self, vec = vec, self
        result = i = j = 0
        n1, n2 = len(self.linked_list), len(vec.linked_list)
        while i < n1 and j < n2:
            if self.linked_list[i][0] == vec.linked_list[j][0]:
                result += self.linked_list[i][1] * vec.linked_list[j][1]
                i, j = i + 1, j + 1
            elif self.linked_list[i][0] < vec.linked_list[j][0]:
                i += 1
            else:
                j += 1
        return result


def range_sum_of_binary_search_tree(root, low, high):
    result = [0]

    def dfs(node):
        if node:
            if low <= node.val <= high:
                result[0] += node.val
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)

    dfs(root)
    return result[0]


def binary_tree_right_side_view1(root):
    result, queue = [], collections.deque([root])
    if not root:
        return result
    while queue:
        for i in range(len(queue)):
            current = queue.popleft()
            if i == 0:
                result.append(current.val)
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
    return result


def binary_tree_right_side_view2(root):
    result, visited = [], set()
    if not root:
        return result

    def dfs(node, level):
        if node:
            if level not in visited:
                visited.add(level)
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)

    dfs(root, 0)
    return result


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class WordDictionary:
    # https://leetcode.com/problems/design-add-and-search-words-data-structure/discuss/774530/Python-Trie-solution-with-dfs-explained
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        n = len(word)

        def dfs(node, i):
            if i == n:
                return node.is_word
            if word[i] == ".":
                for char in node.children:
                    if dfs(node.children[char], i + 1):
                        return True
            if word[i] in node.children:
                node = node.children[word[i]]
                return dfs(node, i + 1)
            return False

        return dfs(self.root, 0)


def trapping_rain_water1(heights):
    # https://leetcode.com/problems/trapping-rain-water/discuss/1374608/C%2B%2BJavaPython-MaxLeft-MaxRight-so-far-with-Picture-O
    n, result = len(heights), 0
    max_left, max_right = [0] * n, [0] * n

    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i - 1])

    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i + 1])

    for i in range(n):
        water_level = min(max_left[i], max_right[i])
        if water_level > heights[i]:
            result += (water_level - heights[i])
    return result


def trapping_rain_water2(heights):
    max_left, max_right, result = heights[0], heights[-1], 0
    l, r = 1, len(heights) - 2
    while l <= r:
        max_left = max(max_left, heights[l])
        max_right = max(max_right, heights[r])
        if max_left < max_right:
            result += (max_left - heights[l])
            l += 1
        else:
            result += (max_right - heights[r])
            r -= 1
    return result


def merge_sorted_array(nums1, nums2, m, n):
    while n > 0:
        if m > 0 and nums1[m - 1] > nums2[n - 1]:
            nums1[m + n - 1] = nums1[m - 1]
            m -= 1
        else:
            nums1[m + n - 1] = nums2[n - 1]
            n -= 1


def first_bad_version(n):

    def is_bad_version(x):
        return x == 0

    l, r = 0, n
    while l < r:
        mid = l + (r - l) // 2
        if is_bad_version(mid):
            r = mid
        else:
            l = mid + 1
    return l
