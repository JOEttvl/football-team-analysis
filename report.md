
# Football Team Analysis Report

## Project Overview
This project analyzes the performance of various football teams using Python, pandas, and matplotlib. The goal is to calculate key metrics such as points, goal difference, attack percentage, and defense percentage, and to visualize the data to gain insights into team performance.

## Methodology
1. **Data Loading**: The data is loaded from a CSV file (`team_input.csv`) containing the teams' statistics.
2. **Data Cleaning**: Losses are calculated based on the number of played matches.
3. **Calculations**:
   - Points: Calculated as `Wins * 3 + Draws`
   - Goal Difference (GD): Calculated as `Goals For (GF) - Goals Against (GA)`
   - Attack Percentage: Calculated as `(GF / Total GF) * 100`
   - Defense Percentage: Calculated as `(GA / Total GA) * 100`
4. **Sorting**: Teams are sorted by points in descending order.
5. **Visualization**: Various plots are generated to visualize the data.

## Key Findings
- **Top Team**: The team with the highest points is identified.
- **Strongest Attack**: Teams with the highest attack percentage are highlighted.
- **Best Defense**: Teams with the lowest defense percentage are highlighted.

## Visualizations
### Distribution of Goals For
![Goals For](goals_for.png)

### Points Distribution
![Points Distribution](points_distribution.png)

### Attack Percentage
![Attack Percentage](attack_percentage.png)

### Defense Percentage
![Defense Percentage](defense_percentage.png)

## Conclusion
This analysis provides valuable insights into the performance of football teams. By examining key metrics and visualizing the data, we can identify the strengths and weaknesses of each team. This information can be used by coaches, analysts, and fans to make informed decisions and improve team performance.

