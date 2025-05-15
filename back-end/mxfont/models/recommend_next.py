import numpy as np
from collections import Counter
import random


# 将四角编码映射为10维向量
def encode_to_vector(four_corner_code):
    vector = np.zeros(10)
    for digit in four_corner_code:
        if digit.isdigit():
            vector[int(digit)] += 1
    return vector

# 计算聚类中心
def compute_centroid(vectors):
    return np.mean(vectors, axis=0)

# 推荐与聚类中心最远的汉字
def recommend_next_char(reference_chars, candidate_chars):
    reference_vectors = np.array([encode_to_vector(four_corner_code_dict[char]) for char in reference_chars])
    centroid = compute_centroid(reference_vectors)
    
    max_distance = -1
    recommended_char = None

    for candidate in candidate_chars:
        if candidate not in four_corner_code_dict:
            continue
        vec = encode_to_vector(four_corner_code_dict[candidate])
        dist = np.linalg.norm(vec - centroid)
        if dist > max_distance:
            max_distance = dist
            recommended_char = candidate

    return recommended_char


