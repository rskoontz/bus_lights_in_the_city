#!/usr/bin/env python3

import json
import urllib.request

class get_bus_data(object):

    def get_data_from_api(self):
        url = "http://api.511.org/transit/StopMonitoring?api_key={api-key-ommited}&agency=SF"
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = response.read()
        values = json.loads(data)

        #print(type(values['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']))



        for bus_stop in values['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
           print(bus_stop['MonitoredVehicleJourney']['LineRef'], 
           bus_stop['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'],
           bus_stop['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'])






        #print(values['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit'][0]['MonitoredVehicleJourney'])


        #def getTargetIds(jsonData):
            #data = json.loads(jsonData)
            #for dest in data['to']['data']:
            #print("to_id:", dest.get('id', 'null'))


def main():
    get_bus_data().get_data_from_api()

if __name__ == "__main__":
    main()
