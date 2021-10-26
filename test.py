# -*- coding: utf-8 -*-

import json
from time import time

import urllib3

http = urllib3.PoolManager()


def main():
    start = time()

    for _ in range(2000):
        http.request(
            "POST",
            "http://localhost:3001/ticket",
            headers={"Content-Type": "application/json"},
            body=json.dumps({
                "name": "x",
                "description": "...",
                "story_points": 3
            })
        )

        # print(r.data.decode("utf-8"))

    print(time() - start)


if __name__ == "__main__":
    main()
