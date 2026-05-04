# Project Specification: Stochastic Train Route Optimization (STRO)

## 1. Environment Configuration
The environment is defined as a discrete 2D grid of dimensions $R \times C$, where $R$ represents the number of rows and $C$ the number of columns. Each vertex $V_{i,j}$ represents a geographical node within a city.

### 1.1 Dynamic Population Model
Each node $V_{i,j}$ contains a stochastic population variable. The population $N$ at a given time $t$ is governed by a probability distribution function:
$$Pr(i, j, t, n)$$
Where:
*   $i, j$: Coordinates of the node.
*   $t$: Time parameter (years).
*   $n$: Population count.
*   **Constraint:** For any specific node and time, the sum of probabilities over all possible population counts $n$ is equal to 1: $\sum_n Pr(i, j, t, n) = 1$.

## 2. Mobility and Trip Generation
Users perform random trips between an origin node $O(i, j)$ and a destination node $D(a, b)$. 

*   **Trip Probability:** The likelihood of a node being chosen as an origin or destination is directly proportional to its population at time $t$. 
*   **Example:** If $O$ is fixed and three possible destinations have populations of 1200, 1200, and 2400 respectively, the transition probabilities to those nodes are $[0.25, 0.25, 0.5]$.

### 2.1 Transit Logic
The movement follows a multimodal "First-Mile/Last-Mile" heuristic:
1.  **Access:** The user walks from the origin $O(i, j)$ to the nearest train station $S_{origin}$.
2.  **Line Haul:** The user travels via train to the station $S_{destination}$ closest to their final destination.
3.  **Egress:** The user walks from $S_{destination}$ to the final destination $D(a, b)$.

## 3. Cost Function
The objective function prioritizes minimizing the "walking" component of the commute.
*   **Primary Cost:** Distance from origin to $S_{origin}$ + distance from $S_{destination}$ to destination.
*   **Negligible Cost:** The time/distance spent on the train is considered zero for this optimization model.
*   **Metric:** The system must minimize the **expected average travel cost** across all users, considering the stochastic fluctuations of the population over $t$.

## 4. Constraints and Design Goals
The task is to design an optimal train route (Graph $G_{route}$) subject to the following:
*   **Topology:** The route can be either a **linear path** or a **closed cycle**.
*   **Capacity:** The route must consist of a maximum of $N$ stations.
*   **Robustness:** The placement of stations and the sequence of the route must be optimized to remain efficient despite the probabilistic nature of population growth/shift over time.
