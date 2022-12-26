import requests
import csv

URL_Bugs = "http://127.0.0.1:8000/bugs/"
URL_Comments = "http://127.0.0.1:8000/comments/"
bugs_package = {}
bugs_comment = {}

# parses the list of bugs

def parse_bugs(bugs):
	for bug in bugs:
		package = bug['package']
		if package not in bugs_package:	
			bugs_package[package] = 0
		bugs_package[package] +=1
	
	return 


def parse_comments(comments):
	for comment in comments:
		ids = comment['bug']
		id_bug = ids.split('/')[-2]
		if id_bug not in bugs_comment:	
			bugs_comment[id_bug] = 0
		bugs_comment[id_bug] +=1
	
	return 


def main():
	#Bugs Requests
	bug_url =  URL_Bugs
	
	while bug_url:
		response_bug = requests.get(bug_url, auth = ('jalmeid2', 'qnc3m5th'))
		parsed_response = response_bug.json()
		bugs = parsed_response['results']
		parse_bugs(bugs)	
		bug_url = parsed_response['next']
	
	
	#Comments Requests
	comments_url =  URL_Comments
	
	while comments_url:
		response_comments = requests.get(comments_url, auth = ('jalmeid2', 'qnc3m5th'))
		parsed_response = response_comments.json()
		comments = parsed_response['results']
		parse_comments(comments)	
		comments_url = parsed_response['next']

	#Writing CSV Files
	
	with open('total_bugs_per_package.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',',quotechar='"')
		writer.writerow(['package', 'total'])
		for key, value in bugs_package.items():
			writer.writerow([key, value])
	
	
	with open('total_comments_per_bug.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter = ',', quotechar='"')
		writer.writerow(['bug_id', 'total'])
		for key, value in bugs_comment.items():
			writer.writerow([key, value])
	
	
if __name__ == '__main__':
	main()
