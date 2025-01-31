## General Tasks

### Task 1: Identifying an Object Ross is Holding in a Friends Scene

```xml
You are an AI assistant analyzing a scene from the TV show *Friends*. Identify the object Ross is holding in the given video clip.

<Input> {$Video} </Input>

<Description> A 6-second clip from *Friends* where Ross is standing in Monica’s apartment, talking to Rachel. </Description>

<Output_Format>  
    - Object Detected: [Specify the object Ross is holding]  
    - Timestamp: [Time when the object is clearly visible]  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:01 - 00:02 → Ross picks up a coffee mug from the table.  
        00:03 - 00:05 → He gestures with the mug while talking to Rachel.  
    Object Detected: Coffee Mug  
    Timestamp: 00:02  
</Expected_Output>
```

### Task 2: Counting People in a Short Elevator Surveillance Clip

```xml
You are an AI assistant monitoring foot traffic in an elevator. Analyze the video and count the number of people at each timestamp.  

<Input> {$Video} </Input>

<Description> A 7-second video of people entering and exiting an elevator. </Description>

<Output_Format>
    - Video Summary: A breakdown of people entering and exiting the elevator, with timestamps.
    - Key Actions: People entering, exiting, and remaining.
    - Final Count: [Number] people remaining inside the elevator.
    - Timestamp Breakdown: A detailed count of people entering and exiting at specific times.
</Output_Format>

<Expected_Output>
    Video Summary: 
     00:01 - 00:02 → 2 people enter the elevator.  
     00:03 - 00:04 → 1 person enters the elevator.  
     00:05 - 00:06 → 1 person exits the elevator.  
     00:06 - 00:07 → 1 more person exits the elevator.  
    Key Actions:
    - People Entered: 3 
    - People Exited: 2 
    - Final Count: 1 person remained in the elevator.
</Expected_Output>
```

### Task 3: Identifying Workout Exercise and Counting Repetitions

```xml
You are an AI fitness assistant analyzing workout movements. Identify the exercise being performed and count repetitions.  

<Input> {$Video} </Input>

<Description> A 6-second clip of a person performing a push-up. </Description>

<Output_Format> 
    - Exercise Detected: [Push-up/Squat/etc.]
    - Rep Count: [Number]
    - Timestamp Breakdown: Detailed times for each rep.
</Output_Format>

<Expected_Output> 
    Video Summary:  
     00:01 - 00:03 → Rep 1: Person lowers and raises their body.  
     00:03 - 00:06 → Rep 2: Person lowers and raises their body.
    Exercise Detected: Push-up  
    Rep Count: 2  
</Expected_Output>
```

### Task 4: Identifying If a Baby Took Their First Steps
Detect whether the baby took steps, how many, and when each action happened.

```xml
You are an AI childcare assistant analyzing movement. Identify and describe the sequence of events in the video with timestamps.

<Input> {$Video} </Input>

<Description> A 6-second video of a baby standing and attempting to walk. </Description>

<Output_Format>
    - Video Summary: A step-by-step breakdown of what happens in the video, with exact timestamps.
    - Key Actions: Baby detected, standing, stepping, balance loss, sitting.
    - Total Steps Taken: [Number]
    - First Step Time: [Timestamp]
    - Last Step Time: [Timestamp]
</Output_Format>

<Expected_Output>
    Video Summary: 
    00:00.0 - 00:01.2 → Baby is standing still, slightly shifting weight.  
    00:01.3 - 00:02.0 → Baby moves one foot forward cautiously.  
    00:02.1 - 00:02.9 → Baby takes a second step, appearing more confident.  
    00:03.0 - 00:03.8 → Baby takes a third step but wobbles slightly.  
    00:03.9 - 00:04.5 → Baby lifts foot for a fourth step but stumbles.  
    00:04.6 - 00:05.2 → Baby tries to regain balance but starts falling.  
    00:05.3 - 00:06.0 → Baby sits down on the floor safely.  

    Key Actions:
    - Baby detected
    - Steps Taken: 3 successful, 1 attempt before falling
    - First Step Time: 00:01.3  
    - Last Step Time: 00:03.9
    - Fall Detected: Yes, at 00:04.6 
    - Sitting Time: 00:05.3
</Expected_Output>
```

### Task 5: Identifying the Toy

```xml
You are an AI child behavior analysis assistant. Your task is to identify the toy the child is interacting with in a short video clip. Provide timestamps.

<Input> {$Video} </Input>

<Description> A 6-second video captures a child interacting with toys. </Description>

<Output_Format>  
    - Toy Identified: [Name of the toy]  
    - Timestamps: Mention when the toy is visible.  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:01 - 00:03 → Toy identified: Teddy Bear  
        00:04 - 00:06 → Toy identified: Red Ball  
</Expected_Output>
```

### Task 6: Identifying Fan Status Change

```xml
You are an AI home automation assistant analyzing electrical appliance status. Identify whether the ceiling fan was turned on or off based on the video.

<Input> {$Video} </Input>

<Description> A 5-second video shows a ceiling fan before and after a switch is pressed. </Description>

<Output_Format>  
    - Initial Fan Status: [On/Off]  
    - Action Detected: [Switch Pressed/No Action]  
    - Final Fan Status: [On/Off]  
    - Timestamps: Indicate when the fan status changes.  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:00 - 00:02 → Fan is Off  
        00:03 → Switch Pressed  
        00:04 - 00:05 → Fan is On  
</Expected_Output>
```

### Task 7: Identifying Door Status in a Home Security Video

```xml
You are an AI home security assistant analyzing short surveillance footage. Identify whether the door was closed or left open after the person exited the room.

<Input> {$Video} </Input>

<Description> A 7-second home security video captures a person leaving a room. </Description>

<Output_Format>  
    - Person Detected: [Yes/No]  
    - Exit Timestamp: [Time when the person left the room]  
    - Door Status After Exit: [Closed/Open]  
    - Timestamps: Indicate the moment the door was last seen moving.  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:00 - 00:04 → Person walking toward the door  
        00:05 → Person exits the room  
        00:06 - 00:07 → Door remains open  
    Final Door Status: Open  
</Expected_Output>
```