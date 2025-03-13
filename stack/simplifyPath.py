class Solution:
    def simplifyPath(self, path: str) -> str:
        s = []
        for d in path.split("/"):
            if d == ".":
                continue
            elif d == "..":
                if s:
                    s.pop()
            elif d:
                s.append(d)
        return "/" + "/".join(s)
