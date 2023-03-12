# Week 2 — Distributed Tracing
## Homework

### Video Watched
* Watched [FREE AWS Cloud Project Bootcamp - Update 2023-02-23 Video](https://youtu.be/gQxzMvk6BzM).
* Watched [Week 2 - Live Streamed Video – Honeycomb.io Setup](https://www.youtube.com/live/2GD9xCzRId4?feature=share).
* Watched [Week 2 - Instrument X-Ray Video](https://youtu.be/n2DTsuBrD_A).
* Watched [Week 2 – X-Ray Subsegments Solved Video](https://youtu.be/4SGTW0Db5y0)
* Watched [Week 2 - CloudWatch Logs Video](https://youtu.be/ipdFizZjOF4).
* Watched [Week 2 - Rollbar Video](https://youtu.be/xMBDAb5SEU4).
* Watched [Week 2 – Github Codespaces Crash Course Video](https://youtu.be/L9KKBXgKopA).

### Work Done
#### Honey Comb
* Setup up Honeycomb as per the video
* After alot of tshooting including adding trying to debug to the console , mixing up my branches
Even adding this  code in  and removing it out  I got spans working .
```
# console standard output
simple_processor = SimpleSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(simple_processor)
```
I had somehow missed to copy 
```
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(__name__)
```

![Honeycomb](../_docs/assets/week2/honeycomb_traces.png)

* My dataset got created when Cruddur started talking to honeycomb

![Dataset_Honeycomb](../_docs/assets/week2/dataset_honeycomb.png)

* Added Mock span data !

* I ran a query and check the mock Data
![Query](../_docs/assets/week2/run_query.png)
![Mock_data](../_docs/assets/week2/check_data.png)

#### AWS X-Ray

* Completed all steps to implement AWS X-Ray tracing With subsegments

![Xray_apply](_docs/assets/week2/xray_aws.png)
![Xray](../_docs/assets/week2/xray_subsegment.png)
![Xray](../_docs/assets/week2/xray_traces.png)
![Xray](../_docs/assets/week2/xray_traces.png)
![Xray_servicemap](../_docs/assets/week2/xray_servicemap.png)

#### Cloud watch
* Got Cloudwatch logs to work fairly easy
![Cloudwatch_logs](../_docs/assets/week2/cloudwatchlogs.png)

#### Rollbar
* Got rollbar to send Data after rebooting the gitpod instance as the Rollbar api env did not get set

![Rollbar](../_docs/assets/week2/rollbar.png)