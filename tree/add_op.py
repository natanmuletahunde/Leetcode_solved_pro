class Solution(object):
    def addOperators(self, num, target):
        res = []

        def dfs(index, path, value, last):
            if index == len(num):
                if value == target:
                    res.append(path)
                return

            for i in range(index + 1, len(num) + 1):
                temp = num[index:i]
                # skip numbers with leading zero
                if len(temp) > 1 and temp[0] == '0':
                    continue
                curr = int(temp)

                if index == 0:
                    dfs(i, temp, curr, curr)  # first number, no operator
                else:
                    dfs(i, path + '+' + temp, value + curr, curr)
                    dfs(i, path + '-' + temp, value - curr, -curr)
                    dfs(i, path + '*' + temp, value - last + last * curr, last * curr)

        dfs(0, "", 0, 0)
        return res
