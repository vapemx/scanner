import virustotal_python
import os.path
import requests


def file_vt(api_key, filename, output):

    try:
        files = {"file": (os.path.basename(filename), open(os.path.abspath(filename), "rb"))}

        # Getting the ID
        with virustotal_python.Virustotal(api_key) as vtotal:
            resp = vtotal.request("files", files=files, method="POST")
            dict1 = resp.json()
            dict2 = dict1["data"]
            id = dict2["id"]

        # Analizing the file
        url = "https://www.virustotal.com/api/v3/analyses/"+id

        headers = {
            "accept": "application/json",
            "id": id,
            "x-apikey": api_key
        }

        response_analysis = requests.get(url, headers=headers)
        analysis = response_analysis.text
        final_analysis = analysis.split("results", 1)[0]
        output.write("\n\n-------File Analysis-------\n")
        output.write("Filename: "+filename)
        output.write("\n"+final_analysis)
        
        return True
    
    except:
        return False
