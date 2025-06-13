[app]
title = MyApp
package.name = myapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = 
    python==3.9.13,
    cython==0.29.36,
    PySide6==6.6.0,
    shiboken6==6.6.0
orientation = portrait
fullscreen = 0

# Android settings
android.archs = arm64-v8a
android.ndk_path = /home/runner/android-ndk-r25c
android.sdk_path = /home/runner/android-sdk
android.min_sdk_version = 21
android.target_sdk_version = 33
android.enable_androidx = True
p4a.branch = develop
