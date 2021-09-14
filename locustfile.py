from locust import HttpUser, task

# https://docs.locust.io/en/stable/quickstart.html
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")