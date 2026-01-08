# 你的数据集只有 2 个关键点时的示例 metainfo
dataset_info = dict(
    dataset_name='shoe2kpt',
    paper_info=dict(
        author='',
        title='',
        container='',
        year='2026',
        homepage='',
    ),
    keypoint_info={
        0: dict(name='kp0', id=0, color=[255, 0, 0], type='', swap=''),
        1: dict(name='kp1', id=1, color=[0, 255, 0], type='', swap=''),
    },
    skeleton_info={
        0: dict(link=('kp0', 'kp1'), id=0, color=[255, 255, 0]),
    },
    joint_weights=[1.0, 1.0],
    # OKS 用，先给个很小的值（你后面也可以按业务调）
    sigmas=[0.01, 0.01],
)
