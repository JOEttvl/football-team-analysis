import pandas as pd
import matplotlib.pyplot as plt  #mohammad ibrahim sasa MOHAMMD ibrahim alanaswah


df = pd.read_csv("team_input.csv")  

df["Losses"] = df["Played"] - (df["Wins"] + df["Draws"])


teams = ["Real Madrid", "Barcelona", "Man City", "Bayern", "Liverpool"]
played = 10


wins_list = []
draws_list = []
losses_list = []
gf_list = []
ga_list = []




print("Basic Statistics:")
print(df.describe())


for team in teams:
    print("Enter stats for", team)
    wins = int(input("Wins: "))
    draws = int(input("Draws: "))
    losses = played - (wins + draws)
    gf = int(input("Goals For: "))
    ga = int(input("Goals Against: "))
    
    wins_list.append(wins)
    draws_list.append(draws)
    losses_list.append(losses)
    gf_list.append(gf)
    ga_list.append(ga)
    print()


data = {
    "Team": teams,
    "Played": [played] * len(teams),
    "Wins": wins_list,
    "Draws": draws_list,
    "Losses": losses_list,
    "GF": gf_list,
    "GA": ga_list
}

df = pd.DataFrame(data)


df["Points"] = df["Wins"] * 3 + df["Draws"]
df["GD"] = df["GF"] - df["GA"]


total_GF = sum(df["GF"])
total_GA = sum(df["GA"])


attack_percentages = [(goals / total_GF) * 100 for goals in df["GF"]]
df["Attack %"] = attack_percentages

defense_percentages = [(goals_against / total_GA) * 100 for goals_against in df["GA"]]
df["Defense %"] = defense_percentages


df = df.sort_values(by="Points", ascending=False).reset_index(drop=True)


print("\nFinal Stats:\n")
print(df[["Team", "Points", "GD", "Attack %", "Defense %"]])
print("\nTop team is:", df.iloc[0]["Team"], "\n")


for i in range(len(df)):
    team = df.loc[i, "Team"]
    atk = df.loc[i, "Attack %"]
    if atk > 20:
        atk_text = "has strong attack"
    elif atk > 15:
        atk_text = "has decent attack"
    else:
        atk_text = "has weak attack"

    defn = df.loc[i, "Defense %"]
    if defn < 20:
        defn_text = "strong defense"
    elif defn < 23:
        defn_text = "average defense"
    else:
        defn_text = "weak defense"

    print(f"{team} {atk_text} and {defn_text} ({round(defn, 2)}%)")


df.to_csv("team_stats.csv", index=False)

plt.hist(df["GF"], bins=5, color='green')
plt.title("Distribution of Goals For")
plt.xlabel("Goals")
plt.ylabel("Frequency")
plt.show()



plt.bar(df["Team"], df["GF"], color='skyblue')
plt.title("Goals For")
plt.ylabel("Goals")
plt.show()


plt.bar(df["Team"], df["Attack %"], color='orange')
plt.title("Attack %")
plt.ylabel("Attack %")
plt.show()


plt.bar(df["Team"], df["Defense %"], color='red')
plt.title("Defense % (Lower is Better)")
plt.ylabel("Defense %")
plt.show()