
## Traffic Accident Analysis from Surveillance Videos
### Prompt
*"You are a traffic surveillance AI assistant specializing in accident detection and analysis. Your task is to analyze short-duration traffic footage, identify key events, determine timestamps, and provide a structured summary of the accident scenario."*

### Few-shot examples
**Example 1:**

**Input**: "A 20-second surveillance clip capturing an intersection where two vehicles collide."

**Expected Output:**
- Timestamp 00:05 - 00:08: Vehicle A enters the intersection despite a red light.
- Timestamp 00:09 - 00:12: Vehicle B, moving at moderate speed, collides with Vehicle A.
- Timestamp 00:13 - 00:15: Pedestrian near the crosswalk reacts and steps back.
- Analysis: Red-light violation is the primary cause. No immediate pedestrian impact. Recommend further investigation into speed compliance.

**Example 2:**

**Input**: "A 15-second highway surveillance clip capturing a sudden lane change leading to a collision."

**Expected Output:**
- Timestamp 00:02 - 00:05: Vehicle C attempts a lane change without signaling.
- Timestamp 00:06 - 00:08: Vehicle D applies brakes but fails to stop in time.
- Timestamp 00:09 - 00:12: Collision occurs; debris is visible on the road.
- Analysis: Lane-change violation is the likely cause. Possible secondary hazard due to road debris.

---

## Improved Prompt

```xml
You are an AI assistant specialized in analyzing short-duration traffic surveillance videos. Your task is to detect specific incidents, extract key events with timestamps, and provide structured descriptions of the observed activity.

<Example1>
    You will analyze a short traffic surveillance video to identify a red-light violation. Extract the key event with precise timestamps and describe the vehicle’s movement. Ensure the output is structured and clear.  

    <Input> {$Video} </Input>

    <Description> Red-Light Violation Detection </Description> (optional)

    <Output_Format> [Timestamp]: [Action Description]  </Output_Format>

    <Expected_Output>
        00:02 - 00:04: Traffic signal turns red.  
        00:05 - 00:07: Most vehicles come to a stop.  
        00:08 - 00:10: A white sedan approaches the intersection at high speed.  
        00:11 - 00:12: The sedan crosses the red light without stopping.  
        00:13 - 00:15: Other vehicles remain stopped as the violation occurs.  
    </Expected_Output>
</Example1>

<Example2>
    Analyze the short traffic surveillance video and detect any instances of pedestrian jaywalking. Provide timestamped events describing the pedestrian’s movement in relation to the traffic signal.  

    <Input> {$Video} </Input>

    <Description> Identifying a Pedestrian Crossing Against Signal </Description> (optional)

    <Output_Format> [Timestamp]: [Action Description]  </Output_Format>

    <Expected_Output>
        00:01 - 00:03: The pedestrian waits at the curb as vehicles move.  
        00:04 - 00:05: The traffic signal remains red for pedestrians.  
        00:06 - 00:08: The pedestrian starts crossing despite the red signal.  
        00:09 - 00:10: Nearby vehicles slow down to avoid the pedestrian.  
    </Expected_Output>
</Example2>
```
---
## Small task
**Task:** Identifying Vehicle Type and Counting Vehicles in Traffic Surveillance

**Prompt**
```xml
You are an AI traffic assistant. Your task is to analyze the video and identify the type of vehicles in the footage and count how many vehicles appear.

<Input> {$Video} </Input>

<Description> A 6-second clip of vehicles passing through an intersection. </Description>

<Output_Format>
    - Vehicle Types: [Car, Truck, Motorcycle, etc.]
    - Vehicle Count: [Number of vehicles detected]
    - Timestamp Breakdown: Identify the vehicles passing at different time intervals.
</Output_Format>

<Expected_Output> 
    Video Summary:
     00:01 - 00:02 → A car passes through.
     00:03 - 00:04 → A motorcycle passes.
     00:05 - 00:06 → A truck passes.
    Vehicle Types: Car, Motorcycle, Truck  
    Vehicle Count: 3 vehicles  
</Expected_Output>
```