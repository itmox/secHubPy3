
def selectOps(form):
    selectedScans = {}
    if "restapi" in form:
        selectedScans['restapi'] = 1
    else: selectedScans['restapi'] = 0

    if "webscan" in form:
        selectedScans['webAppScan'] = 1
    else: selectedScans['webAppScan'] = 0

    if "nmap" in form:
        selectedScans['nmap'] = 1
    else: selectedScans['nmap'] = 0

    if "element_8_4" in form:
        selectedScans['wfuzz'] = 1
    else: selectedScans['wfuzz'] = 0

    if "element_8_5" in form:
        selectedScans['vier'] = 1
    else: selectedScans['vier'] = 0

    if "element_8_6" in form:
        selectedScans['fuenf'] = 1
    else: selectedScans['fuenf'] = 0

    return selectedScans

def appInfo(form):
    info = {}
    if "app" in form:
        info['app'] = form["element_1"]
    else:
        info['app'] = ""

    if "url" in form:
        info['url'] = form["url"]
    else:
        info['url'] = ""

    if "requestor_mail" in form:
        info['req_mail'] = form["requestor_mail"]
    else:
        info['req_mail'] = ""

    if "env" in form:
        info['environment'] = form["env"]
    else:
        info['environment'] = ""

    if "reason" in form:
        info['reason'] = form["reason"]
    else:
        info['reason'] = ""

    if "owner" in form:
        info['owner'] = form["owner"]
    else:
        info['owner'] = ""

    if "info" in form:
        info['add_info'] = form["info"]
    else:
        info['add_info'] = ""

    return info