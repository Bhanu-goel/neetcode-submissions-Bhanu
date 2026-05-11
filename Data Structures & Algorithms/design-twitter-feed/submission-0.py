import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)   

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)

        for user in self.following[userId]:
            if self.tweets[user]:
                idx = len(self.tweets[user])-1
                time,tweetId = self.tweets[user][idx]
                heap.append((time,tweetId,user,idx-1))

        heapq.heapify_max(heap)

        ans = []

        while heap and len(ans) < 10:
            time,tweetId,user,idx = heapq.heappop_max(heap)
            ans.append(tweetId)

            if idx >=0:
                time,tweetId = self.tweets[user][idx]
                heapq.heappush_max(heap,(time,tweetId,user,idx-1))
        
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].discard(followeeId)
