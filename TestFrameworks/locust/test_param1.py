#coding=utf8
#参数化： 循环取数据，数据可重复使用

from locust import TaskSet, task, HttpLocust

class UserBehavior(TaskSet):
    def on_start(self):
        self.index = 0
    @task
    def test_visit(self):
        url = self.locust.share_data[self.index]
        print('visit url: %s' % url)
        self.index = (self.index + 1) % len(self.locust.share_data)
        self.client.get(url)
class WebsiteUser(HttpLocust):
    host = 'http://debugtalk.com'
    task_set = UserBehavior
    share_data = ['url1', 'url2', 'url3', 'url4', 'url5']
    min_wait = 1000
    max_wait = 3000
