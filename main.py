import requests as req
import re
import json
import sys
from os import path

MAIN_TABLE_REGEX = r'(?:### Connect)((?:.|\n)+)(?:### Command)'
DOWNLOAD_REGEX = r'(?:\[)([a-zA-Z.]*)(?:\]\()(.+)(?:\))'
IMAGE_URLS_REGEX = r'!\[([a-zA-Z ]*)\]\(.*?png\)'

RELEASES_FILENAME = 'releases.json'
RELEASES_FILENAME_MIN = 'releases.min.json'


def nested_dict_value_exists(os, arch, download_type, mirth_version, dict_to_test):
	for dict_element in dict_to_test:
		try:
			if dict_element["os"] == os and dict_element["arch"] == arch and dict_element[
				"downloadType"] == download_type and dict_element["tagName"] == mirth_version:
				return True
		except TypeError:
			pass

	return False


def main(url_tag_suffix):
	request_url = f"http://api.github.com/repos/nextgenhealthcare/connect/releases/{url_tag_suffix}"
	response = req.post(request_url)

	if response.status_code != 200:
		print(f"Request url: {request_url}")
		print(response.text)
		exit(1)

	response_json = response.json()

	# Get metadata tags from response json
	tag_name = response_json["tag_name"]
	published_at = response_json["published_at"]
	body = response_json["body"]

	# Format body to remove all image urls, but retain their respective os as a text value
	body = body.replace('\r\n', '\n')
	body = re.sub(IMAGE_URLS_REGEX, r'\1', body)
	body = body.replace('`', '')

	release_component_matches = re.findall(MAIN_TABLE_REGEX, body)[0].strip().split('\n')

	current_request_release_entries = []

	for index in range(2, len(release_component_matches)):
		row = release_component_matches[index]
		elements = row.split(' | ')

		download_data = re.findall(DOWNLOAD_REGEX, elements[2])[0]

		release_entry = {
			"os": elements[0].strip().lower(),
			"arch": elements[1].strip().lower(),
			"downloadType": download_data[0].strip().lower(),
			"downloadUrl": download_data[1].strip().lower(),
			"sha256": elements[3].strip().lower(),
			"md5": elements[4].strip().lower(),
			"publishedAt": published_at,
			"tagName": tag_name,
		}
		current_request_release_entries.append(release_entry)

	# Ensure releases file exists
	if path.isfile(RELEASES_FILENAME) is False:
		f = open(RELEASES_FILENAME, 'w+')
		f.write('[]')
		f.close()

	# Read existing releases file
	with open(RELEASES_FILENAME, "r") as fp:
		releases_list = json.load(fp)

	# Populate final list while filtering out elements that already exists in said list
	for release_entry in current_request_release_entries:
		if not nested_dict_value_exists(os=release_entry['os'],
										arch=release_entry['arch'],
										download_type=release_entry['downloadType'],
										dict_to_test=releases_list,
										mirth_version=tag_name):
			releases_list.append(release_entry)

	# Write JSON file
	with open(RELEASES_FILENAME, "w") as fp:
		json.dump(releases_list, fp, indent=4, separators=(',', ': '))

	# Write JSON minified file
	with open(RELEASES_FILENAME_MIN, "w") as fp:
		json.dump(releases_list, fp, indent=None, separators=(',', ':'))


if __name__ == '__main__':
	if len(sys.argv) != 2:
		url_suffix = "latest"
	else:
		url_suffix = f"tags/{sys.argv[1]}"

	main(url_suffix)
