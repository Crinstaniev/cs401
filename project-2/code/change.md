- TEST 1: Replica number from 1 to 5
    - LOGFILE: [modify_replica_num.json](./result/modify_replica_num.json)
- TEST 2: Update code, print response status: "online!" instead of "online"
    - LOGFILE: [update_code.json](./result/update_code.json)
- TEST 3: Data update, bump data version from 1 to 2
    - LOGFILE: [update_data.json](./result/update_data.json)

using python, draw a line. When the status is online, make the segment green. When it is not, make it red. And mark where the status change. The status is from a json file, here is a sample:
{"model_date": "2023-02-22 00:10:29", "status": "online", "time": "2023-02-22 00:12:23", "version": "1.0.0"}
{"model_date": "2023-02-22 00:10:29", "status": "online", "time": "2023-02-22 00:12:24", "version": "1.0.0"}
{"model_date": "2023-02-22 00:10:29", "status": "online", "time": "2023-02-22 00:12:25", "version": "1.0.0"}
{"model_date": "2023-02-22 00:10:29", "status": "online", "time": "2023-02-22 00:12:26", "version": "1.0.0"}