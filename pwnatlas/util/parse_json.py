import json

def parse_cve(parsed_data):
    return {
        'cve': parsed_data["id"],
        'published': parsed_data["published"],
        'description': parsed_data["descriptions"][0]["value"],
        'cvss_score': parsed_data["metrics"]["cvssMetricV2"][0]["cvssData"]["baseScore"],
        'cvss_severity': parsed_data["metrics"]["cvssMetricV2"][0]["baseSeverity"],
        'cvss_vectorString': parsed_data["metrics"]["cvssMetricV2"][0]["cvssData"]["vectorString"]
    }
    
def parse_news(parsed_data):
    return {
        'foo': 'bar'
    }