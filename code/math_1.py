import math

point_6 = {'編號：': 6, 'X ': 295, 'Y ': 263}
point_62 = {'編號：': 62, 'X ': 273, 'Y ': 338}
point_291 = {'編號：': 291, 'X ': 325, 'Y ': 340}

x1, y1 = point_6['X '], point_6['Y ']
x2, y2 = point_62['X '], point_62['Y ']
x3, y3 = point_291['X '], point_291['Y ']

def calculate_angle(line1, line2):
    # 線段的斜率
    slope1 = (line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0])
    slope2 = (line2[1][1] - line2[0][1]) / (line2[1][0] - line2[0][0])
    
# 計算角度
    angle_radians = abs(math.atan(slope2) - math.atan(slope1))
    angle_degrees = math.degrees(angle_radians)

    return angle_degrees

# 定義兩條線段
line1 = [(295, 263), (273, 338)]
line2 = [(295, 263), (325, 340)]

# 計算角度
angle = calculate_angle(line1, line2)
print(f"這兩條線的角度為 {angle}。")

distance_6_62 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
distance_6_291 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
distance_62_291 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)

print("編號 6 和 62 的距離:", distance_6_62)
print("編號 6 和 291 的距離:", distance_6_291)
print("編號 62 和 291 的距離:", distance_62_291)