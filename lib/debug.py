from get_requester import GetRequester
url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
requester = GetRequester(url)
print(requester.get_response_body())
print(requester.load_json())