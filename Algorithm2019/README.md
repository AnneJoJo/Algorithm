# Algorithm Patterns (Interview-Ready)

🎯 Goal: Organize algorithms into **4 hierarchical layers** — from abstract to concrete — and place my **8 core modules** inside.  
This way, I can review concepts top-down before interviews: start from strategies, then recall paradigms, and finally match problem families.

---

## Knowledge Hierarchy

1. **Data Structures (Structures)** → provide operations (stack / queue / heap / tree / graph / hash)  
2. **Strategies** → abstract methods to explore or solve (BFS, DFS, DP, Greedy, Divide & Conquer)  
3. **Paradigms (Patterns)** → reusable solution templates (Sliding Window, Prefix Sum + HashMap, Monotonic Stack, Binary Search)  
4. **Problem Families** → high-frequency categories (Intervals, Shortest Path, LRU Cache, etc.)

> Workflow for interviews:  
> **Identify the layer → recall the strategy/paradigm → map to the problem family.**

---

## My 8 Core Modules

### 🧱 Data Structures (Structures)
*(kept separate in `data_structures/` — not mixed with algorithms)*

### 🌀 Strategies
- **BFS** – level order traversal, unweighted shortest path, multi-source expansion  
- **DFS / Backtracking** – recursion, exhaustive search, state generation  
- **Dynamic Programming (DP)** – divide into subproblems, recurrence + memoization/tabulation  

### 🎯 Paradigms (Patterns)
- **Sliding Window** – variable-length subarray/substring, two-pointers  
- **Prefix Sum + HashMap** – range sums, subarray equals K, frequency tracking  
- **Monotonic Stack** – next greater/smaller element, histogram, stock span  
- **Binary Search / Search on Answer** – sorted arrays, monotone predicate, answer space search  

### 📂 Problem Families
- **Intervals** – merge intervals, meeting rooms, scanning line extensions  

---

## Module Entry Points

### 🌀 Strategies

**1️⃣ BFS**  
- *Essence*: explore by levels using `queue + visited`.  
- *Applications*: unweighted shortest path, multi-source diffusion, level order traversal.  
- *Template*: [BFS template](algorithms/01-bfs/README.md)

**2️⃣ DFS / Backtracking**  
- *Essence*: recursive deep search with backtracking.  
- *Applications*: subsets, permutations, graph connectivity.  
- *Template*: [DFS/Backtracking template](algorithms/02-dfs/README.md)

**3️⃣ Dynamic Programming (DP)**  
- *Essence*: break down into overlapping subproblems.  
- *Applications*: knapsack, subsequences, edit distance, LIS.  
- *Template*: [DP templates](algorithms/03-dp/README.md)

---

### 🎯 Paradigms

**4️⃣ Sliding Window**  
- *Essence*: expand `right`, shrink `left` when condition holds.  
- *Applications*: longest/shortest substrings, anagrams, at-most/at-least K distinct.  
- *Template*: [Sliding Window template](algorithms/04-sliding-window/README.md)

**5️⃣ Prefix Sum + HashMap**  
- *Essence*: `pre[i] - pre[j] = target` tracked with a hashmap.  
- *Applications*: subarray sum equals K, parity/even-odd, continuous sum multiple of K.  
- *Template*: [Prefix Sum template](algorithms/05-prefix-hash/README.md)

**6️⃣ Monotonic Stack**  
- *Essence*: stack maintains increasing/decreasing order.  
- *Applications*: next greater element, daily temperatures, largest rectangle in histogram.  
- *Template*: [Monotonic Stack template](algorithms/06-monotonic-stack/README.md)

**7️⃣ Binary Search / Search on Answer**  
- *Essence*: search on sorted data or feasible answer space.  
- *Applications*: find min capacity, rotated array search, split array largest sum.  
- *Template*: [Binary Search template](algorithms/07-binary-search/README.md)

---

### 📂 Problem Families

**8️⃣ Intervals**  
- *Essence*: sort by start/end, then merge or count overlaps.  
- *Applications*: merge intervals, meeting rooms II, insert interval, scanning line.  
- *Template*: [Interval problems](algorithms/08-intervals/README.md)

---

## Checklists

- **Daily Warm-Up** (`checklists/daily-warmup.md`): pick 1 module → read checklist → re-implement template → 1 mini exercise.  
- **Pre-Interview 10min** (`checklists/pre-interview-10min.md`): skim 8 templates, re-code 2 weak spots, calm breathing.  

---

⚡ With this hierarchy, the repo becomes:  
- **Algorithms (this folder)** → abstract strategies, paradigms, problem families.  
- **Data Structures** → separate toolbox of implementations.  
- **Checklists** → daily/weekly habits and pre-interview skim routines.

