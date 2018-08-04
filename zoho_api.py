from __future__ import with_statement
from ReportClient import ReportClient
import sys
import random
import datetime
import time

while True:
    for machine in range(1, 4):
        m = machine
        p = random.sample(range(2, 25), 1)
        s = random.sample(range(1, 9), 1)
        t = datetime.datetime.now()
        print t
# #

        class Sample:

            LOGINEMAILID = "abc@gmail.com"
            AUTHTOKEN = "**********************"
            DATABASENAME = "api_test4"
            TABLENAME = "testing"
            rc = None
            rc = ReportClient(AUTHTOKEN)

            def AddRow(self, rc):
                # for machine in range(0, 6):
                #     m = machine
                #     p = random.sample(range(1, 30), 1)
                #     s = random.sample(range(1, 30), 1)
                uri = rc.getURI(self.LOGINEMAILID,
                                self.DATABASENAME, self.TABLENAME)
                rowData = {"time": t, "machine": m,
                           "pieces": p[0], "stops": s[0]}
                result = rc.addRow(uri, rowData, None)
                print result
        time.sleep(30)
        obj = Sample()
        obj.AddRow(obj.rc)
