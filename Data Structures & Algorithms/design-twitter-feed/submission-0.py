import heapq
from collections import defaultdict
from typing import List


class Twitter:

    def __init__(self):
        self.time = 0

        # Stores: (-time, userId, tweetId)
        self.max_heap = []

        # followerId -> set of followed users
        self.account = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        # Negative time makes the latest tweet come out first.
        heapq.heappush(
            self.max_heap,
            (-self.time, userId, tweetId)
        )

    def getNewsFeed(self, userId: int) -> List[int]:
        # Users must always see their own tweets.
        self.account[userId].add(userId)

        temp = []
        news = []

        while self.max_heap and len(news) < 10:
            info = heapq.heappop(self.max_heap)
            temp.append(info)

            _, tweet_user_id, tweet_id = info

            if tweet_user_id in self.account[userId]:
                news.append(tweet_id)

        # Restore all temporarily removed tweets.
        for info in temp:
            heapq.heappush(self.max_heap, info)

        return news

    def follow(self, followerId: int, followeeId: int) -> None:
        self.account[followerId].add(followerId)
        self.account[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # A user should continue following themselves.
        if followerId == followeeId:
            return

        self.account[followerId].discard(followeeId)