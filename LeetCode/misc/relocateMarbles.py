class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        final_pos = set(nums)
        n = len(moveFrom)
        for i in range(n):
            if moveFrom[i] in final_pos:
                final_pos.remove(moveFrom[i])
                final_pos.add(moveTo[i])
        return sorted(list(final_pos))