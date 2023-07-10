import heapq

class KthLargest:
    def __init__(self, nums, k):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, num):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, num)
        elif num > self.heap[0]:
            heapq.heappop(self.heap)
            heapq.heappush(self.heap, num)

        return self.heap[0]

def main():
    kthLargest = KthLargest([4, 1, 3, 12, 7, 14], 3)
    print(kthLargest.add(6))  # returns '7'
    print(kthLargest.add(13))  # returns '12'
    print(kthLargest.add(4))  # returns '12'

main()
