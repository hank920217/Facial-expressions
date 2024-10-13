import math

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
angle = int(calculate_angle(line1, line2))
print(f"這兩條線的角度為 {angle}°")
