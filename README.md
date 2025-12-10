📅 GitHub Day Tracker
A simple Python script to help you track your GitHub posting activity and maicntain consistency.

🚀 How It Works
📋 Overview
This script calculates how many days have passed since your last GitHub post and provides friendly reminders to keep you consistent.

⚙️ Setup
Edit the date: Change last_post_date to your actual last post date

python
```
last_post_date = datetime.date(2024, 2, 10)  # ← Change this date!
```
🎯 Usage
Run the script with Python:
bash
```
python Simple Day Tracker.py
```

📊 Sample Output

text

GitHub Post Tracker

===================

Today: 2024-02-15

Last post: 2024-02-10

Days since last post: 5

ℹ️ It's been 5 days since your last post.

🎨 Features

✅ Daily Tracking: Automatically calculates days since last post

🔔 Smart Reminders: Different messages based on activity level

📅 Date Validation: Uses Python's built-in datetime module

🐍 Simple Code: Easy to understand and modify

🛠️ Customization
Want to change the reminder intervals? Modify this section:

python

# Reminder logic - change these numbers as needed
```
if days_since_last_post == 0:

    print("✅ You posted today! Great job!")
    
elif days_since_last_post == 1:

    print("✅ You posted yesterday. Keep it up!")
    
elif days_since_last_post < 7:  # ← Change this value

    print(f"ℹ️ It's been {days_since_last_post} days since your last post.")
    
else:  # ← Change this value

    print(f"🚨 Time to post! It's been {days_since_last_post} days!")
```
💡 Pro Tip
Schedule this script to run daily using:

Windows Task Scheduler 🪟

macOS/Linux crontab 🐧

GitHub Actions (advanced) 🤖

## 📌 Today's Historical Fact
<!-- DAILY_FACT -->
```plaintext
📌 Daily Fact: On December 10, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 09, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 08, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 07, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 06, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 05, history continues to unfold with remarkable events and discoveries.
```
```plaintext
📌 Daily Fact: On December 04, history continues to unfold with remarkable events and discoveries.
```

*✨ This fact updates automatically every day!*
