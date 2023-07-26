# Artifacts 📜

- [notebooks](notebooks): custom apps to eventstream as realtime feeds
- [pipelines](pipelines): used for loading historical data to backfill and also orchestration of source streams (notebooks custom apps to eventstream as realtime feeds)
- [kql](kql): scripts can be ran over kql db after ingestion tasks started
- [RTA_Live_FlightStreamerNoiseComplaints.pbix](/RTA_Live_FlightStreamerNoiseComplaints.pbix)
  - This Power BI report uses Direct Query over +30TBs (includes the Historical of multiple years and the live stream), you can connect it to your own KQL DB after executing the previous artifacts. It uses the following objects (tables, views, functions) to render several visuals (AllAirport, Altitudes, FlightData10Days, GetAllAirportlataCodes, GetNonCompliantFlightsByAirport, H3Resolution, and TimeResolutions).
  - It mainly renders geo-fences on a map where a plane has flown below a certain altitude. The report contains 3 pages.
  - Start by using the first page "Non Compliant Flights", if the notebook was ran to steam the live data, then filter MyTimeBin by the Last 4hrs or 1hr. You may find one or two call-signs within the geo-fences for JFK international. These are planes that were likely decending or accending around the airport, lets see where they traveled.
  - Copy those call-signs and proceed to the second page "CallSign Tracker". Filter by CallSign, enter the call-sign (case sensitive) into the filter and select it. It should render a tragectory the plane few over a 10s interval collection provided by the live source API from OpenSky. We can see where the path the plane's call sign took for a given TimeStamp.
  -  Proceed to the third page to look at the "CallSign Details". Filter by the same CallSign to see its details. You can look at additional details using the [kql](kql) artifacts QuerySet [RTA-DemoKQLQueries.kql](/artifacts/kql/RTA-DemoKQLQueries.kql).

Create Eventstream(s) & KQL DB using Fabric web-UI. Learn more at: https://aka.ms/fabric-tutorials > multi-experience > [Real-Time Analytics](https://learn.microsoft.com/fabric/real-time-analytics/tutorial-introduction)
