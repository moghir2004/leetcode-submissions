class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "[]"
        if len(strs) == 1:
            return strs[0]
        encoded_str = '❤️'.join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        if s == "":
            return ['']
        decoded_str = s.split("❤️")
        return decoded_str