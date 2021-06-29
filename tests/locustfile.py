import random

from locust import between, task
from locust.contrib.fasthttp import FastHttpUser


class SimpleUser(FastHttpUser):
    wait_time = between(0.5, 2.5)
    # @task
    # def echo(self):
    #     self.client.post("/echo?echo=foo")

    @task
    def initial_valid(self):
        self.client.get("/")
        self.client.post(
            "/waypoints",
            json={
                "waypoint": f"{random.uniform(-100.0, 100.0)}, {random.uniform(-100.0,100.0)}"
            },
        )
        self.client.get("/waypoints?offset=0&limit=10")
