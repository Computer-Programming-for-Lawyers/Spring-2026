# **In-Class Activity: Categorizing Congressional Sessions**  

## **Objective**  
In this activity, you will analyze a **pre-processed list of congressional adjournment descriptions** and categorize them into three types:
- **Pro Forma** (brief session with no legislative business)  
- **Not in Session** (did not meet at all)  
- **Other** (neither of above, likely a regular meeting day)  

You will use **for loops, if statements, and dictionaries** to store and count how many days each chamber (House and Senate) falls into each category.  

---

### **Data to Help You Get Started**  

We've provided a few lines of code in `starter.ipynb` to help you get started. That code loads the pre-processed list of adjournment strings into a list called "adjournment_strings".

The first three strings in the list are pasted below for reference:
* The House was not in session today. The House is scheduled to meet in Pro Forma session at 12 p.m. on Thursday January 6 2022.
* The House was not in session today. The House is scheduled to meet in Pro Forma session at 12 p.m. on Thursday January 6 2022.No hearings were held.
* Adjournment: The House met at 12 p.m. and adjourned at 12:09 p.m.


---
**Task: Count how many days fall into each category**  
* Iterate through `adjournment_strings` using a **for loop**.  
* Check if the description contains **"House"** or **"Senate"**.  
* Use **if statements** to determine whether the session was **pro forma, not in session, or other**. Count it as pro forma if the string includes "pro forma", as not in session if the string includes "not in session", and as other for all other categories.
* Store the counts in the dictionary provided.  

## **Expected Output**
```
Senate: {'pro forma': 157, 'not in session': 67, 'other': 237}
House: {'pro forma': 0, 'not in session': 89, 'other': 514}
```

---

## **Optional Advanced Challenge**  

Store the time the session convened and adjourned in a seperate list. You may consult online sources. You would likely need to use regular expression matching and slicing (aka, get 10 characters that follow terms like "convened at" and "adjourned at" and then extract the time from that list of characters.)