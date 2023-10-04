import requests
import json
from .util import parse_json, exploitdb

#################################################################################
#       module: pwnatlas.get                                                     #
#       used to get cve data by id or keyword search                            #
#       note: keyword search currently limited to the first result. for more    #
#       specific results, please use a more specific query.                     #
#################################################################################
    
def by_id(id):                  # pwnatlas.get.by_id()
    data = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=" # api call
                 + id)
    
    if data.status_code != 200:
        return False
    
    parsed_data = json.loads(data.text)["vulnerabilities"][0]["cve"] # preprocessing the json output as it is put into a dict
    
    try:
        cve_dict = parse_json.parse_cve(parsed_data)
    except KeyError:
        #print("One of your values is incorrect. Please check input.")
        return False
    
    return cve_dict
    
def by_keyword(keywords):       # pwnatlas.get.by_keyword()
    data = requests.get("https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch="
                        + keywords
                        + "&keywordExactMatch&resultsPerPage=1")
    
    if data.status_code != 200:
        return False
    
    parsed_data = json.loads(data.text)["vulnerabilities"][0]["cve"]
    
    try:
        cve_dict = parse_json.parse_cve(parsed_data)
    except KeyError:
        #print("One of your values is incorrect. Please check input.")
        return False
    
    return cve_dict

def find_exploit(id): # cve id
    return exploitdb.search(id) if not False else False