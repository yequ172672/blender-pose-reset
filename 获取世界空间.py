import bpy
import math

# 获取当前活动的对象（通常是骨骼对象）
selected_object = bpy.context.active_object

# 确保当前对象是骨骼对象
if selected_object and selected_object.type == 'ARMATURE':
    # 获取选中的骨骼
    selected_bones = selected_object.pose.bones

    # 遍历骨骼并获取其世界空间旋转值，忽略输出前缀为 "bone" 的骨骼
    for bone in selected_bones:
        # 检查骨骼名称是否以 "bone" 开头（不区分大小写），如果是则跳过
        if bone.name.lower().startswith("bone"):
            continue

        # 获取骨骼的世界空间旋转矩阵
        world_matrix = selected_object.matrix_world @ bone.matrix

        # 获取旋转矩阵的欧拉角表示（以弧度为单位）
        rotation_euler = world_matrix.to_euler()

        # 将弧度转换为角度
        rotation_degrees = [math.degrees(angle) for angle in rotation_euler]

        print("骨骼 '{}' 的世界空间旋转角度：{}".format(bone.name, rotation_degrees))
else:
    print("当前活动对象不是骨骼对象。")
