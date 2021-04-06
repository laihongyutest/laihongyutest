# ！/usr/bin/env python
# encoding:utf-8
from locust import HttpUser, task, TaskSet

"""
主机属性host，体重属性weight，任务属性task，环境属性environment，wait_time属性
主机host。weight体重，task任务，environment环境，wait_time属性
"""


# class QuickstarUser(HttpUser):
#     wait_time = between(1, 2)
#
#     @task
#     def index_page(self):
#         self.client.get('/测试')
#         self.client.get('/python自动化')
#     @task(3)
#     def view_item(self):
#         for item in range(10):
#             self.client.get(f)


class TestIndex(TaskSet):
    @task
    def getindex(self):
        self.client.get('/')


class WebSite(HttpUser):
    task_set = TestIndex
    min_wait = 1000
    max_wait = 2000
