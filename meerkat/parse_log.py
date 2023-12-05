import json

try:
    with open("meerkat-alerts.json", "r") as f:
        # Do something with the file content here
        data = f.read()
        parsed_data = json.loads(data)

        # Filter for severity 3 and retrieve signatures
        severity_3_signatures = [snippet['alert']['signature'] for snippet in parsed_data if snippet.get('alert', {}).get('severity') == 1]

        # Print filtered signatures
        for signature in severity_3_signatures:
            print(signature)
except FileNotFoundError:
    print("File not found or path is incorrect.")
except IOError:
    print("An error occurred while reading the file.")

'''
import json

try:
    with open("meerkat-alerts.json", "r") as f:
        # Do something with the file content here
        data = f.read()
        parsed_data = json.loads(data)

        # Filter for severity 3
        severity_3_snippets = [snippet for snippet in parsed_data if snippet.get('alert', {}).get('severity') == 1]

        # Print filtered JSON snippets
        for snippet in severity_3_snippets:
            print(json.dumps(snippet, indent=2))
except FileNotFoundError:
    print("File not found or path is incorrect.")
except IOError:
    print("An error occurred while reading the file.")
'''