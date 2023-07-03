from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def get_message(self):
        self.client.get("/")
    @task
    def save_message(self):
        headers = {
            'Content-type': 'application/json'
        }
        payload = {
            'text': 'mallorca'
        }
        self.client.post("/", headers=headers, json=payload)
