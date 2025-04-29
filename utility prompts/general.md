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

### Task 8: Detecting a Dropped Object

```xml
You are an AI assistant analyzing a video to detect when and what object is dropped.  

<Input> {$Video} </Input>

<Description> A 5-second video shows a person holding an object, which accidentally falls. </Description>

<Output_Format>  
    - Object Dropped: [Specify the object]  
    - Drop Timestamp: [Time when the object falls]  
    - Impact Timestamp: [Time when the object hits the ground]  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:01 → Person accidentally drops a mobile phone.  
        00:02 → Phone hits the ground.  
    Object Dropped: Mobile Phone  
    Drop Timestamp: 00:01  
    Impact Timestamp: 00:02  
</Expected_Output>
```
### Task 9: Detecting a Light Turning On or Off

```xml
You are an AI home automation assistant analyzing a video for changes in lighting conditions.  

<Input> {$Video} </Input>

<Description> A 5-second home surveillance video capturing a room with a light source. </Description>

<Output_Format>  
    - Initial Light Status: [On/Off]  
    - Action Detected: [Switch Pressed/No Action]  
    - Final Light Status: [On/Off]  
    - Timestamps: Mention when the change occurred.  
</Output_Format>

<Expected_Output>  
    Video Summary:  
        00:00 - 00:02 → Room is dark (Light Off).  
        00:03 → Switch Pressed.  
        00:04 - 00:05 → Room is bright (Light On).  
    Initial Light Status: Off  
    Action Detected: Switch Pressed  
    Final Light Status: On  
</Expected_Output>
```
### Task 10: Understanding Causality 

```xml
<Input> {$Video} </Input>

<Description> A person spills water on the floor, then another person slips and falls. </Description>

<Question> Why did the person fall? </Question>

<Output_Format>  
    - Answer: [Short Explanation]  
</Output_Format>

<Expected_Output>  
    Answer: The person slipped because water was spilled on the floor.  
</Expected_Output>
```

### Task 11: Tracking fast moving objects

```xml
<Input> {$Video} </Input>

<Description> A magician moves a ball between three cups very quickly. </Description>

<Question> Where is the ball now? </Question>

<Output_Format>  
    - Answer: [Cup Position]  
</Output_Format>

<Expected_Output>  
    Answer: Under the middle cup  
</Expected_Output>
```

### Taks 12: Multiple People Interaction

```xml
<Input> {$Video} </Input>

<Description> A person hands a book to another person, who puts it on a shelf. </Description>

<Question> Who placed the book on the shelf? </Question>

<Output_Format>  
    - Answer: [Person A/Person B]  
</Output_Format>

<Expected_Output>  
    Answer: Person B  
</Expected_Output>
```

### Task 13: Detecting Actions in Crowded Scenes

```xml
<Input> {$Video} </Input>

<Description> A person in a red shirt picks up a bag in a crowded market. </Description>

<Question> What did the person in the red shirt do? </Question>

<Output_Format>  
    - Answer: [Action Description]  
</Output_Format>

<Expected_Output>  
    Answer: Picked up a bag.  
</Expected_Output>
```

### Task 14: Missing ingredients in cooking

```xml
<Input> {$Video} </Input>

<Description> A person prepares a cup of coffee by adding hot water to a cup, followed by sugar and stirring. However, no coffee powder was added. </Description>

<Question> Is any ingredient missing from the coffee preparation? </Question>

<Output_Format>  
    - Answer: [Yes/No]  
    - Missing_Ingredient: [Ingredient Name]  
</Output_Format>

<Expected_Output>  
    Answer: Yes  
    Missing_Ingredient: Coffee powder  
</Expected_Output>
```

### Task 15: Identifying the First Object to Fall in a Chain Reaction

```xml
<Input> {$Video} </Input>

<Description> A domino setup where multiple objects (a ball, a book, and a bottle) are involved. A book falls first, hitting a ball, which then knocks over a bottle. </Description>

<Question> Which object fell first? </Question>

<Output_Format>
    - Answer: [Object Name]  
    - Timestamp: [Time when the object fell]  
</Output_Format>

<Expected_Output>  
    Answer: Book  
    Timestamp: 00:02  
</Expected_Output>
```

### Task 16: Who Dropped the Wallet?

```xml
<Input> {$Video} </Input>

<Description> Person A walks from left to right. A wallet falls. Person B, walking in the opposite direction, picks it up. </Description>

<Question> Who dropped the wallet? </Question>

<Output_Format>  
    - Answer: [Person Description]  
</Output_Format>

<Expected_Output>  
    Answer: Person A  
</Expected_Output>
```

### Task 17: Who Scored the Goal?

```xml
<Input> {$Video} </Input>

<Description> Two players attempt to score a goal. The ball deflects and goes in. </Description>

<Question> Who scored the goal? </Question>

<Expected_Output> The last player to touch the ball. </Expected_Output>
```

### Task 18: Identical Twins Switching Places

```xml
<Input> {$Video} </Input>

<Description> Two identical twins are talking. One leaves, and the other takes their place. </Description>

<Question> Is this the same person as before? </Question>

<Expected_Output> "No, they switched." </Expected_Output>
```

### Task 19: Who Crossed the Finish Line First?

```xml
<Input> {$Video} </Input>

<Description> Three runners approach the finish line. They cross at nearly the same time. </Description>

<Question> Who won the race? </Question>

<Expected_Output> "The runner whose body crossed first." </Expected_Output>
```

### Task 20: Moving a chess coin 
Testing if model is able to identify the coin moved by the player.

### Task 21: Detecting action in crowded scene
Identifying what a person is wearing who got down from the car first.
