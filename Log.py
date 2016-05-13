class Log:
    def __init__(self, client_ip, client_identd, user_id, date_time, request_type, requested_resource, response_code,
                 content_size, agent):
        self.client_ip = client_ip
        self.client_identd = client_identd
        self.user_id = user_id
        self.date_time = date_time
        self.request_type = request_type
        self.requested_resource = requested_resource
        self.response_code = response_code
        self.content_size = content_size
        self.agent = agent

    def __str__(self):
        return self.client_ip + ', ' + self.client_identd + ', ' + self.user_id + ', ' + self.date_time.strftime("%d/%b/%Y:%H:%M:%S %z") + ', ' +\
               self.request_type + ', ' + self.requested_resource + ', ' + str(self.response_code) + ', ' + str(self.content_size) + ', ' + self.agent
