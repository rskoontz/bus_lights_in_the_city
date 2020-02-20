#!/usr/bin/env python3

import json
import requests
import urllib

class get_bus_data(object):

    def get_data_from_api(self):
        r = requests.get('http://api.511.org/transit/StopMonitoring?api_key={omni-api-key}')
        data = r.json()        
        
        for items in data['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
            r = requests.get('http://api.511.org/transit/StopMonitoring?api_key={omit-api-key}')
            #data = json.loads(r.text())
            data = r.json()
            r.encoding='utf-8-sig'
            bus_stop_ref = items['MonitoredVehicleJourney']['DestinationRef']
            bus_stop_direction = items['MonitoredVehicleJourney']['DirectionRef']

            return(bus_stop_ref, bus_stop_direction)

        #for bus_stop in values['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit']:
        #   print(bus_stop['MonitoredVehicleJourney']['LineRef'], 
        #   bus_stop['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'],
        #   bus_stop['MonitoredVehicleJourney']['MonitoredCall']['ExpectedArrivalTime'])
        #print(values['ServiceDelivery']['StopMonitoringDelivery']['MonitoredStopVisit'][0]['MonitoredVehicleJourney'])
def main():
    get_bus_data().get_data_from_api()

if __name__ == "__main__":
    main()
