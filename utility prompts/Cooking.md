## Prompt

```xml
You will watch a short cooking video and generate structured step-by-step instructions. For each action, include the timestamp range and a brief description. Ensure the extracted steps are sequential and relevant.  

<Input> {$Video_1}  </Input>

<Description> Making an Omelette </Description> (optional)

<Output_Format> [Timestamp]: [Action Description] </Output_Format>

<Expected_Output>:
    00:02 - 00:05: Crack two eggs into a bowl.  
    00:06 - 00:09: Whisk the eggs until fully blended.  
    00:10 - 00:13: Heat a pan and add butter.  
    00:14 - 00:18: Pour the egg mixture into the pan.  
    00:19 - 00:24: Stir gently until the eggs begin to set.  
    00:25 - 00:28: Fold the omelette and remove from heat.  
    00:29 - 00:30: Serve on a plate. 
</Expected_output>
```


---------------

## 1️⃣ Action Detection in Cooking Videos
### Prompt:
*"Identify the key cooking actions in the video and provide approximate timestamps for each step."*

**Example Output:**
- 00:02 - 00:06: Chopping onions
- 00:07 - 00:12: Heating oil in the pan
- 00:13 - 00:17: Adding tomatoes
- 00:18 - 00:22: Stirring the mixture

---

## 2️⃣ Frame-Based Action Segmentation
### Prompt:
*"Segment the video into frames and detect actions occurring in each frame along with their timestamps."*

**Example Output:**
| Start Time | End Time | Action Description |
|------------|---------|--------------------|
| 00:00 | 00:04 | Gathering ingredients |
| 00:05 | 00:09 | Chopping vegetables |
| 00:10 | 00:14 | Heating oil in pan |
| 00:15 | 00:19 | Sauteing onions |
| 00:20 | 00:24 | Stirring sauce |

---

## 3️⃣ Sequential Reasoning Across Frames
### Prompt:
*"Analyze the sequence of cooking actions across frames and describe their logical progression."*

**Example Output:**
- Step 1: User chops vegetables.
- Step 2: User heats oil in a pan.
- Step 3: User sautes onions.
- Step 4: User adds tomatoes.

---

## 4️⃣ Action Transition Detection
### Prompt:
*"Identify key transitions between cooking actions and provide timestamps where a change occurs."*

**Example Output:**
- 00:04: Transition from chopping onions to heating oil
- 00:09: Transition from heating oil to sauteing onions
- 00:14: Transition from sauteing onions to adding spices

---

## 5️⃣ Missing Step Detection
### Prompt:
*"Analyze the cooking process and identify if any essential step is missing."*

**Example Output:**
The step of preheating the pan before adding oil is missing, which may lead to uneven cooking.

---

## 6️⃣ Real-Time Cooking Action Tracking
### Prompt:
*"Continuously monitor the video and provide real-time action detection with timestamps."*

**Example Output (Live Updates):**
- "00:00 - 00:04 → The user is washing vegetables."
- "00:05 - 00:09 → The user is chopping carrots."
- "00:10 - 00:14 → The user is stirring soup in the pot."

