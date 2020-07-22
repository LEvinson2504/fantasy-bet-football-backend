# Roadmap for fantasy bet football

## TODO
1. Transfer the Bets database from Firestore to django(in progress). 
2. Creating endpoints to send json data to the client. 
3. Automated Leaderboard to track scores of players and update when necessary using the data from API, like a cron job.
4. User Login/Signup and sessions and a profile page.

## IMPROVEMENT
1. Clean up client side and make it more reactive, need to read more on it.
2. Cache data in the server so dont require spamming the API

## EXPLORE IDEAS:
1. We have a basic news component now, need to find a better source for better news, maybe news the user will be interested in etc.
2. Display stats of teams. There are several opportunities for this: The api has stats for the past 10 games which would be the easier option. Otherwise collect the data and clean to get the deterministic and relevant stats. Player stats, Top football teams, etc. 
