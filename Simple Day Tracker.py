import datetime

# Get today's date
today = datetime.date.today()

# Set your last post date (change this to your last post date)
last_post_date = datetime.date(2024, 2, 10)

# Calculate days since last post
days_since_last_post = (today - last_post_date).days

# Display results
print("GitHub Post Tracker")
print("===================")
print(f"Today: {today}")
print(f"Last post: {last_post_date}")
print(f"Days since last post: {days_since_last_post}")

# Reminder logic
if days_since_last_post == 0:
    print("✅ You posted today! Great job!")
elif days_since_last_post == 1:
    print("✅ You posted yesterday. Keep it up!")
elif days_since_last_post < 7:
    print(f"ℹ️ It's been {days_since_last_post} days since your last post.")
else:
    print(f"🚨 Time to post! It's been {days_since_last_post} days!")