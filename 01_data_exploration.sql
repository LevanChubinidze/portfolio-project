-- PORTFOLIO PROJECT: Gaming User Behavior Analysis

-- ============================================================
-- Exercise 1: Data Exploration & User Segmentation
-- ============================================================

-- Step 1: Overview of the gaming dataset
SELECT 
    'Users' as table_name,
    COUNT(*) as record_count
FROM users
UNION ALL
SELECT 'Bets', COUNT(*) FROM bets
UNION ALL
SELECT 'Sessions', COUNT(*) FROM sessions;

-- Step 2: User Demographics & Activity
SELECT 
    u.user_id,
    u.username,
    u.country,
    u.age,
    COUNT(DISTINCT b.bet_id) as total_bets,
    SUM(b.amount) as total_amount_bet,
    AVG(b.amount) as avg_bet,
    COUNT(DISTINCT CASE WHEN b.result = 'win' THEN 1 END) as wins,
    ROUND(100.0 * COUNT(DISTINCT CASE WHEN b.result = 'win' THEN 1 END) / 
          COUNT(DISTINCT b.bet_id), 1) as win_rate_percent,
    COUNT(DISTINCT s.session_id) as total_sessions
FROM users u
LEFT JOIN bets b ON u.user_id = b.user_id
LEFT JOIN sessions s ON u.user_id = s.user_id
GROUP BY u.user_id, u.username, u.country, u.age
ORDER BY total_amount_bet DESC;

-- Step 3: User Segmentation (High/Medium/Low Value)
WITH user_stats AS (
    SELECT 
        u.user_id,
        u.username,
        u.country,
        SUM(b.amount) as total_bet,
        COUNT(b.bet_id) as bet_count,
        AVG(b.amount) as avg_bet
    FROM users u
    LEFT JOIN bets b ON u.user_id = b.user_id
    GROUP BY u.user_id, u.username, u.country
)
SELECT 
    user_id,
    username,
    country,
    total_bet,
    bet_count,
    avg_bet,
    CASE 
        WHEN total_bet >= 150 THEN 'High Value'
        WHEN total_bet >= 75 THEN 'Medium Value'
        ELSE 'Low Value'
    END as user_segment
FROM user_stats
ORDER BY total_bet DESC;

-- Step 4: Game Performance Analysis
SELECT 
    game,
    COUNT(*) as bets_placed,
    SUM(amount) as total_wagered,
    AVG(amount) as avg_bet,
    COUNT(CASE WHEN result = 'win' THEN 1 END) as wins,
    ROUND(100.0 * COUNT(CASE WHEN result = 'win' THEN 1 END) / COUNT(*), 1) as win_rate_percent
FROM bets
GROUP BY game
ORDER BY total_wagered DESC;