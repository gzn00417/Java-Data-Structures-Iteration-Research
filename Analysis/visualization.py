# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython


# %%
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

get_ipython().magic("matplotlib inline")


# %%
# 10^9
f, ax = plt.subplots()
ArrayList = pd.read_csv("../csv/ArrayList.csv")
sns.barplot(data=ArrayList)
ax.set_title("ArrayList")


# %%
f, ax = plt.subplots()
sns.lineplot(data=ArrayList)
ax.set_title("ArrayList")
plt.ylim(0.5, 1.0)


# %%
# 10^7
f, ax = plt.subplots()
HashMap = pd.read_csv("../csv/HashMap.csv")
sns.barplot(data=HashMap)
ax.set_title("HashMap")


# %%
f, ax = plt.subplots()
sns.lineplot(data=HashMap)
ax.set_title("HashMap")
plt.ylim(0.3, 0.8)


# %%
# 10^12
f, ax = plt.subplots()
HashSet = pd.read_csv("../csv/HashSet.csv")
sns.barplot(data=HashSet)
ax.set_title("HashSet")


# %%
f, ax = plt.subplots()
sns.lineplot(data=HashSet)
ax.set_title("HashSet")
plt.ylim(2.2, 3.6)


# %%
# 10^5
f, ax = plt.subplots()
LinkedList = pd.read_csv("../csv/LinkedList.csv")
sns.barplot(data=LinkedList)
ax.set_title("LinkedList")


# %%
f, ax = plt.subplots()
sns.lineplot(data=LinkedList)
ax.set_title("LinkedList")
plt.ylim(1.6, 2.2)


# %%
Base = 0

ArrayList /= 10 ** (Base - 8)
ArrayList["Type"] = "ArrayList"  # 8

HashMap /= 10 ** (Base - 7)
HashMap["Type"] = "HashMap"  # 7

HashSet /= 10 ** (Base - 8)
HashSet["Type"] = "HashSet"  # 8

LinkedList /= 10 ** (Base - 8)
LinkedList["Type"] = "LinkedList"  # 8

data = pd.concat([ArrayList, HashMap, HashSet, LinkedList], ignore_index=True).drop(
    ["FOR"], axis=1
)
data[["Explicit_Iteration", "Inner_Iteration"]] = np.log10(
    data[["Explicit_Iteration", "Inner_Iteration"]]
)
data.info()


# %%
f, ax = plt.subplots()
sns.barplot(x="Type", y="Explicit_Iteration", data=data)
ax.set_title("Explicit_Iteration")


# %%
f, ax = plt.subplots()
sns.barplot(x="Type", y="Inner_Iteration", data=data)
ax.set_title("Inner_Iteration")


# %%
