# turtlebot3
tutlebot3に関するパッケージ　ちょびっといじったりしてるやつ

ここにメモとしてcartographerを使ったslamの方法を示す
## インストール
  ```shell 
  sudo apt install ros-melodic-cartographer ros-melodic-cartographer-ros ros-melodic-cartographer-ros-msgs ros-melodic-cartographer-rviz
  ```
## 変更点
  ```shell
  $ roscd turtlebot3_slam
  $ cd config
  $ emacs turtlebot3_lds_2d.lua
  -- tracking_frame = "imu_link",
     tracking_frame = "base_footprint",
  ```
  このように変更すること
  
## 使用方法
  ```shell
  $ roslaunch turtlebot3_gazebo turtlebot3_world.launch
  $ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=cartographer
  ```
  上記のコマンドで立ち上げればうまくいくはず
  
## rviz tf2に関して
なんかたまにtf2関連でrvizが立ち上がらんときがある（以下のエラーが出るとき）
  ```shell
  rviz: symbol lookup error: /opt/ros/melodic/lib/libtf.so: undefined symbol: _ZN7tf2_ros17TransformListenerC1ERN3tf210BufferCoreERKN3ros10NodeHandleEb
  ```
これはgeometry2関連のbranchを修正すればなんとかなる
  ```shell
  $ git clone -b melodic-devel https://github.com/ros/geometry2.git
  ```
  branchに関しては、各々変更したらいいかも？
  これをインストールしてcatkin buildすればいける
