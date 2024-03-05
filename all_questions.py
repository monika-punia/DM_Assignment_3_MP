# Add import files
import pickle
# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering, such as agglomerative clustering, handles outliers better than k-means because outliers often stay separate or merge late, making them easier to identify and remove."

    # For question (b)"

    # type: bool (True/False)
    answers["(b)"] = True

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means can give varied clusterings in different runs, but agglomerative hierarchical clustering remains consistent unless there are ties in proximity values."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "K-means clustering isn't always faster or less memory-intensive than agglomerative hierarchical clustering, and it's not considered the most efficient overall. Other algorithms like the leader algorithm can be more efficient."

    # type: bool (True/False)
    answers["(d)"] = False

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "In K-means post-processing, when a cluster is split by choosing a point as a new center, the SSE (Sum of Squared Errors) usually goes up because splitting spreads points farther from centroids."

    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In k-means, when the SSE (Sum of Squared Errors) goes down, it means the clusters are getting more cohesive and compact. SSE is like the opposite of cohesion, so a decrease is good."

    # For question (f)
    answers["(f)"] = True  # True if the statement is correct"

    # type: bool (True/False)
    answers["(f)"] = True

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "In k-means, when SSB (between sum of squares) goes up, it means clusters are getting more separated. So, if SSB increases, clusters become more distinct from each other."

    # type: bool (True/False)
    answers["(g)"] = False

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "In K-Means clustering, improving cohesion (lowering SSE) also boosts separation (raising SSB). SSE and SSB are linked through the total sum of squares (TSS)."

    # type: bool (True/False)
    answers["(h)"] = True

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "In k-means, the total sum of squares (TSS) always stays the same, connecting SSE (Within Sum of Squares) and BSS (Between Sum of Squares). It's shown by the equation: TSS = SSE + SSB."

    # type: bool (True/False)
    answers["(i)"] = True

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "In k-means, when cohesion goes up (SSE reduces), separation also goes up (SSB increases). SSE is linked to cluster cohesion inversely, while SSB is directly connected to cluster separation."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Each shaded circle has one centroid at its center because the clusters are too far apart for one centroid to pull points from another."

    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Each shaded region will have one centroid at its center, but the final clusters will include points from both regions because they are close and not circular."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "In the k-means final clustering, one cluster becomes empty because the centroid at 12.5 is farthest from all points compared to other clusters."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = "4*R**2"

    # type: a string that evaluates to a float
    answers["(b) SSE"] = "4*(a**2 + b**2 + R**2)"

    # type: a string that evaluates to a float
    answers["(c) SSE"] = "10*R**2"
    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "All points in circle A go to its centroid. About ⅓ of circle B's points (left third) go to the left centroid in B, and the rest (⅔ of B and all of C) go to the center of B. This makes the right centroid in B move to circle C due to more points. In the next iteration, each circle's points go to their own centroids, and K-means converges."

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Circles A and B are close, far from C. Points from both A and B go to A's centroid. C's points split between its centroids. A's centroid moves between A and B. Centroids in C slightly move apart but stay in C, each having half of C's points."

    # type: int
    answers["(c) Circle (a)"] = 0

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "A and B, close and far from C, make points from both go to A's centroid. C's points split between its centroids, each getting 50,000. A's centroid moves between A and B, and centroids in C slightly move apart but stay in C, each with half of C's points."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {'Group A' , 'Group B'}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Merging A and B due to their smallest link distance, showing closeness in their nearest points."

    # type: set
    answers["(b)"] = {'Group A' , 'Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Merging A and C due to their smallest complete link distance, showing high similarity between their furthest points."

    return answers





# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(a) boundary"] = {'D', 'G'}

    # type: set
    answers["(a) noise"] = {'A', 'H'}

    # type: set
    answers["(b) cluster 1"] = {'B', 'C', 'D', 'E', 'F', 'G'}

    # type: set
    answers["(b) cluster 2"] = {'I', 'J', 'L', 'M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B', 'C', 'E', 'F', 'I', 'J', 'L', 'M', 'D', 'G'}

    # type: set
    answers["(c)-a boundary"] = {'A', 'H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M'}

    # type: set
    answers["(c)-b cluster 2"] = set()

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "Cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 has high clustering entropy because of more varied land cover types."

    # type: string
    answers["(b)"] = "Cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 has low clustering entropy because it mainly represents water land cover with minimal variability."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "Diagonal entries look clear and mostly blue, showing strong cohesion within clusters. This uniformity suggests points in a cluster are closely grouped, maintaining consistent coherence."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Rows 1 and 3 match clusters A and C, shown by different colors off the diagonal, indicating varied distances from A (or C) to other clusters. Rows 2 and 4 match clusters B and D, reflecting similar observations."

    # type: string
    answers["(a) Matrix 2"] = "X"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "Two diagonal entries are notably crisp and mostly blue, showing better cohesion in clusters B and C. This highlights tighter relationships within these clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "Rows 1 and 4 have unclear diagonal entries and varied colors, indicating different distances from other clusters. Rows with sharp diagonal entries show two identical colors, suggesting equidistant relationships with two clusters and a greater distance from one cluster."

    # type: string
    answers["(a) Matrix 3"] = "Y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "Like Matrix 2, two diagonal entries are clear and intense blue, showing strong cohesion in clusters B and C. This consistency suggests robust relationships within these clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "In each row, two off-diagonal entries have similar colors, and one is different. This shows that each cluster is relatively closer to two other clusters than the remaining one, highlighting distinct inter-cluster relationships."

    # type: string
    answers["(b) Row 1"] = "A"

    # type: string
    answers["(b) Row 2"] = "B"

    # type: string
    answers["(b) Row 3"] = "C"

    # type: string
    answers["(b) Row 4"] = "D"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "Row 1 stands for Cluster A. The diagonal entry is less clear, suggesting weaker cohesion. Off-diagonal entries show different colors, indicating diverse distances from other clusters. Cluster A is closest to B, then C, and farthest from D."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "Row 2 represents Cluster B. The diagonal entry is clear, indicating strong cohesion. Two out of three off-diagonal entries share the same color, suggesting equidistant relationships with Clusters A and C, although the proximity to Cluster A is slightly less defined. Cluster B has the greatest distance from Cluster D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "Row 3 is for Cluster C. The diagonal is clear, showing strong cohesion. Two of three off-diagonal entries share a color, indicating equidistant relationships with Clusters B and D, but slightly less defined with Cluster D. Cluster C is farthest from Cluster A."

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "Row 4 is for Cluster D. Like Cluster A, the diagonal entry is less clear, suggesting lower cohesion. Off-diagonal entries have different colors, showing varied distances from other clusters. Cluster D is closest to Cluster C, then B, and farthest from A."

    return answers


# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ["Hierarchical", "Overlapping", "Partial"]

    # type: list
    answers["(b)"] = ["Partitional", "Exclusive", "Complete"]

    # type: list
    answers["(c)"] = ["Partitional", "Fuzzy", "Complete"]

    # type: list
    answers["(d)"] = ["Hierarchical", "Exclusive", "Complete"]

    # type: list
    answers["(e)"] = ["Partitional", "Exclusive", "Partial"]

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "Computer Science students are grouped by data mining class grades using exclusive clustering, but it's partial as not all students may have taken the class."

    return answers


# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "DBSCAN struggles with dense noise, impacting pattern identification."

    # type: string
    answers["(a) Figure (b)"] = "DBSCAN can spot patterns because they have higher density than noise."

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "DBSCAN's suitability depends on density distribution."

    # type: string
    answers["(b) Figure (a)"] = "K-means struggles to segment facial features because it assumes uniform density."

    # type: string
    answers["(b) Figure (b)"] = "K-means can segment facial features with the right number of clusters but might include background points."

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "K-means effectiveness depends on cluster assumptions."

    # type: string
    answers["(c)"] = "Spectral clustering, Gaussian mixture models, or Reciprocal density-based DBSCAN can effectively segment facial features in Figure (a)."

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
