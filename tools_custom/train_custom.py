import os
import sys

# 让 python 能 import 到你本地仓库的 mmpose
REPO_ROOT = r"D:\github_code\mmpose-main"
sys.path.insert(0, REPO_ROOT)
os.chdir(REPO_ROOT)

from mmpose.utils import register_all_modules
from mmpose.registry import DATASETS

def main():
    register_all_modules()  # 官方示例也建议先注册模块:contentReference[oaicite:4]{index=4}

    data_root = r"D:/github_code/mmpose-main/custom_dataset/"  # 建议用 /
    ann_file = "annotations/test.json"
    img_prefix = "images/test/"  # 你的图片在 custom_dataset/images/test/

    dataset_cfg = dict(
        type="CocoDataset",
        data_root=data_root,
        data_mode="topdown",
        ann_file=ann_file,
        data_prefix=dict(img=img_prefix),
        # 引用你刚建的 metainfo 文件:contentReference[oaicite:5]{index=5}
        metainfo=dict(from_file="configs/_base_/datasets/shoe2kpt.py"),
        # 这里只做数据读取/检查，pipeline 给最小可用的一组
        # （正式训练时要按你选的模型 codec 来配完整 pipeline）
        pipeline=[
            dict(type="LoadImage"),
            dict(type="GetBBoxCenterScale"),
            dict(type="PackPoseInputs"),
        ],
        test_mode=True,
    )

    dataset = DATASETS.build(dataset_cfg)
    print("Dataset length:", len(dataset))
    print("Metainfo keys:", dataset.metainfo.keys())

    # 取一个样本看看结构
    sample = dataset[0]
    print("Sample keys:", sample.keys())
    # 通常会包含 inputs / data_samples（视 pipeline 而定）
    print("First sample:", type(sample))

if __name__ == "__main__":
    main()
