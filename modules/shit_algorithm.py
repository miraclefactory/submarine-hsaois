# 数据分离和平滑算法
# 目标检测任务中的元数据分离和元数据平滑

import PIL.Image as Image
from main import *

kernel = [[1,0,-1],
 		  [1,0,-1],
 		  [1,0,-1]]

"""
dHash
"""
def caculateHashValue(image):
    resize_width = 9
    resize_height = 8
    smaller_img = image.resize((resize_width, resize_height),Image.ANTIALIAS)
    grayscale_image = smaller_img.convert('L')
    pixels = list(grayscale_image.getdata())
    difference = []
    for row in range(resize_height):
        row_s_idx = row * resize_width
        for col in range(resize_width - 1):
            left_pixel_idx = row_s_idx + col
            difference.append(pixels[left_pixel_idx] > pixels[left_pixel_idx + 1])
    decimal_value = 0
    hash_base16 = ""
    for index, value in enumerate(difference):    
            if value:         
                    decimal_value += value * (2 ** (index % 8))   
            if index % 8 == 7:  
                    hash_base16 += str(hex(decimal_value)[2:].rjust(2, "0")) 
                    decimal_value = 0
    return hash_base16

def caculateHammingDistance(dhash1,dhash2):
    difference = (int(dhash1, 16)) ^ (int(dhash2, 16))
    return bin(difference).count("1")

"""
第一种:分两步(stupid)
"""
# //////////////////////////////////////////////////////////////////////////////////////////

threshold = 2			# INVALID DATA THRESHOLD
dominate_gene = []		# CURRENT DOMINATE GENE
current_gene_pool = []	# CURRENT GENE POOL
invalid = False			# INVALID DATA FLAG
output_data = []		# OUTPUT DATA

def evolution(input_list):
	global dominate_gene, current_gene_pool, invalid, output_data, buffer
	if len(input_list) > threshold:
		invalid = False
		input_list.sort()
		current_gene_pool.append(input_list)
		dominate_gene = max(current_gene_pool, key=current_gene_pool.count)
	else:
		invalid = True
		if dominate_gene != []:
			output_data.append(dominate_gene)
			print(current_gene_pool)
		dominate_gene = []
		current_gene_pool = []
#
# for data in input_list:
# 	evolution(data)

"""
第二种:只平滑(smart)
"""
# //////////////////////////////////////////////////////////////////////////////////////////

# 数据分割
def segementation(input_data, segement_size):
    for i in range(0, len(input_data), segement_size):
    	yield input_data[i:i+segement_size]

# 长度加权平均池化, a more agressive way is Stochastic-pooling（以权重作为概率随机抽样）
def length_weighted_average_pooling(input_list):
	avg_len = sum(len(i) * len(i) * 0.1 for i in input_list) / sum(len(i) * 0.1 for i in input_list)
	mini = min(abs(len(i) - avg_len) for i in input_list)
	return [i for i in input_list if abs(len(i) - avg_len) == mini][0]

# 特征最大池化
def feature_max_pooling(input_list):
	maxi = max(len(set(i)) for i in input_list)
	candidate_list = [i for i in input_list if len(set(i)) == maxi]
	return max((len(i), i) for i in candidate_list)[1]

# 特征加权平均池化
def feature_weighted_average_pooling(input_list):
	avg_feat_num = sum(len(set(i)) * len(set(i)) * 0.1 for i in input_list) / sum(len(set(i)) * 0.1 for i in input_list)
	mini = min(abs(len(set(i)) - avg_feat_num) for i in input_list)
	candidate_list = [i for i in input_list if abs(len(set(i)) - avg_feat_num) == mini]
	return max((len(set(i)), i) for i in candidate_list)[1]

# print(feature_max_pooling([length_weighted_average_pooling(i) for i in segementation(input_list, 4)]))
# print(feature_weighted_average_pooling([length_weighted_average_pooling(i) for i in segementation(input_list, 4)]))
