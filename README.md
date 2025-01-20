# celadon-py
获取 Celadon 项目使用到的脚本文件

> [!IMPORTANT]
> 脚本文件用于获取去除 AOSP 项目的 Celadon 源码树（镜像），而非完整的 Celadon 源码树，在使用此脚本之前应执行命令（以发行版 00.21.03.39 为例，根据需要自行替换发行版 XML 文件）：
> 
>    对于 Celadon 源码树：
>    ```shell
>    repo init -u https://github.com/projectceladon/manifest -b master -m stable-build/CIV_00.21.03.39_A11.xml
>    ```
>    对于源码树镜像：
>    ```shell
>    repo init -u https://github.com/projectceladon/manifest -b master -m stable-build/CIV_00.21.03.39_A11.xml --mirror
>    ```

## 使用方法

1. 执行命令：
   ```shell
   python run.py %celadon%/.repo/manifests/stable-build/CIV_00.21.03.39_A11.xml
   ```
  > [!WARNING]
  > 这里的 XML 文件路径应使用斜杠（“/”）而不是反斜杠（“\”）

2. 命令执行完成以后，原来的 `CIV_00.21.03.39_A11.xml` 文件被重命名为 `CIV_00.21.03.39_A11_origin.xml`，现有的 `CIV_00.21.03.39_A11.xml` 文件就是去除 AOSP 项目的 XML 文件。
3. 执行命令 `repo sync` 即可。
4. 如果想要免翻墙获取 AOSP 项目，可将原来的 `CIV_00.21.03.39_A11.xml` 中的 AOSP 项目源从 `https://android-review.googlesource.com` 改为 `https://mirrors.tuna.tsinghua.edu.cn/git/AOSP` 或者其他镜像源的 URL 再执行同步命令。
