import requests
import json
from datetime import datetime,date

api_endpoint = "https://mehtagold.dashboard.paralaxiom.in"

username = "diptangsu.burd@gmail.com"

with requests.Session() as s:
    loginInfo = s.post(f"{api_endpoint}/accounts/login/",data={
        "username":f"{username}",
        "password":f"{password}"
    })
    loginRes = loginInfo.json()

    userStatusCheck = s.get(f"{api_endpoint}/reports/user_status/")
    statusInfo = userStatusCheck.json()

    updateTime = s.get(f"{api_endpoint}/reports/get_last_update_time")

    eventHistory = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-20T21:21:57+05:30",
        "end_date":"2022-03-21T21:21:57+05:30",
        "limit":10,
        "offset":0,
        "camera":["all"],
        "status":["all"],
        "objects":["all"]
    })
    eventHistoryRes = eventHistory.json()

    cameraHealth = s.post(f"{api_endpoint}/reports/camera_health/",json={
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30",
        "marking_names": None,
        "critical_status": [
            "Critical"
        ]
    })
    cameraHealthRes = cameraHealth.json()

    nonCriticalHealth = s.post(f"{api_endpoint}/reports/non_critical_health/",json={
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30",
        "marking_names": None,
        "event_types": [
            "distort_detection",
            "light_on_off_detection"
        ]
    })
    nonCriticalRes = nonCriticalHealth.json()

    cameraServiceTime = s.post(f"{api_endpoint}/reports/camera_service/",json={
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30"
    })
    cameraServiceTimeRes = cameraServiceTime.json()

    vastHealth = s.post(f"{api_endpoint}/reports/vast_system_health/",json={
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30",
        "marking_names": None,
        "critical_status": [
            "Critical"
        ],
        "limit": 15,
        "offset": 0
    })
    vastRes = vastHealth.json()

    cameraListForPerson = s.post(f"{api_endpoint}/reports/get_camera_list_for_person/",json={
        "org_id": [1,2],
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30"
    })
    camListRes = cameraListForPerson.json()

    cameraDistortion = s.post(f"{api_endpoint}/reports/camera_distortion/",json={
        "start_date": "2022-03-20T23:17:31+05:30",
        "end_date": "2022-03-21T23:17:31+05:30",
        "limit": 10,
        "event_types": [
            "distort_detection"
        ],
        "offset": 0
    })
    cameraDistortionRes = cameraDistortion.json()


    eventHistoryLimit = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-20T21:21:57+05:30",
        "end_date":"2022-03-21T21:21:57+05:30",
        "limit":30,
        "offset":0,
        "camera":["all"],
        "status":["all"],
        "objects":["all"]
    })
    eventHistoryLimitRes = eventHistoryLimit.json()

    eventHistoryCamName = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-21T19:09:39+05:30",
        "end_date":"2022-03-22T19:09:39+05:30",
        "orgID":[1,2],
        "projectID":[1,2],
        "limit":10,
        "offset":0,
        "camera":["Ground Floor Security"],
        "status":["all"],
        "objects":["all"]
    })
    eventHistoryCamRes = eventHistoryCamName.json()

    eventHistoryAlertLevel = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-21T19:09:39+05:30",
        "end_date":"2022-03-22T19:09:39+05:30",
        "orgID":[1,2],
        "projectID":[1,2],
        "limit":10,
        "offset":0,
        "camera":["all"],
        "status":["Critical"],
        "objects":["all"]
    })
    eventHistoryAlertRes = eventHistoryAlertLevel.json()

    eventHistoryObjects = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-21T19:23:04+05:30",
        "end_date":"2022-03-22T19:23:04+05:30",
        "orgID":[1,2],
        "projectID":[1,2],
        "limit":10,
        "offset":0,
        "camera":["all"],
        "status":["all"],
        "objects":["person"]
    })
    eventHistoryObjectRes = eventHistoryObjects.json()

    eventHistoryDates = s.post(f"{api_endpoint}/reports/event_history_limit/",json={
        "start_date":"2022-03-08T19:23:00+05:30",
        "end_date":"2022-03-17T19:23:00+05:30",
        "orgID":[1,2],
        "projectID":[1,2],
        "limit":10,
        "offset":0,
        "camera":["all"],
        "status":["all"],
        "objects":["all"]
    })
    eventHistoryDatesRes = eventHistoryDates.json()


with open("logs-{}.txt".format(date.today()),"a") as f:
        f.write('\n--------------------------------------\n')
        f.write(f"{datetime.now()}\n")
        json.dump(loginRes,f)

        f.write('\n . \n')
        f.write('\n --Login Status--\n')
        json.dump(statusInfo,f)

        f.write('\n . \n')
        f.write('\n --Event History Limit--\n')
        json.dump(eventHistoryRes,f)

        f.write('\n . \n')
        f.write('\n --Camera Health--\n')
        json.dump(cameraHealthRes,f)

        f.write('\n . \n')
        f.write('\n --Non Critical Health--\n')
        json.dump(nonCriticalRes,f)

        f.write('\n . \n')
        f.write('\n --Camera Service Time--\n')
        json.dump(cameraServiceTimeRes,f)

        f.write('\n . \n')
        f.write('\n --VAST System Health--\n')
        json.dump(vastRes,f)

        f.write('\n . \n')
        f.write('\n --Camera List For Person--\n')
        json.dump(camListRes,f)

        f.write('\n . \n')
        f.write('\n --Camera Distortion--\n')
        json.dump(cameraDistortionRes,f)

        f.write('\n . \n')
        f.write('\n --Event History with Limit Varied--\n')
        json.dump(eventHistoryLimitRes,f)

        f.write('\n . \n')
        f.write('\n --Event History with Camera Name Varied--\n')
        json.dump(eventHistoryLimitRes,f)

        f.write('\n . \n')
        f.write('\n --Event History with Alert Level Varied--\n')
        json.dump(eventHistoryAlertRes,f)

        f.write('\n . \n')
        f.write('\n --Event History with Object Name Varied--\n')
        json.dump(eventHistoryObjectRes,f)

        f.write('\n . \n')
        f.write('\n --Event History with Dates Varied--\n')
        json.dump(eventHistoryDatesRes,f)
        f.write('\n--------------------------------------\n')
