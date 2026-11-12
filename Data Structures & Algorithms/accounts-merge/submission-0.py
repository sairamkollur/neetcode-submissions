class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = collections.defaultdict(set)
        for index, account in enumerate(accounts):
            for email in account[1:]:
                d[email].add(index)
        
        def dfs(index):
            res = [index]
            for email in accounts[index][1:]:
                for nei in d[email]:
                    if nei not in seen:
                        seen.add(nei)
                        res += dfs(nei)
            return res
        def process(t):
            name = accounts[t[0]][0]
            res = [name]
            s = set()
            for index in t:
                for email in accounts[index][1:]:
                    s.add(email)
            res += sorted(s)
            return res
        
        l = []
        seen = set()
        for index, account in enumerate(accounts):
            if index not in seen:
                t = dfs(index)
                l.append(process(t))
        return l