


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        output_lst = [first]
        for i in range(len(encoded)):
            output_lst.append(output_lst[i] ^ encoded[i])
        return output_lst
