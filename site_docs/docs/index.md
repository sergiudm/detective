detective：一款更适合中国宝宝的室友内卷监测工具
==================================================

## 介绍

detective是一款更适合中国宝宝的室友内卷监测工具，它可以帮助你监测室友的内卷行为，让你的寝室生活更加和谐。
> TODO：demo

## 环境要求
| 环境   | 版本                                              |
| ------ | ------------------------------------------------- |
| OS     | Ubuntu22.04, Raspberry Pi OS, Window11, Debian 12 |
| Python | 3.10                                              |

## 硬件清单
- Raspberry Pi 4B * 2
- 摄像头 * 2
- 蜂鸣器
- LED灯
- 面包板

## 安装依赖
创建虚拟环境
```bash
conda create -n your_env_name python=3.10
conda activate your_env_name
```
安装依赖
```bash
git clone https://github.com/sergiudm/detective.git
cd detective
pip install -r requirements.txt
```

## 使用说明
开始前，你需要配置`config.json`文件，
以下是一个示例：
```json
{
    "default_detect_mode": "others",
    "use_camera": true,
    "LED_pin": 18, # LED灯的引脚
    "use_visualization": false, # 是否使用可视化
    "server_email": "youremail@example.com",
    "server_email_password": "your email password",# 请使用授权码
    "target_email": [
        "email1",
        "email2"
    ],
    "smtp_server":"your smtp server",
    "smtp_port": 587,
    "video_path": "assets/videos/sit.mp4", # use_camera为false时，使用该视频
    "image_path": "resources", # 邮件中的图片
    "send_delay": 13,
    "effective_detection_duration": 2,
    "max_num_hands": 2,
    "min_detection_confidence": 0.65,
    "min_tracking_confidence": 0.65
}
```
>[!CAUTION] 
实际使用时，请删除`config.json`中的所有注释!

Linux:
```bash
cd detective
sudo chmod +x run.sh
./run.sh
```
Windows:
```bash
cd detective
python main.py
```

## 功能
- 检测是否有室友在内卷
    - 如果有，会自动响起警报，并且发微信通知你
- 检测你是不是卷过头了
    - 如果连续工作超过2小时（可在`config.json`中配置），会自动响起警报，并提醒你休息一下
- to do list
  - 检测 学习 与 玩游戏
    - 肩部、髋部、膝盖 夹角； 手部 位置
  - 报警：蜂鸣器（可换为便宜的喇叭）（直到结束学习才消失）、led、微信发消息
  - 开关门检测
    - 开关门 检测完成后： 人在寝室，才监控
  - 不良坐姿的检测
  - 魔术

## 如何贡献
本仓库仅使用了[mediapipe](https://github.com/google-ai-edge/mediapipe)中的人体姿态检测和手部检测功能，如果你有更多想法，欢迎：

- 提交PR
- 提交Issue
- 传播给更多的室友

## Acknowledgement
[mediapipe](https://github.com/google-ai-edge/mediapipe)