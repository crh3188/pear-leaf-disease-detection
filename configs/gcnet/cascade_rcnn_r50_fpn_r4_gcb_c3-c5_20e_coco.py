_base_ = '../cascade_rcnn/cascade_rcnn_r50_fpn_20e_coco.py'
model = dict(
    backbone=dict(plugins=[
        dict(
            cfg=dict(type='ContextBlock', ratio=1. / 4),
            stages=(False, True, True, True),
            position='after_conv3')
    ]))
