import sqlite3
import pandas as pd
import numpy as np

# Connect to database
conn = sqlite3.connect('gaming.db')

# Load user data with betting stats
query = """
WITH user_stats AS (
    SELECT 
        u.user_id,
        u.username,
        u.country,
        u.age,
        SUM(b.amount) as total_bet,
        COUNT(b.bet_id) as bet_count,
        AVG(b.amount) as avg_bet,
        COUNT(CASE WHEN b.result = 'win' THEN 1 END) as wins
    FROM users u
    LEFT JOIN bets b ON u.user_id = b.user_id
    GROUP BY u.user_id, u.username, u.country, u.age
)
SELECT * FROM user_stats
"""

df = pd.read_sql_query(query, conn)
conn.close()

print("=" * 80)
print("USER SEGMENTATION ANALYSIS")
print("=" * 80)

# Segment users by total bet amount
def segment_user(total_bet):
    if pd.isna(total_bet):
        return 'No Activity'
    elif total_bet >= 150:
        return 'High Value'
    elif total_bet >= 75:
        return 'Medium Value'
    else:
        return 'Low Value'

df['segment'] = df['total_bet'].apply(segment_user)

# Summary by segment
print("\n--- USER SEGMENTS SUMMARY ---")
segment_summary = df.groupby('segment').agg({
    'user_id': 'count',
    'total_bet': ['sum', 'mean'],
    'bet_count': 'mean',
    'avg_bet': 'mean'
}).round(2)

print(segment_summary)

# Detailed breakdown by segment
print("\n--- DETAILED USER BREAKDOWN ---")
for segment in ['High Value', 'Medium Value', 'Low Value']:
    segment_df = df[df['segment'] == segment]
    if len(segment_df) > 0:
        print(f"\n{segment} Users ({len(segment_df)} users):")
        print(segment_df[['username', 'country', 'total_bet', 'bet_count', 'avg_bet', 'wins']].to_string(index=False))

# Key insights
print("\n--- KEY INSIGHTS ---")
high_value = df[df['segment'] == 'High Value']
medium_value = df[df['segment'] == 'Medium Value']
low_value = df[df['segment'] == 'Low Value']

print(f"\nHigh Value Users: {len(high_value)} users generating ${high_value['total_bet'].sum():.2f}")
print(f"Medium Value Users: {len(medium_value)} users generating ${medium_value['total_bet'].sum():.2f}")
print(f"Low Value Users: {len(low_value)} users generating ${low_value['total_bet'].sum():.2f}")

print(f"\nTotal Revenue: ${df['total_bet'].sum():.2f}")
print(f"High Value % of Revenue: {(high_value['total_bet'].sum() / df['total_bet'].sum()) * 100:.1f}%")

print("\n" + "=" * 80)