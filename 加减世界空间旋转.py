import bpy
import re
import math
import mathutils

# 定义包含骨骼名称和旋转角度信息的字符串
data = """
骨骼 'Bip01 R UpperArm' 的世界空间旋转角度：[2.683834682227535, -53.416993630607536, 0.9114545937923515]
"""

# 使用正则表达式提取骨骼名称和旋转角度
pattern = r"骨骼 '(.*?)' 的世界空间旋转角度：\[(.*?)\]"
matches = re.findall(pattern, data)

# 获取当前活动的对象（通常是骨骼对象）
selected_object = bpy.context.active_object

# 确保当前对象是骨骼对象
if selected_object and selected_object.type == 'ARMATURE':
    # 遍历匹配结果并设置骨骼的世界空间旋转
    for match in matches:
        bone_name = match[0]
        rotation_angles = [math.radians(float(angle)) for angle in match[1].split(', ')]

        # 获取骨骼对象
        bone = selected_object.pose.bones.get(bone_name)

        if bone:
            # 创建旋转矩阵并应用于骨骼
            rotation_matrix = mathutils.Euler(rotation_angles).to_matrix().to_4x4()
            bone.matrix_basis.identity()  # 重置骨骼的本地矩阵为单位矩阵
            bone.matrix_basis @= rotation_matrix  # 将旋转矩阵应用于骨骼的本地矩阵

            print("已设置骨骼 '{}' 的世界空间旋转角度为：{}".format(bone_name, [math.degrees(angle) for angle in rotation_angles]))
        else:
            print("找不到骨骼 '{}'。".format(bone_name))
else:
    print("当前活动对象不是骨骼对象。")
