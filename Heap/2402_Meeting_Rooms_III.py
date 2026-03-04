import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        busy, free = [], list(range(n))
        heapq.heapify(free)                         
        meetingCount = [0] * n
        for start, end in meetings:
            duration = end - start

            while busy and busy[0][0] <= start:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(free, room)
            if free:
                room = heapq.heappop(free)
                heapq.heappush(busy, (end, room))
            else:
                endTime, room = heapq.heappop(busy)
                heapq.heappush(busy, (endTime + duration, room))

            meetingCount[room] += 1

        bestRoom = 0
        for room in range(1, n):
            if meetingCount[room] > meetingCount[bestRoom]:
                bestRoom = room
        return bestRoom

# Time Complexity: O(m log m + m log n) – We first sort the meetings by
# their start time, which takes O(m log m) time where m is the number of
# meetings. For each meeting, we may perform heap operations on the `busy`
# and `free` heaps. Each push or pop operation on a heap of size at most n
# (the number of rooms) takes O(log n) time. Since we process all m meetings
# and perform a constant number of heap operations per meeting, the total
# heap cost is O(m log n). Thus, the overall time complexity is
# O(m log m + m log n).

# Space Complexity: O(n) – The algorithm maintains two heaps: `free`, which
# stores up to n available room indices, and `busy`, which stores up to n
# rooms currently in use along with their end times. Additionally, we keep
# an array `meetingCount` of size n to track how many meetings each room
# hosts. Therefore, the auxiliary space used grows linearly with the number
# of rooms, resulting in O(n) space complexity.